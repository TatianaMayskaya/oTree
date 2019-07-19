from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import time


class PlayerBot(Bot):
    timeout_value = 20

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        if not self.session.config['skip_test']:
            if self.round_number == 1:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 2})
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 80})
            if self.round_number == 2:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 0})
            if self.round_number == 3:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 2})
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 80})
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 80})
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 0})
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 25})
            if self.round_number == 4:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 2})
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 80})
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 80})
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 10})
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 25})
            if self.round_number == 5:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 15})
            if self.round_number == 6:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 38})
            time.sleep(self.timeout_value)
            yield (pages.Results)
