from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        if self.round_number <= 3:
            yield (pages.GameAnnouncement)
        if self.player.id_in_group == 2 and self.round_number <= 2:
            yield (pages.Offer, {'amount_offered': 20})
        if self.player.id_in_group == 2 and self.round_number == 3:
            yield (pages.Offer, {'amount_offered_1': 30, 'amount_offered_2': 40})
        if self.player.id_in_group == 1 and self.round_number == 3:
            yield (pages.GameChoice, {'game_played': 1})
        if self.player.id_in_group == 1 and self.round_number <= 3:
            if self.round_number == 1 or (self.round_number == 3 and self.group.game_played == 1):
                yield (pages.Accept, {'response': 30})
            else:
                yield (pages.Accept)
