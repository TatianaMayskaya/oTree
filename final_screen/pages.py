from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


def add_currency(currency_used, num):
    if currency_used == 0:
        return '$' + str(num)
    elif currency_used == 1:
        return '£' + str(num)
    else:
        if num % 10 == 1:
            return str(num) + ' рубль'
        elif (num % 10 == 2) | (num % 10 == 3) | (num % 10 == 4):
            return str(num) + ' рубля'
        else:
            return str(num) + ' рублей'


class PaymentInfo(Page):
    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'payment': self.participant.vars['payment_formula'] + ' = ' +
                           add_currency(self.session.config['currency_used'],
                                        float(self.participant.payoff_plus_participation_fee()))}


page_sequence = [
    PaymentInfo
]
