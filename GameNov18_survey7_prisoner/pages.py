from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'rate_survey_text': self.session.vars['rate_survey_text']}

    def before_next_page(self):
        self.participant.vars['prisoner_payoffs'] = []


class Prisoner(Page):
    form_model = 'player'
    form_fields = ['Prisoner_decision']

    def vars_for_template(self):
        return {
            'language': self.session.config['language'],
            'both_cooperate_payoff': Constants.Prisoner_both_cooperate_payoff[self.round_number-1],
            'both_defect_payoff': Constants.Prisoner_both_defect_payoff[self.round_number-1],
            'betrayed_payoff': Constants.Prisoner_betrayed_payoff[self.round_number - 1],
            'betray_payoff': Constants.Prisoner_betray_payoff[self.round_number - 1]
        }


class ResultsWaitPage(WaitPage):

    def vars_for_template(self):
        return {'title_text': self.session.vars['wait_page_title'], 'body_text': self.session.vars['wait_page_body']}

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_prisoner_payoff()
        if self.round_number == 2:
            for p in self.group.get_players():
                p.set_final_prisoner_payoff()


class PrisonerResults(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'language': self.session.config['language'],
            'my_decision': me.Prisoner_decision,
            'opponent_decision': opponent.Prisoner_decision,
            'payoff': me.Prisoner_payoff
        }


class Results(Page):
    def is_displayed(self):
        return self.round_number == 2

    def vars_for_template(self):
        return {
            'language': self.session.config['language'],
            'payoff_1': int(self.participant.vars['prisoner_payoffs'][0]),
            'payoff_2': int(self.participant.vars['prisoner_payoffs'][1]),
            'payment_question': self.player.payment_question,
            'payment': self.player.payoff_text
        }


page_sequence = [
    Introduction,
    Prisoner,
    ResultsWaitPage,
    PrisonerResults,
    Results
]
