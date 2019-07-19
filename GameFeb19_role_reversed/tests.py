from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import time
import random


class PlayerBot(Bot):
    def play_round(self):
        timeout_value = 1
        if self.round_number == 1:
            yield (pages.Introduction)
        if self.round_number <= self.session.config['n_rounds']:
            time.sleep(timeout_value)
            yield (pages.RoleInGame)
            if self.player.role() == '1A' or self.player.role() == '1B':
                time.sleep(timeout_value)
                yield (pages.Offer, {'offer': random.randint(0, self.session.vars['endowment'])})
            time.sleep(timeout_value)
            yield (pages.ComputerChoice)
            time.sleep(timeout_value)
            if self.player.role() == '2C' and self.group.computer_choice == 'C':
                yield (pages.PlayerChoice, {'player_choice': random.choice(['A', 'B'])})
            elif self.player.role() == '2D' and self.group.computer_choice == 'D':
                yield (pages.PlayerChoice, {'player_choice': random.choice(['A', 'B'])})
            else:
                yield (pages.PlayerChoiceAnnouncement)
            if self.player.role() == '2C' or self.player.role() == '2D':
                time.sleep(timeout_value)
                yield (pages.Accept, {'response': random.randint(0, self.session.vars['endowment'])})
            time.sleep(timeout_value)
            yield (pages.Results)
