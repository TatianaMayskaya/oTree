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


def utility_function(p, q, theta):
    arg = q - q * q / 2 / theta - p
    return 10*(1 - math.exp(-arg))


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            players = self.get_players()
            for p in players:
                p.theta = self.session.config['thetaH']
                p.participant.vars['income_1'] = '-'
                p.participant.vars['tax_1'] = '-'
                p.participant.vars['income_2'] = '-'
                p.participant.vars['tax_2'] = '-'
            low_type = random.sample(players, int(self.session.config['beta'] * len(players)))
            for p in low_type:
                p.theta = self.session.config['thetaL']
            self.session.vars['num_rounds'] = len(players)
            self.session.vars['n_low'] = len(low_type)
            self.session.vars['n_high'] = len(players) - len(low_type)

    def vars_for_admin_report(self):
        results_table = []
        players = self.get_players()
        for p in players:
            results_table.append(((p.id_in_group,
                                   p.participant.vars['income_1'],
                                   p.participant.vars['tax_1'],
                                   p.participant.vars['income_2'],
                                   p.participant.vars['tax_2'])))
        return {'results_table': results_table}


class Group(BaseGroup):
    income_1 = models.FloatField(min=0)
    tax_1 = models.FloatField()
    income_2 = models.FloatField(min=0)
    tax_2 = models.FloatField()


class Player(BasePlayer):
    theta = models.FloatField()
    income_1 = models.FloatField(min=0)
    tax_1 = models.FloatField()
    income_2 = models.FloatField(min=0)
    tax_2 = models.FloatField()
    income = models.FloatField(min=0)
    tax = models.FloatField()
