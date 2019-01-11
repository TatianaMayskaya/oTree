from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.MyPage, {'order': self.round_number})
        else:
            if self.player.in_round(self.round_number - 1).in_game:
                yield (pages.MyPage, {'order': self.round_number})
        if self.round_number == Constants.num_rounds:
            yield (pages.Results)
