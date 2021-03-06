from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from GameFeb19_intro.pages import Page, WaitPage

from GameFeb19_intro.models import add_currency

from GameFeb19_main.pages import (
    RoleInGame, Offer, MatchAnnouncement, Accept, Results
)

from GameFeb19_main.models import do_my_shuffle, set_payoffs

import random

from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.session.vars['UG'] = True
        self.session.vars['reversed'] = True
        do_my_shuffle(self.subsession)


class Introduction(Page):
    def vars_for_template(self):
        return {'rate_text': add_currency(
            self.session.config['currency_used'],
            self.session.vars['rate_UG_reversed'] * self.session.config['real_world_currency_per_point'])}

    def is_displayed(self):
        return self.round_number == 1


class OfferWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.computer_choice = random.choice(['C', 'D'])
        self.group.player_choice = random.choice(['A', 'B'])


class ResponseWaitPage(WaitPage):
    def after_all_players_arrive(self):
        set_payoffs(self.group, 4)


page_sequence = [
    ShuffleWaitPage,
    Introduction,
    RoleInGame,
    Offer,
    OfferWaitPage,
    MatchAnnouncement,
    Accept,
    ResponseWaitPage,
    Results
]
