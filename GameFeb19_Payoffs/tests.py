from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import time


class PlayerBot(Bot):
    timeout_value = 20

    def play_round(self):
        time.sleep(self.timeout_value)
        yield (pages.Payoffs)
