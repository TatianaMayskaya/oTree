from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import time

class PlayerBot(Bot):

    def play_round(self):
        yield (pages.RoleInGame)
        if self.player.role() == '1A' or self.player.role() == '1B':
            yield (pages.Offer, {'offer': 20})
        yield (pages.ComputerChoice)
        if self.player.role() == '2C' and self.group.computer_choice == 'C':
            yield (pages.PlayerChoice, {'player_choice': 'A'})
        elif self.player.role() == '2D' and self.group.computer_choice == 'D':
            yield (pages.PlayerChoice, {'player_choice': 'A'})
        else:
            yield (pages.PlayerChoiceAnnouncement)
        if self.player.role() == '2C' or self.player.role() == '2D':
            yield (pages.Accept, {'response': 20})
        time.sleep(15)
        yield (pages.Results)