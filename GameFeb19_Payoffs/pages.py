from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from GameFeb19_intro.models import add_currency

from GameFeb19_intro.pages import Page, WaitPage

import random

from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Payoffs(Page):
    def vars_for_template(self):
        self.participant.vars['payoff_text'] = add_currency(
            self.session.config['currency_used'], float(self.participant.payoff_plus_participation_fee()))
        return {'role': self.participant.vars['role'],
                'role_reversed': self.participant.vars['role_reversed'],
                'roleUG': self.participant.vars['roleUG'],
                'roleUG_reversed': self.participant.vars['roleUG_reversed'],
                'results_table': self.participant.vars['results_table'],
                'results_table_reversed': self.participant.vars['results_table_reversed'],
                'results_tableUG': self.participant.vars['results_tableUG'],
                'results_tableUG_reversed': self.participant.vars['results_tableUG_reversed'],
                'payment_round': self.participant.vars['payment_round'],
                'payment_round_reversed': self.participant.vars['payment_round_reversed'],
                'payment_roundUG': self.participant.vars['payment_roundUG'],
                'payment_roundUG_reversed': self.participant.vars['payment_roundUG_reversed'],
                'payment_rounds_Q': self.participant.vars['payment_rounds_Q'],
                'payment': self.participant.vars['payment_formula'] + ' = ' + self.participant.vars['payoff_text'],
                'total_questions': range(1, self.session.config['total_questions'] + 1),
                'CT_part': self.session.vars['CT_part'],
                'Q_part': self.session.vars['Q_part'],
                'questions_CT': self.participant.vars['questions_CT'],
                'questions_Q': self.participant.vars['questions_Q'],
                'questions_correct_CT': self.participant.vars['questions_correct_CT'],
                'num_questions_CT': self.session.vars['num_questions_CT'],
                'num_questions_Q': self.session.vars['num_questions_Q']}


page_sequence = [
    Payoffs
]
