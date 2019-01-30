from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Government, {'income_1': 0.5, 'tax_1': 0.3, 'income_2': 0.2, 'tax_2': 4})
        if self.round_number <= self.session.vars['num_rounds']:
            yield (pages.Worker, {'income': 0.5})
