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
Moral hazard game with Two Tasks 
"""


class Constants(BaseConstants):
    name_in_url = 'CT19_Multitasking'
    players_per_group = 2

    num_rounds = 30  # maximum number of rounds allowed

    principal_outside_option = 0
    agent_outside_option = 0


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=False)
        if self.round_number == 1:
            self.session.config['real_world_currency_per_point'] = 0.01
            with open(self.session.config['file']) as parameters_file:
                self.session.vars['parameters'] = list(csv.DictReader(parameters_file))
            self.session.vars['num_rounds'] = len(self.session.vars['parameters'])
            self.session.vars['sigma1'] = []
            self.session.vars['sigma2'] = []
            self.session.vars['rho'] = []
            self.session.vars['kappa'] = []
            self.session.vars['eta'] = []
            self.session.vars['gamma'] = []
            self.session.vars['k'] = []
            self.session.vars['alpha1'] = []
            self.session.vars['alpha2'] = []
            self.session.vars['beta'] = []
            self.session.vars['n_offered'] = []
            self.session.vars['n_accepted'] = []
            self.session.vars['opt_effort1'] = []
            self.session.vars['opt_effort2'] = []
            self.session.vars['principal_payoff'] = []
        if self.round_number <= self.session.vars['num_rounds']:
            for p in self.get_groups():
                parameters_data = self.session.vars['parameters'][self.round_number - 1]
                p.line = int(parameters_data['id'])
                p.sigma1 = float(parameters_data['sigma1'])
                p.sigma2 = float(parameters_data['sigma2'])
                p.rho = float(parameters_data['rho'])
                p.kappa = float(parameters_data['kappa'])
                p.eta = float(parameters_data['eta'])
                p.gamma = float(parameters_data['gamma'])
                p.k = float(parameters_data['k'])

    def vars_for_admin_report(self):
        results_table = []
        for i in range(len(self.session.vars['sigma1'])):
            results_table.append(((self.session.vars['sigma1'][i],
                                   self.session.vars['sigma2'][i],
                                   self.session.vars['rho'][i],
                                   self.session.vars['kappa'][i],
                                   self.session.vars['eta'][i],
                                   self.session.vars['gamma'][i],
                                   self.session.vars['k'][i],
                                   self.session.vars['alpha1'][i],
                                   self.session.vars['alpha2'][i],
                                   self.session.vars['beta'][i],
                                   self.session.vars['n_offered'][i],
                                   self.session.vars['n_accepted'][i],
                                   self.session.vars['opt_effort1'][i],
                                   self.session.vars['opt_effort2'][i],
                                   self.session.vars['principal_payoff'][i])))
        return {'results_table': results_table}


def principal_payoff(q1, q2, alpha1, alpha2, beta, kappa):
    return kappa * (q1 + q2) - (alpha1 * q1 + alpha2 * q2 + beta)


def agent_payoff(q1, q2, e1, e2, alpha1, alpha2, beta, eta, gamma, k):
    w = alpha1 * q1 + alpha2 * q2 + beta
    cost = e1 * e1 / 2 + e2 * e2 / 2 + k * e1 * e2
    arg = - gamma * (w - cost)
    if arg > 10:
        arg = 10
    return eta * (1 - math.exp(arg)) / gamma


def opt_effort(alpha1, alpha2, k):
    if alpha1 >= k * alpha2 and alpha2 >= k * alpha1:
        e1 = (alpha1 - k * alpha2) / (1 - k * k)
        e2 = (alpha2 - k * alpha1) / (1 - k * k)
    elif alpha1 > alpha2 and alpha1 > 0:
        e1 = alpha1
        e2 = 0
    elif alpha2 > alpha1 and alpha2 > 0:
        e1 = 0
        e2 = alpha2
    else:
        e1 = 0
        e2 = 0
    return {'e1': e1, 'e2': e2}


def expected_agent_payoff(alpha1, alpha2, beta, e1, e2, eta, gamma, k, sigma1, sigma2, rho):
    cost = e1 * e1 / 2 + e2 * e2 / 2 + k * e1 * e2
    payoff = alpha1 * e1 + alpha2 * e2 + beta - cost - gamma / 2 * (alpha1 * alpha1 * sigma1 * sigma1 +
                                                                    2 * rho * alpha1 * alpha1 * sigma1 * sigma2 +
                                                                    alpha2 * alpha2 * sigma2 * sigma2)
    return eta / gamma * (1 - math.exp(- gamma * payoff))


class Group(BaseGroup):
    line = models.IntegerField()
    sigma1 = models.FloatField(min=0)
    sigma2 = models.FloatField(min=0)
    rho = models.FloatField(min=-1, max=1)
    kappa = models.FloatField(min=0)
    eta = models.FloatField(min=0)
    gamma = models.FloatField(min=0)
    k = models.FloatField(min=-1, max=1)
    alpha1 = models.FloatField(label='Performance-related component for task 1, alpha1:')
    alpha2 = models.FloatField(label='Performance-related component for task 2, alpha2:')
    beta = models.FloatField(label='Fixed compensation level, beta:')
    offer_accepted = models.BooleanField(choices=[[True, 'Accept'], [False, 'Reject']],
                                         widget=widgets.RadioSelectHorizontal,
                                         label='Will you accept the contract or reject it?')
    effort1 = models.FloatField(min=0, label='Please select the effort level for task 1, e1:')
    effort2 = models.FloatField(min=0, label='Please select the effort level for task 2, e2:')
    q1 = models.FloatField(initial=0)
    q2 = models.FloatField(initial=0)

    def include_entry(self):
        found = False
        for i in range(len(self.session.vars['gamma'])):
            if self.session.vars['sigma1'][i] == self.sigma1 and \
                    self.session.vars['sigma2'][i] == self.sigma2 and \
                    self.session.vars['rho'][i] == self.rho and \
                    self.session.vars['kappa'][i] == self.kappa and \
                    self.session.vars['eta'][i] == self.eta and \
                    self.session.vars['gamma'][i] == self.gamma and \
                    self.session.vars['k'][i] == self.k and \
                    self.session.vars['alpha1'][i] == self.alpha1 and \
                    self.session.vars['alpha2'][i] == self.alpha2 and \
                    self.session.vars['beta'][i] == self.beta:
                found = True
                self.session.vars['n_offered'][i] = self.session.vars['n_offered'][i] + 1
                if self.offer_accepted:
                    self.session.vars['n_accepted'][i] = self.session.vars['n_accepted'][i] + 1
        if not found:
            self.session.vars['sigma1'].append(self.sigma1)
            self.session.vars['sigma2'].append(self.sigma2)
            self.session.vars['rho'].append(self.rho)
            self.session.vars['kappa'].append(self.kappa)
            self.session.vars['eta'].append(self.eta)
            self.session.vars['gamma'].append(self.gamma)
            self.session.vars['k'].append(self.k)
            self.session.vars['alpha1'].append(self.alpha1)
            self.session.vars['alpha2'].append(self.alpha2)
            self.session.vars['beta'].append(self.beta)
            self.session.vars['n_offered'].append(1)
            if self.offer_accepted:
                self.session.vars['n_accepted'].append(1)
            else:
                self.session.vars['n_accepted'].append(0)
            effort = opt_effort(self.alpha1, self.alpha2, self.k)
            self.session.vars['opt_effort1'].append(effort['e1'])
            self.session.vars['opt_effort2'].append(effort['e2'])
            if expected_agent_payoff(self.alpha1, self.alpha2, self.beta, effort['e1'], effort['e2'], self.eta,
                                     self.gamma, self.k, self.sigma1, self.sigma2, self.rho) >= 0:
                pi = principal_payoff(effort['e1'], effort['e2'], self.alpha1, self.alpha2, self.beta, self.kappa)
            else:
                pi = Constants.principal_outside_option
            self.session.vars['principal_payoff'].append(pi)

    def set_payoffs(self):
        p1, p2 = self.get_players()

        if self.offer_accepted:
            xi1 = random.gauss(0, 1)
            xi2 = random.gauss(0, 1)
            eps1 = math.sqrt(1 - self.rho * self.rho) * self.sigma1 * xi1 + self.rho * self.sigma1 * xi2
            eps2 = self.sigma2 * xi2
            self.q1 = self.effort1 + eps1
            self.q2 = self.effort2 + eps2
            p1.payoff = \
                principal_payoff(self.q1, self.q2, self.alpha1, self.alpha2, self.beta, self.kappa) \
                / self.session.config['real_world_currency_per_point']
            p2.payoff = \
                agent_payoff(self.q1, self.q2, self.effort1, self.effort2, self.alpha1, self.alpha2, self.beta,
                             self.eta, self.gamma, self.k) \
                / self.session.config['real_world_currency_per_point']
        else:
            p1.payoff = Constants.principal_outside_option / self.session.config['real_world_currency_per_point']
            p2.payoff = Constants.agent_outside_option / self.session.config['real_world_currency_per_point']

        self.include_entry()


class Player(BasePlayer):
    pass
