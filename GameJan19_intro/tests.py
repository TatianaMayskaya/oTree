from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        if self.round_number == 1:
            yield (pages.Question, {'submitted_answer': 2})
            yield (pages.Question, {'submitted_answer': 80})
        if self.round_number == 2:
            yield (pages.Question, {'submitted_answer': 0})
        if self.round_number == 3:
            yield (pages.Question, {'submitted_answer': 2})
            yield (pages.Question, {'submitted_answer': 80})
            yield (pages.Question, {'submitted_answer': 80})
            yield (pages.Question, {'submitted_answer': 0})
            yield (pages.Question, {'submitted_answer': 25})
        if self.round_number == 4:
            yield (pages.Question, {'submitted_answer': 2})
            yield (pages.Question, {'submitted_answer': 80})
            yield (pages.Question, {'submitted_answer': 80})
            yield (pages.Question, {'submitted_answer': 10})
            yield (pages.Question, {'submitted_answer': 25})
        if self.round_number == 5:
            yield (pages.Question, {'submitted_answer': 15})
        if self.round_number == 6:
            yield (pages.Question, {'submitted_answer': 38})
        yield (pages.Results)
