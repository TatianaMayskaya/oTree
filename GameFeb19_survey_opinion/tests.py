from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Question, {'submitted_answer': random.randint(1, 5)})
