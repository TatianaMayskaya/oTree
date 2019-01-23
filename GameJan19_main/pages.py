from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, add_tokens, add_currency

import random


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def vars_for_template(self):
        return {'title_text': self.session.vars['wait_page_title'], 'body_text': self.session.vars['wait_page_body']}

    def after_all_players_arrive(self):
        self.subsession.do_my_shuffle()


class Introduction(Page):
    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'rate_text': add_currency(
                    self.session.config['currency_used'],
                    self.session.vars['rate'] * self.session.config['real_world_currency_per_point'])}

    def is_displayed(self):
        return self.round_number == 1


class RoleInGame(Page):
    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'role': self.player.role(),
                'round_number': self.round_number,
                'n_rounds': Constants.num_rounds}


class Offer(Page):
    form_model = 'player'
    form_fields = ['offer']

    def offer_max(self):
        return self.session.vars['endowment']

    def is_displayed(self):
        return self.player.role() == '1A' or self.player.role() == '1B'

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'role': self.player.role(),
                'round_number': self.round_number,
                'n_rounds': Constants.num_rounds,
                'offer_label': self.session.vars['offer'],
                'endowment': self.session.vars['endowment'],
                'payoff_if_rejected': self.session.vars['payoff_if_rejected']
                }


class OfferWaitPage(WaitPage):

    def after_all_players_arrive(self):
        if self.round_number < Constants.num_rounds:
            self.group.computer_choice = random.choice(['C', 'D'])
        else:
            self.group.computer_choice = 'C'

    def vars_for_template(self):
        return {'title_text': self.session.vars['wait_page_title'], 'body_text': self.session.vars['wait_page_body']}


class ComputerChoice(Page):
    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'round_number': self.round_number,
                'n_rounds': Constants.num_rounds,
                'computer_choice': self.group.computer_choice
                }


class PlayerChoice(Page):
    form_model = 'group'
    form_fields = ['player_choice']

    def is_displayed(self):
        if self.group.computer_choice == 'C':
            return self.player.role() == '2C'
        else:
            return self.player.role() == '2D'

    def vars_for_template(self):
        if self.group.computer_choice == 'C':
            computer_choice_opposite = 'D'
        else:
            computer_choice_opposite = 'C'
        return {'language': self.session.config['language'],
                'round_number': self.round_number,
                'n_rounds': Constants.num_rounds,
                'role': self.player.role(),
                'computer_choice_opposite': computer_choice_opposite,
                'player_choice_label': self.session.vars['player_choice']
                }


class PlayerChoiceWaitPage(WaitPage):
    def vars_for_template(self):
        return {'title_text': self.session.vars['wait_page_title'], 'body_text': self.session.vars['wait_page_body']}


class PlayerChoiceAnnouncement(Page):
    def is_displayed(self):
        if self.group.computer_choice == 'C':
            return not (self.player.role() == '2C')
        else:
            return not (self.player.role() == '2D')

    def vars_for_template(self):
        if self.group.computer_choice == 'C':
            computer_choice_opposite = 'D'
        else:
            computer_choice_opposite = 'C'
        if self.group.player_choice == 'A':
            player_choice_opposite = 'B'
        else:
            player_choice_opposite = 'A'
        return {'language': self.session.config['language'],
                'round_number': self.round_number,
                'n_rounds': Constants.num_rounds,
                'computer_choice': self.group.computer_choice,
                'computer_choice_opposite': computer_choice_opposite,
                'player_choice': self.group.player_choice,
                'player_choice_opposite': player_choice_opposite
                }


class Accept(Page):
    form_model = 'player'
    form_fields = ['response']

    def is_displayed(self):
        return self.player.role() == '2C' or self.player.role() == '2D'

    def vars_for_template(self):
        if self.group.player_choice == 'A':
            player_choice_opposite = 'B'
        else:
            player_choice_opposite = 'A'
        if self.player.role() == '2C' and self.group.computer_choice == 'C':
            partner = self.group.player_choice
        elif self.player.role() == '2D' and self.group.computer_choice == 'D':
            partner = self.group.player_choice
        else:
            partner = player_choice_opposite
        return {'language': self.session.config['language'],
                'role': self.player.role(),
                'round_number': self.round_number,
                'n_rounds': Constants.num_rounds,
                'response_label': self.session.vars['response'],
                'endowment': self.session.vars['endowment'],
                'payoff_if_rejected': self.session.vars['payoff_if_rejected'],
                'partner': partner
                }


class ResponseWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):
        return {'title_text': self.session.vars['wait_page_title'], 'body_text': self.session.vars['wait_page_body']}


class Results(Page):
    def vars_for_template(self):
        if self.group.computer_choice == 'C':
            computer_choice_opposite = 'D'
        else:
            computer_choice_opposite = 'C'
        if self.group.player_choice == 'A':
            player_choice_opposite = 'B'
        else:
            player_choice_opposite = 'A'
        return {'language': self.session.config['language'],
                'round_number': self.round_number,
                'n_rounds': Constants.num_rounds,
                'computer_choice': self.group.computer_choice,
                'computer_choice_opposite': computer_choice_opposite,
                'player_choice': self.group.player_choice,
                'player_choice_opposite': player_choice_opposite,
                'role': self.participant.vars['role'],
                'results_table': self.participant.vars['results_table'],
                'payment_round': self.participant.vars['payment_round'],
                'payment': self.participant.vars['payment_formula'] + ' = ' + self.participant.vars['payoff_text']
                }


page_sequence = [
    ShuffleWaitPage,
    Introduction,
    RoleInGame,
    Offer,
    OfferWaitPage,
    ComputerChoice,
    PlayerChoice,
    PlayerChoiceWaitPage,
    PlayerChoiceAnnouncement,
    Accept,
    ResponseWaitPage,
    Results
]
