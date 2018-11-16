from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        role = 3-self.player.id_in_group
        return {'language': self.session.config['language'],
                'role': role,
                'part_num': self.participant.vars['survey_part']}


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

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        role = 3 - self.player.id_in_group
        return {'language': self.session.config['language'],
                'offer0_label': self.session.vars['offer0'],
                'offer1_label': self.session.vars['offer1'],
                'offer2_label': self.session.vars['offer2'],
                'endowment': self.session.vars['endowment'],
                'payoff_if_rejected': self.session.vars['payoff_if_rejected'],
                'role': role,
                'part_num': self.participant.vars['survey_part']}


class GameChoice(Page):
    form_model = 'group'
    form_fields = ['game_played']

    def game_played_choices(self):
        if self.session.config['language'] == 1:
            return [[1, 'Game 1'], [2, 'Game 2']]
        else:
            return [[1, 'Игра 1'], [2, 'Игра 2']]

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number == 3

    def vars_for_template(self):
        role = 3 - self.player.id_in_group
        return {'language': self.session.config['language'],
                'game_label': self.session.vars['game'],
                'role': role,
                'part_num': self.participant.vars['survey_part']}


class Accept(Page):
    form_model = 'group'

    def get_form_fields(self):
        if self.round_number == 1 or (self.round_number == 3 and self.group.game_played == 1):
            return ['response']
        else:
            return []

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        role = 3 - self.player.id_in_group
        return {'language': self.session.config['language'],
                'response_label': self.session.vars['response'],
                'endowment': self.session.vars['endowment'],
                'payoff_if_rejected': self.session.vars['payoff_if_rejected'],
                'role': role,
                'part_num': self.participant.vars['survey_part']}


class ResultsWaitPage(WaitPage):

    def vars_for_template(self):
        return {'title_text': self.session.vars['wait_page_title'], 'body_text': self.session.vars['wait_page_body']}

    def after_all_players_arrive(self):
        if self.round_number == Constants.num_rounds:
            for p in self.group.get_players():
                p.participant.vars['survey_part'] = p.participant.vars['survey_part'] + 1


page_sequence = [
    Introduction,
    GameAnnouncement,
    Offer,
    GameChoice,
    Accept,
    ResultsWaitPage
]
