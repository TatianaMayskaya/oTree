from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class PaymentInfo(Page):
    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'payment': self.participant.vars['payment_formula'] + ' = ' +
                    str(self.participant.payoff_plus_participation_fee())}


page_sequence = [
    PaymentInfo
]
