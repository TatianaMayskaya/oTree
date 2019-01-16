from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import csv
import math
import random

author = 'Tatiana Mayskaya'

doc = """
Contract Theory ICEF year 2019
Seller-Buyer game
"""


class Constants(BaseConstants):
    name_in_url = 'CT19_SellerBuyer'
    players_per_group = 2

    num_rounds = 30  # maximum number of rounds allowed


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=False)
        if self.round_number == 1:
            with open(self.session.config['file']) as parameters_file:
                self.session.vars['parameters'] = list(csv.DictReader(parameters_file))
            self.session.vars['num_rounds'] = len(self.session.vars['parameters'])
            self.session.vars['beta'] = []
            self.session.vars['c'] = []
            self.session.vars['thetaL'] = []
            self.session.vars['thetaH'] = []
            self.session.vars['uL'] = []
            self.session.vars['uH'] = []
            self.session.vars['p_offered'] = []
            self.session.vars['q_offered'] = []
            self.session.vars['n_offered'] = []
            self.session.vars['n_accepted'] = []
            self.session.vars['seller_payoff'] = []
            self.session.vars['buyerL_payoff'] = []
            self.session.vars['buyerH_payoff'] = []
        if self.round_number <= self.session.vars['num_rounds']:
            for p in self.get_groups():
                parameters_data = self.session.vars['parameters'][self.round_number - 1]
                p.line = int(parameters_data['id'])
                p.beta = float(parameters_data['beta'])
                p.cost = float(parameters_data['c'])
                p.thetaL = float(parameters_data['thetaL'])
                p.thetaH = float(parameters_data['thetaH'])
                p.uL = float(parameters_data['uL'])
                p.uH = float(parameters_data['uH'])
                p.type = random.random() < p.beta

    def vars_for_admin_report(self):
        results_table = []
        n_types = 1
        diff_default_options = False
        for i in range(len(self.session.vars['p_offered'])):
            if (self.session.vars['beta'][i] > 0) and (self.session.vars['beta'][i] < 1):
                n_types = 2
                if self.session.vars['uL'][i] != 0 or self.session.vars['uH'][i] != 0:
                    diff_default_options = True
            results_table.append(((self.session.vars['beta'][i],
                                   self.session.vars['c'][i],
                                   self.session.vars['thetaL'][i],
                                   self.session.vars['thetaH'][i],
                                   self.session.vars['uL'][i],
                                   self.session.vars['uH'][i],
                                   self.session.vars['p_offered'][i],
                                   self.session.vars['q_offered'][i],
                                   self.session.vars['n_offered'][i],
                                   self.session.vars['n_accepted'][i],
                                   self.session.vars['seller_payoff'][i],
                                   self.session.vars['buyerL_payoff'][i],
                                   self.session.vars['buyerH_payoff'][i])))
        return {'results_table': results_table, 'n_types': n_types,
                'diff_default_options': diff_default_options}


def products_list(p_list, q_list, accepted_list, p, q, accepted):
    found = False
    for i in range(len(p_list)):
        if p_list[i] == p:
            if q_list[i] == q:
                found = True
                if not accepted_list[i]:
                    accepted_list[i] = accepted
    if not found:
        p_list.append(p)
        q_list.append(q)
        accepted_list.append(accepted)
    return {'p_list': p_list, 'q_list': q_list, 'accepted_list': accepted_list}


class Group(BaseGroup):
    line = models.IntegerField()
    beta = models.FloatField()
    cost = models.FloatField()
    thetaL = models.FloatField()
    thetaH = models.FloatField()
    uL = models.FloatField()
    uH = models.FloatField()
    type = models.BooleanField()  # true = Low, false = High
    price_1 = models.FloatField()
    price_2 = models.FloatField()
    price_3 = models.FloatField()
    price_4 = models.FloatField()
    price_5 = models.FloatField()
    quality_1 = models.FloatField(min=0)
    quality_2 = models.FloatField(min=0)
    quality_3 = models.FloatField(min=0)
    quality_4 = models.FloatField(min=0)
    quality_5 = models.FloatField(min=0)
    offer_accepted = models.IntegerField(widget=widgets.RadioSelect,
                                         choices=[
                                             [1, 'Product 1'],
                                             [2, 'Product 2'],
                                             [3, 'Product 3'],
                                             [4, 'Product 4'],
                                             [5, 'Product 5'],
                                             [0, 'Neither']
                                         ],
                                         label='Please choose one of them or neither')

    def include_product(self, price, quality, accepted):
        found = False
        for i in range(len(self.session.vars['p_offered'])):
            if self.session.vars['p_offered'][i] == price and \
                    self.session.vars['q_offered'][i] == quality and \
                    self.session.vars['beta'][i] == self.beta and \
                    self.session.vars['c'][i] == self.cost and \
                    self.session.vars['thetaL'][i] == self.thetaL and \
                    self.session.vars['thetaH'][i] == self.thetaH and \
                    self.session.vars['uL'][i] == self.uL and \
                    self.session.vars['uH'][i] == self.uH:
                found = True
                self.session.vars['n_offered'][i] = self.session.vars['n_offered'][i] + 1
                if accepted:
                    self.session.vars['n_accepted'][i] = self.session.vars['n_accepted'][i] + 1
        if not found:
            self.session.vars['beta'].append(self.beta)
            self.session.vars['c'].append(self.cost)
            self.session.vars['thetaL'].append(self.thetaL)
            self.session.vars['thetaH'].append(self.thetaH)
            self.session.vars['uL'].append(self.uL)
            self.session.vars['uH'].append(self.uH)
            self.session.vars['p_offered'].append(price)
            self.session.vars['q_offered'].append(quality)
            self.session.vars['n_offered'].append(1)
            if accepted:
                self.session.vars['n_accepted'].append(1)
            else:
                self.session.vars['n_accepted'].append(0)
            self.session.vars['seller_payoff'].append(price - self.cost * quality)
            self.session.vars['buyerL_payoff'].append(self.thetaL * math.sqrt(quality) - price)
            self.session.vars['buyerH_payoff'].append(self.thetaH * math.sqrt(quality) - price)

    def set_payoffs(self):
        p1, p2 = self.get_players()

        if self.offer_accepted > 0:
            price = getattr(self, 'price_{}'.format(int(self.offer_accepted)))
            quality = getattr(self, 'quality_{}'.format(int(self.offer_accepted)))
            p1.payoff = price - self.cost * quality
            if self.type:
                theta = self.thetaL
            else:
                theta = self.thetaH
            p2.payoff = theta * math.sqrt(quality) - price
        else:
            p1.payoff = 0
            if self.type:
                p2.payoff = self.uL
            else:
                p2.payoff = self.uH

        if self.offer_accepted == 1:
            prod_list = products_list([], [], [], self.price_1, self.quality_1, True)
        else:
            prod_list = products_list([], [], [], self.price_1, self.quality_1, False)
        if self.offer_accepted == 2:
            prod_list = products_list(prod_list['p_list'], prod_list['q_list'],
                                      prod_list['accepted_list'], self.price_2, self.quality_2, True)
        else:
            prod_list = products_list(prod_list['p_list'], prod_list['q_list'],
                                      prod_list['accepted_list'], self.price_2, self.quality_2, False)
        if self.offer_accepted == 3:
            prod_list = products_list(prod_list['p_list'], prod_list['q_list'],
                                      prod_list['accepted_list'], self.price_3, self.quality_3, True)
        else:
            prod_list = products_list(prod_list['p_list'], prod_list['q_list'],
                                      prod_list['accepted_list'], self.price_3, self.quality_3, False)
        if self.offer_accepted == 4:
            prod_list = products_list(prod_list['p_list'], prod_list['q_list'],
                                      prod_list['accepted_list'], self.price_4, self.quality_4, True)
        else:
            prod_list = products_list(prod_list['p_list'], prod_list['q_list'],
                                      prod_list['accepted_list'], self.price_4, self.quality_4, False)
        if self.offer_accepted == 5:
            prod_list = products_list(prod_list['p_list'], prod_list['q_list'],
                                      prod_list['accepted_list'], self.price_5, self.quality_5, True)
        else:
            prod_list = products_list(prod_list['p_list'], prod_list['q_list'],
                                      prod_list['accepted_list'], self.price_5, self.quality_5, False)
        for i in range(len(prod_list['p_list'])):
            self.include_product(prod_list['p_list'][i], prod_list['q_list'][i], prod_list['accepted_list'][i])


class Player(BasePlayer):
    pass
