from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import time

class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        yield (pages.Prisoner, {'Prisoner_decision': 'A1'})
        yield (pages.PrisonerResults)
        if self.round_number == 2:
            time.sleep(15)
            yield (pages.Results)
