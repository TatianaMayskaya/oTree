from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = 'player'
    form_fields = ['submitted_answer']

    def vars_for_template(self):
        return {'language': self.session.config['language']}


page_sequence = [
    Question
]
