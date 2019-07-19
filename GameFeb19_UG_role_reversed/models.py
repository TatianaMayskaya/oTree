from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.utils.translation import ugettext_lazy as _

from GameFeb19_intro.models import add_currency, add_tokens, TRNSL_ERR_MSG, translated_languages

from GameFeb19_main.models import (
    creating_session_template, for_admin_report, computer_choice_var, player_choice_var, offer_var, response_var,
    payment_round_var, player_role
)

import random

author = 'Tatiana Mayskaya'

doc = """
Base Game: Ultimatum Game with 4 players in a group and endogenous pairing
Ultimatum Game - 2
"""


class Constants(BaseConstants):
    name_in_url = 'GameFeb19_UG_role_reversed'
    players_per_group = 4
    num_rounds = 20  # >= self.session.config['n_rounds']


class Subsession(BaseSubsession):
    def creating_session(self):
        creating_session_template(self.session)

    def vars_for_admin_report(self):
        ultimatum_game = True
        return for_admin_report(self.get_groups(), ultimatum_game)


class Group(BaseGroup):
    computer_choice = computer_choice_var()
    player_choice = player_choice_var()


class Player(BasePlayer):
    offer = offer_var()
    response = response_var()
    payment_round = payment_round_var()

    def role(self):
        return player_role(self.id_in_group)