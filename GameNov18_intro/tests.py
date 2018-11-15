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
        if self.round_number == 2:
            yield (pages.Question, {'submitted_answer': 2})
        if self.round_number == 3:
            yield (pages.Question, {'submitted_answer': 0})
        if self.round_number == 4:
            yield (pages.Question, {'submitted_answer': 80})
        if self.round_number == 5:
            yield (pages.Question, {'submitted_answer': 0})
        if self.round_number == 6:
            yield (pages.Question, {'submitted_answer': 30})
        if self.round_number == 7:
            yield (pages.Question, {'submitted_answer': 85})
        if self.round_number == 8:
            yield (pages.Question, {'submitted_answer': 2})
        if self.round_number == 9:
            yield (pages.Question, {'submitted_answer': 10})
        if self.round_number == 10:
            yield (pages.Question, {'submitted_answer': 100})
        if self.round_number == 11:
            yield (pages.Question, {'submitted_answer': 80})
        if self.round_number == 12:
            yield (pages.Question, {'submitted_answer': 0})
        if self.round_number == 13:
            yield (pages.Question, {'submitted_answer': 60})
        if self.round_number == 14:
            yield (pages.Question, {'submitted_answer': 0})
        if self.round_number == 15:
            yield (pages.Question, {'submitted_answer': 80})
        if self.round_number == 16:
            yield (pages.Question, {'submitted_answer': 70})
        if self.round_number == 17:
            yield (pages.Question, {'submitted_answer': 0})
        if self.round_number == 18:
            yield (pages.Question, {'submitted_answer': 50})
        if self.round_number == 19:
            yield (pages.Question, {'submitted_answer': 0})
        if self.round_number == 20:
            yield (pages.Question, {'submitted_answer': 10})
        yield (pages.Results)
