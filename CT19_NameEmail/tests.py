from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.participant.label[0] == '_' and self.session.config['Email'] == 1:
            yield (pages.ContactInfo, {'name': 'Tatiana', 'email': 'tmay@gmail.com'})
        elif self.participant.label[0] == '_':
            yield (pages.ContactInfo, {'name': 'Tatiana'})
        elif self.session.config['Email'] == 1:
            yield (pages.ContactInfo, {'email': 'tmay@gmail.com'})

