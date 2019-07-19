from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.utils.translation import ugettext_lazy as _

from GameFeb19_intro.models import add_currency, add_tokens, TRNSL_ERR_MSG, translated_languages

import random

author = 'Tatiana Mayskaya'

doc = """
Base Game: Ultimatum Game with 4 players in a group and endogenous pairing
main part
"""


def reshuffling(players, round_number, n_rounds, reverse):
    group_matrix = []
    if round_number < n_rounds:
        if round_number == 1:
            if reverse:
                players2 = [p for p in players if p.participant.vars['treated'] + p.participant.vars['control'] == 0]
                players1 = [p for p in players if p.participant.vars['treated'] + p.participant.vars['control'] > 0]
            else:
                random.shuffle(players)
                while players:
                    new_group = [players.pop(), players.pop(), players.pop(), players.pop()]
                    group_matrix.append(new_group)
        else:
            players1 = [p for p in players if p.participant.vars['treated'] + p.participant.vars['control'] == 0]
            players2 = [p for p in players if p.participant.vars['treated'] + p.participant.vars['control'] > 0]
        if (round_number > 1) or reverse:
            random.shuffle(players1)
            random.shuffle(players2)
            while players1:
                new_group = [players1.pop(), players1.pop(), players2.pop(), players2.pop()]
                group_matrix.append(new_group)
    else:
        T_players = [p for p in players if
                     p.participant.vars['treated'] == 1 and p.participant.vars['control'] == 0]
        C_players = [p for p in players if
                     p.participant.vars['treated'] == 0 and p.participant.vars['control'] == 1]
        TC_players = [p for p in players if
                      p.participant.vars['treated'] == 1 and p.participant.vars['control'] == 1]
        N_players = [p for p in players if
                     p.participant.vars['treated'] == 0 and p.participant.vars['control'] == 0]
        random.shuffle(T_players)
        random.shuffle(C_players)
        random.shuffle(TC_players)
        random.shuffle(N_players)
        while N_players:
            if C_players:  # list is not empty
                p3 = C_players.pop()
            elif TC_players:
                p3 = TC_players.pop()
            else:
                p3 = T_players.pop()
            if T_players:
                p4 = T_players.pop()
            elif TC_players:
                p4 = TC_players.pop()
            else:
                p4 = C_players.pop()
            new_group = [N_players.pop(), N_players.pop(), p3, p4]
            group_matrix.append(new_group)
    return group_matrix


def for_admin_report(groups, ultimatum_game):
    players = []
    for group in groups:
        for player in group.get_players():
            if player.role() == '1A' or player.role() == '1B':
                role = 'Player 1'
                choice = player.offer
            elif ultimatum_game:  # simple ultimatum game
                role = 'Player 2'
                choice = player.response
            elif (player.role() == '2C' and group.computer_choice == 'C') or (
                    player.role() == '2D' and group.computer_choice == 'D'):
                role = 'Player 2T'
                choice = player.response
            else:
                role = 'Player 2C'
                choice = player.response
            players.append((player.participant.label, role, choice))
    return {'players': players}


class Constants(BaseConstants):
    name_in_url = 'GameFeb19_main'
    players_per_group = 4
    num_rounds = 20  # >= self.session.config['n_rounds']


def creating_session_template(session):
    assert session.config['language'] in translated_languages, TRNSL_ERR_MSG


def do_my_shuffle(subsession):
    group_matrix = reshuffling(subsession.get_players(), subsession.round_number, subsession.session.config['n_rounds'],
                               subsession.session.vars['reversed'])
    subsession.set_group_matrix(group_matrix)
    subsession.group_randomly(fixed_id_in_group=True)


class Subsession(BaseSubsession):
    def creating_session(self):
        creating_session_template(self.session)

    def vars_for_admin_report(self):
        ultimatum_game = False
        return for_admin_report(self.get_groups(), ultimatum_game)


def computer_choice_var():
    return models.StringField(choices=['C', 'D'])


def player_choice_var():
    return models.StringField(choices=[['A', _('Player 1A')], ['B', _('Player 1B')]],
                              widget=widgets.RadioSelectHorizontal)


def set_payoffs(group, game_number):
    p1A, p1B, p2C, p2D = group.get_players()
    if (group.computer_choice == 'C' and group.player_choice == 'A') or (
            group.computer_choice == 'D' and group.player_choice == 'B'):
        p1A.response = p2C.response
        p1B.response = p2D.response
        p2C.offer = p1A.offer
        p2D.offer = p1B.offer
    else:
        p1A.response = p2D.response
        p1B.response = p2C.response
        p2C.offer = p1B.offer
        p2D.offer = p1A.offer
    for p in group.get_players():
        set_payoffs_for_player(p, game_number)


class Group(BaseGroup):
    computer_choice = computer_choice_var()
    player_choice = player_choice_var()


def offer_var():
    return models.IntegerField(min=0)


def response_var():
    return models.IntegerField(min=0)


def payment_round_var():
    return models.BooleanField(initial=True)


def player_role(id_in_group):
    if id_in_group == 1:
        return '1A'
    if id_in_group == 2:
        return '1B'
    if id_in_group == 3:
        return '2C'
    if id_in_group == 4:
        return '2D'


def set_payoffs_for_player(player, game_number):
    if player.offer < player.response:
        player.payoff = player.session.vars['payoff_if_rejected']
        if player.role() == '1A' or player.role() == '1B':
            response = _('your offer was rejected')
        else:
            response = _('you rejected this offer')
    else:
        if player.role() == '1A' or player.role() == '1B':
            response = _('your offer was accepted')
            player.payoff = player.session.vars['endowment'] - player.offer
        else:
            response = _('you accepted this offer')
            player.payoff = player.offer

    if player.round_number == 1:
        payment_round = random.choice(range(1, player.session.config['n_rounds'] + 1))
        if game_number == 1:
            player.participant.vars['payment_round'] = payment_round
        elif game_number == 2:
            player.participant.vars['payment_round_reversed'] = payment_round
        elif game_number == 3:
            player.participant.vars['payment_roundUG'] = payment_round
        else:
            player.participant.vars['payment_roundUG_reversed'] = payment_round
        if game_number == 1:
            player.participant.vars['payment_formula'] = ''
        player.participant.vars['treated'] = 0
        player.participant.vars['control'] = 0
        if player.id_in_group <= 2:
            role = 1
        else:
            role = 2
        if game_number == 1:
            player.participant.vars['role'] = role
        elif game_number == 2:
            player.participant.vars['role_reversed'] = role
        elif game_number == 3:
            player.participant.vars['roleUG'] = role
        else:
            player.participant.vars['roleUG_reversed'] = role
    results_table = (player.round_number, add_tokens(player.session.config['language'], player.offer), response,
                     add_tokens(player.session.config['language'], int(player.payoff)))
    if player.round_number == 1:
        if game_number == 1:
            player.participant.vars['results_table'] = []
        elif game_number == 2:
            player.participant.vars['results_table_reversed'] = []
        elif game_number == 3:
            player.participant.vars['results_tableUG'] = []
        else:
            player.participant.vars['results_tableUG_reversed'] = []
    if game_number == 1:
        player.participant.vars['results_table'].append(results_table)
    elif game_number == 2:
        player.participant.vars['results_table_reversed'].append(results_table)
    elif game_number == 3:
        player.participant.vars['results_tableUG'].append(results_table)
    else:
        player.participant.vars['results_tableUG_reversed'].append(results_table)

    if (player.role() == '2C' and player.group.computer_choice == 'C') or (
            player.role() == '2D' and player.group.computer_choice == 'D'):
        player.participant.vars['treated'] = 1
    elif player.id_in_group >= 3:
        player.participant.vars['control'] = 1

    if game_number == 1:
        payment_round = player.participant.vars['payment_round']
    elif game_number == 2:
        payment_round = player.participant.vars['payment_round_reversed']
    elif game_number == 3:
        payment_round = player.participant.vars['payment_roundUG']
    else:
        payment_round = player.participant.vars['payment_roundUG_reversed']
    if player.round_number != payment_round:
        player.payoff = 0
        player.payment_round = False
    else:
        if game_number == 1:
            player.participant.vars['payment_formula'] = add_currency(player.session.config['currency_used'],
                                                                      player.session.config['participation_fee'])
            rate = player.session.vars['rate']
        elif game_number == 2:
            rate = player.session.vars['rate_reversed']
        elif game_number == 3:
            rate = player.session.vars['rate_UG']
        else:
            rate = player.session.vars['rate_UG_reversed']
        player.participant.vars['payment_formula'] = \
            player.participant.vars['payment_formula'] + \
            ' + ' + str(int(player.payoff)) + '*' + \
            add_currency(player.session.config['currency_used'],
                         rate * player.session.config['real_world_currency_per_point'])
        player.payoff = player.payoff * rate
        # player.participant.vars['payoff_text'] = add_currency(
        #     player.session.config['currency_used'], float(player.participant.payoff_plus_participation_fee()))


class Player(BasePlayer):
    offer = offer_var()
    response = response_var()
    payment_round = payment_round_var()

    def role(self):
        return player_role(self.id_in_group)

    # def set_payoffs(self, game_number):
    #     if self.offer < self.response:
    #         self.payoff = self.session.vars['payoff_if_rejected']
    #         if self.role() == '1A' or self.role() == '1B':
    #             response = _('your offer was rejected')
    #         else:
    #             response = _('you rejected this offer')
    #     else:
    #         if self.role() == '1A' or self.role() == '1B':
    #             response = _('your offer was accepted')
    #             self.payoff = self.session.vars['endowment'] - self.offer
    #         else:
    #             response = _('you accepted this offer')
    #             self.payoff = self.offer
    #
    #     if self.round_number == 1:
    #         payment_round = random.choice(range(1, self.session.config['n_rounds'] + 1))
    #         if game_number == 1:
    #             self.participant.vars['payment_round'] = payment_round
    #         elif game_number == 2:
    #             self.participant.vars['payment_round_reversed'] = payment_round
    #         elif game_number == 3:
    #             self.participant.vars['payment_roundUG'] = payment_round
    #         else:
    #             self.participant.vars['payment_roundUG_reversed'] = payment_round
    #         if game_number == 1:
    #             self.participant.vars['payment_formula'] = ''
    #         self.participant.vars['treated'] = 0
    #         self.participant.vars['control'] = 0
    #         if self.id_in_group <= 2:
    #             role = 1
    #         else:
    #             role = 2
    #         if game_number == 1:
    #             self.participant.vars['role'] = role
    #         elif game_number == 2:
    #             self.participant.vars['role_reversed'] = role
    #         elif game_number == 3:
    #             self.participant.vars['roleUG'] = role
    #         else:
    #             self.participant.vars['roleUG_reversed'] = role
    #     results_table = [[self.round_number, add_tokens(self.session.config['language'], self.offer), response,
    #                       add_tokens(self.session.config['language'], int(self.payoff))]]
    #     if self.round_number == 1:
    #         if game_number == 1:
    #             self.participant.vars['results_table'] = results_table
    #         elif game_number == 2:
    #             self.participant.vars['results_table_reversed'] = results_table
    #         elif game_number == 3:
    #             self.participant.vars['results_tableUG'] = results_table
    #         else:
    #             self.participant.vars['results_tableUG_reversed'] = results_table
    #     else:
    #         if game_number == 1:
    #             self.participant.vars['results_table'].append(results_table)
    #         elif game_number == 2:
    #             self.participant.vars['results_table_reversed'].append(results_table)
    #         elif game_number == 3:
    #             self.participant.vars['results_tableUG'].append(results_table)
    #         else:
    #             self.participant.vars['results_tableUG_reversed'].append(results_table)
    #
    #     if (self.role() == '2C' and self.group.computer_choice == 'C') or (
    #             self.role() == '2D' and self.group.computer_choice == 'D'):
    #         self.participant.vars['treated'] = 1
    #     elif self.id_in_group >= 3:
    #         self.participant.vars['control'] = 1
    #
    #     if game_number == 1:
    #         payment_round = self.participant.vars['payment_round']
    #     elif game_number == 2:
    #         payment_round = self.participant.vars['payment_round_reversed']
    #     elif game_number == 3:
    #         payment_round = self.participant.vars['payment_roundUG']
    #     else:
    #         payment_round = self.participant.vars['payment_roundUG_reversed']
    #     if self.round_number != payment_round:
    #         self.payoff = 0
    #         self.payment_round = False
    #     else:
    #         if game_number == 1:
    #             self.participant.vars['payment_formula'] = add_currency(self.session.config['currency_used'],
    #                                                                     self.session.config['participation_fee'])
    #             rate = self.session.vars['rate']
    #         elif game_number == 2:
    #             rate = self.session.vars['rate_reversed']
    #         elif game_number == 3:
    #             rate = self.session.vars['rate_UG']
    #         else:
    #             rate = self.session.vars['rate_UG_reversed']
    #         self.participant.vars['payment_formula'] = \
    #             self.participant.vars['payment_formula'] + \
    #             ' + ' + str(int(self.payoff)) + '*' + \
    #             add_currency(self.session.config['currency_used'],
    #                          rate * self.session.config['real_world_currency_per_point'])
    #         self.payoff = self.payoff * rate
    #         self.participant.vars['payoff_text'] = add_currency(
    #             self.session.config['currency_used'], float(self.participant.payoff_plus_participation_fee()))
