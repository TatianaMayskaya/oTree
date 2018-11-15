from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'rate_survey_text': self.session.vars['rate_survey_text']}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    ResultsWaitPage,
    Results
]
