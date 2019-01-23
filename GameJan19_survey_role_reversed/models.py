from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


import random

author = 'Tatiana Mayskaya'

doc = """
Base Game: Ultimatum Game with 4 players in a group and endogenous pairing
survey: roles reversed 
"""


def add_currency(currency_used, num):
    if currency_used == 0:
        return '$' + str(num)
    elif currency_used == 1:
        return '£' + str(num)
    else:
        if num % 10 == 1:
            return str(num) + ' рубль'
        elif (num % 10 == 2) | (num % 10 == 3) | (num % 10 == 4):
            return str(num) + ' рубля'
        else:
            return str(num) + ' рублей'


def add_tokens(language, num):
    if language == 1:
        if num != 1:
            return str(num) + ' tokens'
        else:
            return str(num) + ' token'
    else:
        if num % 10 == 1:
            return str(num) + ' жетон'
        elif (num % 10 == 2) | (num % 10 == 3) | (num % 10 == 4):
            return str(num) + ' жетона'
        else:
            return str(num) + ' жетонов'


class Constants(BaseConstants):
    name_in_url = 'GameJan19_survey_role_reversed'
    players_per_group = 4
    num_rounds = 8  # make sure it coincides with self.session.config['n_rounds']


class Subsession(BaseSubsession):
    def do_my_shuffle(self):
        players = self.get_players()
        group_matrix = []
        if self.round_number < Constants.num_rounds:
            if self.round_number == 1:
                players2 = [p for p in players if p.participant.vars['treated'] + p.participant.vars['control'] == 0]
                players1 = [p for p in players if p.participant.vars['treated'] + p.participant.vars['control'] > 0]
            else:
                players1 = [p for p in players if p.participant.vars['treated'] + p.participant.vars['control'] == 0]
                players2 = [p for p in players if p.participant.vars['treated'] + p.participant.vars['control'] > 0]
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
        self.set_group_matrix(group_matrix)
        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    computer_choice = models.StringField(choices=['C', 'D'])
    player_choice = models.StringField(choices=[['A', 'Player 1A'], ['B', 'Player 1B']],
                                       widget=widgets.RadioSelectHorizontal)

    def set_payoffs(self):
        p1A, p1B, p2C, p2D = self.get_players()
        if (self.computer_choice == 'C' and self.player_choice == 'A') or (
                self.computer_choice == 'D' and self.player_choice == 'B'):
            p1A.response = p2C.response
            p1B.response = p2D.response
            p2C.offer = p1A.offer
            p2D.offer = p1B.offer
        else:
            p1A.response = p2D.response
            p1B.response = p2C.response
            p2C.offer = p1B.offer
            p2D.offer = p1A.offer
        for p in self.get_players():
            p.set_payoffs()


class Player(BasePlayer):
    offer = models.IntegerField(min=0)
    response = models.IntegerField(min=0)
    payment_round = models.BooleanField(initial=True)

    def set_payoffs(self):
        if self.offer < self.response:
            self.payoff = self.session.vars['payoff_if_rejected']
            if self.session.config['language'] == 1:
                response = 'rejected'
            else:
                if self.id_in_group <= 2:
                    response = 'отклонено'
                else:
                    response = 'отклонили'
        else:
            if self.session.config['language'] == 1:
                response = 'accepted'
            else:
                if self.id_in_group <= 2:
                    response = 'принято'
                else:
                    response = 'приняли'
            if self.role() == '1A' or self.role() == '1B':
                self.payoff = self.session.vars['endowment'] - self.offer
            else:
                self.payoff = self.offer

        if self.round_number == 1:
            self.participant.vars['payment_round_reversed'] = random.choice(range(1, Constants.num_rounds + 1))
            self.participant.vars['payoff_text'] = ''
            self.participant.vars['treated'] = 0
            self.participant.vars['control'] = 0
            if self.id_in_group <= 2:
                self.participant.vars['role_reversed'] = 1
            else:
                self.participant.vars['role_reversed'] = 2
            self.participant.vars['results_table_reversed'] = \
                [[1, add_tokens(self.session.config['language'], self.offer), response,
                  add_tokens(self.session.config['language'], int(self.payoff))]]
        else:
            self.participant.vars['results_table_reversed'].append((
                self.round_number, add_tokens(self.session.config['language'], self.offer), response,
                add_tokens(self.session.config['language'], int(self.payoff))))
        if (self.role() == '2C' and self.group.computer_choice == 'C') or (
                self.role() == '2D' and self.group.computer_choice == 'D'):
            self.participant.vars['treated'] = 1
        elif self.id_in_group >= 3:
            self.participant.vars['control'] = 1

        if self.round_number != self.participant.vars['payment_round_reversed']:
            self.payoff = 0
            self.payment_round = False
        else:
            self.participant.vars['payment_formula'] = \
                self.participant.vars['payment_formula'] + \
                ' + ' + str(int(self.payoff)) + '*' + \
                add_currency(self.session.config['currency_used'],
                             self.session.vars['rate_reversed'] * self.session.config['real_world_currency_per_point'])
            self.payoff = self.payoff * self.session.vars['rate_reversed']
            self.participant.vars['payoff_text'] = add_currency(
                self.session.config['currency_used'], float(self.participant.payoff_plus_participation_fee()))

    def role(self):
        if self.id_in_group == 1:
            return '1A'
        if self.id_in_group == 2:
            return '1B'
        if self.id_in_group == 3:
            return '2C'
        if self.id_in_group == 4:
            return '2D'