from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        yield (pages.Rules)
        if self.player.id_in_group == 1:
            yield (pages.Send, {'sent_amount': 10})
        if self.player.id_in_group == 2:
            yield (pages.SendBack, {'sent_back_amount': 10*Constants.multiplier[self.round_number - 1]})
        yield(pages.TrustResults)
        if self.round_number == Constants.num_rounds:
            yield(pages.Results)
