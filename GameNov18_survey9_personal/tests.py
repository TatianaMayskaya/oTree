from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        num = self.participant.vars['questions'][self.round_number - 1]
        if num == 1:
            yield (pages.Question, {'age': 25})
        if num == 2:
            yield (pages.Question, {'gender': 0})
        if num == 3:
            yield (pages.Question, {'field': 3})
        if num == 4:
            yield (pages.Question, {'native_language': 'English, Spanish'})
        if num == 5:
            yield (pages.Question, {'income': 5})
        if num == 6:
            yield (pages.Question, {'riskat': 3})
        if num == 7:
            yield (pages.Question, {'happy_now': 0})
        if num == 8:
            yield (pages.Question, {'happy_future': 8})
        if num == 9:
            yield (pages.Question, {'trust': 10})
        if num == 10:
            yield (pages.Question, {'freedom': 1})
        if num == 11:
            yield (pages.Question, {'democracy': 0})
        if num == 12:
            yield (pages.Question, {'democracy_live': 4})
