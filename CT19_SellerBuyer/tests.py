from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group == 1:
            yield (pages.Seller, {'price_1': 1, 'price_2': 1, 'price_3': 1, 'price_4': 1, 'price_5': 1,
                                  'quality_1': 2, 'quality_2': 2, 'quality_3': 2, 'quality_4': 2, 'quality_5': 2})
        else:
            yield (pages.Buyer, {'offer_accepted': 1})
        yield (pages.Results)
