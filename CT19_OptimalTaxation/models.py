from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import math
import random

author = 'Tatiana Mayskaya'

doc = """
Contract Theory ICEF year 2019
Optimal Income Taxation
"""


class Constants(BaseConstants):
    name_in_url = 'CT19_OptimalTaxation'
    players_per_group = None
    num_rounds = 30  # maximum number of participants allowed


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            players = self.get_players()
            for p in players:
                p.theta = self.session.config['thetaH']
            low_type = random.sample(players, int(self.session.config['beta'] * len(players)))
            for p in low_type:
                p.theta = self.session.config['thetaL']
            self.session.vars['num_rounds'] = len(players)



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    theta = models.FloatField()
    income_1 = models.FloatField(min=0)
    tax_1 = models.FloatField()
    income_2 = models.FloatField(min=0)
    tax_2 = models.FloatField()
    income = models.FloatField(min=0)

