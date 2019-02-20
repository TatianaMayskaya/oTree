from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):
        if self.player.round_number <= self.session.vars['num_rounds']:
            if self.player.id_in_group == 1:
                yield (pages.Principal, {'alpha1': 1, 'alpha2': 2, 'beta': -4})
            else:
                yield (pages.Agent, {'offer_accepted': random.choice([True, False])})
                if self.group.offer_accepted:
                    yield (pages.Agent, {'effort1': random.random(), 'effort2': random.random()})
        if self.player.round_number < self.session.vars['num_rounds']:
            yield (pages.Results)