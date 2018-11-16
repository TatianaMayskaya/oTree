from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, add_tokens, add_currency
from django.conf import settings


class RoleInGame(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'language': self.session.config['language']}


class GameAnnouncement(Page):
    def vars_for_template(self):
        return {'language': self.session.config['language']}


class Offer(Page):
    form_model = 'group'

    def get_form_fields(self):
        if self.round_number == 3:
            return ['amount_offered_1', 'amount_offered_2']
        elif self.round_number <= 2:
            return ['amount_offered']
        else:
            return []

    def amount_offered_max(self):
        return self.session.vars['endowment']

    def amount_offered_1_max(self):
        return self.session.vars['endowment']

    def amount_offered_2_max(self):
        return self.session.vars['endowment']

    # def error_message(self, values):
    #     fields = self.get_form_fields()
    #     for f in fields:
    #         if values[f] < 0:
    #             return self.session.vars['too_little_offered']
    #         if values[f] > self.session.vars['endowment']:
    #             return self.session.vars['too_much_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'offer0_label': self.session.vars['offer0'],
                'offer1_label': self.session.vars['offer1'],
                'offer2_label': self.session.vars['offer2'],
                'endowment': self.session.vars['endowment'],
                'payoff_if_rejected': self.session.vars['payoff_if_rejected']
                }


class GameChoice(Page):
    form_model = 'group'
    form_fields = ['game_played']

    def game_played_choices(self):
        if self.session.config['language'] == 1:
            return [[1, 'Game 1'], [2, 'Game 2']]
        else:
            return [[1, 'Игра 1'], [2, 'Игра 2']]

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == 3

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'game_label': self.session.vars['game']
                }


class Accept(Page):
    form_model = 'group'

    def get_form_fields(self):
        if self.round_number == 1 or (self.round_number == 3 and self.group.game_played == 1):
            return ['response']
        else:
            return []

    # def response_max(self):
    #     return self.session.vars['endowment'] + 1

    # def error_message(self, values):
    #     fields = self.get_form_fields()
    #     for f in fields:
    #         if values[f] < 0:
    #             return self.session.vars['too_little_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'response_label': self.session.vars['response'],
                'endowment': self.session.vars['endowment'],
                'payoff_if_rejected': self.session.vars['payoff_if_rejected']
                }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):
        return {'title_text': self.session.vars['wait_page_title'], 'body_text': self.session.vars['wait_page_body']}


class Results(Page):
    def is_displayed(self):
        return self.round_number == 3

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'amount_offered_G1': add_tokens(self.session.config['language'], self.player.amount_offered_G1),
                'amount_offered_G2': add_tokens(self.session.config['language'], self.player.amount_offered_G2),
                'payoff_G1': add_tokens(self.session.config['language'], self.player.payoff_G1),
                'payoff_G2': add_tokens(self.session.config['language'], self.player.payoff_G2),
                'payoff_G3': add_tokens(self.session.config['language'], self.player.payoff_G3),
                'amount_offered_G3_G1': add_tokens(self.session.config['language'], self.player.amount_offered_G3_G1),
                'amount_offered_G3_G2': add_tokens(self.session.config['language'], self.player.amount_offered_G3_G2),
                'payment': self.participant.vars['payment_formula'] + ' = ' + self.player.payoff_text}


page_sequence = [
    RoleInGame,
    GameAnnouncement,
    Offer,
    GameChoice,
    Accept,
    ResultsWaitPage,
    Results
]
