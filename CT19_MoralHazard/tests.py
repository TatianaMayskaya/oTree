from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):

    def play_round(self):
        if self.player.round_number <= self.session.vars['num_rounds']:
            if self.player.id_in_group == 1:
                if self.session.vars['binary']:
                    yield (pages.Principal, {'w0': 1, 'w1': 2})
                else:
                    yield (pages.Principal, {'t': 1, 's': 2})
            else:
                yield (pages.Agent, {'offer_accepted': random.choice([True, False])})
                if self.group.offer_accepted:
                    if self.session.vars['binary']:
                        yield (pages.Agent, {'effort_binary': random.choice([0, 1])})
                    else:
                        yield (pages.Agent, {'effort_cont': 100*random.random()})
        if self.player.round_number < self.session.vars['num_rounds']:
            yield (pages.Results)
