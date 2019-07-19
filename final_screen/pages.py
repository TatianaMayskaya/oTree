from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from GameFeb19_intro.pages import Page, WaitPage

from GameFeb19_intro.models import add_currency


class PaymentInfo(Page):
    def vars_for_template(self):
        return {'payment': self.participant.vars['payment_formula'] + ' = ' +
                           add_currency(self.session.config['currency_used'],
                                        float(self.participant.payoff_plus_participation_fee()))}


page_sequence = [
    PaymentInfo
]
