from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = 'player'
    form_fields = ['submitted_answer']

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'part_num': self.participant.vars['survey_part']}

    def before_next_page(self):
        if self.round_number == Constants.num_rounds:
            self.participant.vars['survey_part'] = self.participant.vars['survey_part'] + 1


page_sequence = [
    Question
]
