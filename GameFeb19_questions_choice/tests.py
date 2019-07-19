from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import time


class PlayerBot(Bot):
    timeout_value = 20

    def play_round(self):
        if self.round_number == 1:
            time.sleep(self.timeout_value)
            yield (pages.Introduction)
        if not self.session.config['skip_CognitiveTest']:
            if self.player.question_id == 1:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 10})
            if self.player.question_id == 2:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 100})
            if self.player.question_id == 3:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 24})
            if self.player.question_id == 4:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 9})
            if self.player.question_id == 5:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 29})
            if self.player.question_id == 6:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 20})
            if self.player.question_id == 7:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer_options': 2})
            if self.player.question_id == 8:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 45})
            if self.player.question_id == 9:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 2})
            if self.player.question_id == 10:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 400})
            if self.player.question_id == 11:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 80})
            if self.player.question_id == 12:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 3})
            if self.player.question_id == 13:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 21})
            if self.player.question_id == 14:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer': 24})
            if self.player.question_id == 15:
                time.sleep(self.timeout_value)
                yield (pages.Question, {'submitted_answer_options': 2})
