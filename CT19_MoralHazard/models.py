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
Moral hazard game 
"""


class Constants(BaseConstants):
    name_in_url = 'CT19_MoralHazard'
    players_per_group = 2

    num_rounds = 30  # maximum number of rounds allowed

    principal_outside_option = 0
    agent_outside_option = 0


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=False)
        if self.round_number == 1:
            self.session.vars['binary'] = self.session.config['binary']
            self.session.config['real_world_currency_per_point'] = 0.01
            with open(self.session.config['file']) as parameters_file:
                self.session.vars['parameters'] = list(csv.DictReader(parameters_file))
            self.session.vars['num_rounds'] = len(self.session.vars['parameters'])
            if self.session.config['binary']:
                self.session.vars['alpha0'] = []
                self.session.vars['alpha1'] = []
                self.session.vars['w0'] = []
                self.session.vars['w1'] = []
                self.session.vars['n_high_effort'] = []
                self.session.vars['n_low_effort'] = []
                self.session.vars['agentL_payoff'] = []
                self.session.vars['agentH_payoff'] = []
            else:
                self.session.vars['sigma'] = []
                self.session.vars['t'] = []
                self.session.vars['s'] = []
            self.session.vars['gamma'] = []
            self.session.vars['n_offered'] = []
            self.session.vars['n_accepted'] = []
            self.session.vars['opt_effort'] = []
            self.session.vars['principal_payoff'] = []
        if self.round_number <= self.session.vars['num_rounds']:
            for p in self.get_groups():
                parameters_data = self.session.vars['parameters'][self.round_number - 1]
                p.line = int(parameters_data['id'])
                if self.session.config['binary']:
                    p.alpha0 = float(parameters_data['alpha0'])
                    p.alpha1 = float(parameters_data['alpha1'])
                else:
                    p.sigma = float(parameters_data['sigma'])
                p.gamma = float(parameters_data['gamma'])

    def vars_for_admin_report(self):
        results_table = []
        if self.session.config['binary']:
            for i in range(len(self.session.vars['alpha0'])):
                results_table.append(((self.session.vars['alpha0'][i],
                                       self.session.vars['alpha1'][i],
                                       self.session.vars['gamma'][i],
                                       self.session.vars['w0'][i],
                                       self.session.vars['w1'][i],
                                       self.session.vars['n_offered'][i],
                                       self.session.vars['n_accepted'][i],
                                       self.session.vars['n_high_effort'][i],
                                       self.session.vars['n_low_effort'][i],
                                       self.session.vars['opt_effort'][i],
                                       self.session.vars['principal_payoff'][i],
                                       self.session.vars['agentL_payoff'][i],
                                       self.session.vars['agentH_payoff'][i])))
        else:
            for i in range(len(self.session.vars['sigma'])):
                results_table.append(((self.session.vars['sigma'][i],
                                       self.session.vars['gamma'][i],
                                       self.session.vars['t'][i],
                                       self.session.vars['s'][i],
                                       self.session.vars['n_offered'][i],
                                       self.session.vars['n_accepted'][i],
                                       self.session.vars['opt_effort'][i],
                                       self.session.vars['principal_payoff'][i])))
        return {'results_table': results_table, 'binary': self.session.config['binary']}


def principal_payoff(q, w):
    return 10 * q - w


def agent_payoff(w, e, gamma):
    return 10 * (1 - math.exp(-gamma * w)) / gamma - e


def opt_cont_effort(t, s, gamma, sigma):
    eta = 10
    if s <= 0:
        return 0
    else:
        e = gamma * s * sigma * sigma / 2 - t / s + 1 / gamma / s * math.log(s * eta)
        if e > 0:
            return e
        else:
            return 0


class Group(BaseGroup):
    line = models.IntegerField()
    alpha0 = models.FloatField(min=0, max=1)
    alpha1 = models.FloatField(min=0, max=1)
    sigma = models.FloatField(min=0)
    gamma = models.FloatField(min=0)
    w0 = models.FloatField(label='w0:')
    w1 = models.FloatField(label='w1:')
    t = models.FloatField(label='Fixed compensation level t:')
    s = models.FloatField(label='Performance-related component s:')
    offer_accepted = models.BooleanField(choices=[[True, 'Accept'], [False, 'Reject']],
                                         widget=widgets.RadioSelectHorizontal,
                                         label='Will you accept the contract or reject it?')
    effort_binary = models.IntegerField(choices=[[1, '1 (high)'], [0, '0 (low)']],
                                        widget=widgets.RadioSelectHorizontal,
                                        label='You accepted the contract. Please select the effort level:')
    effort_cont = models.FloatField(min=0, label='You accepted the contract. Please select the effort level:')
    q_binary = models.IntegerField(choices=[1, 0])
    q_cont = models.FloatField()
    w = models.FloatField()

    def include_entry(self):
        found = False
        if self.session.config['binary']:
            for i in range(len(self.session.vars['gamma'])):
                if self.session.vars['w0'][i] == self.w0 and \
                        self.session.vars['w1'][i] == self.w1 and \
                        self.session.vars['alpha0'][i] == self.alpha0 and \
                        self.session.vars['alpha1'][i] == self.alpha1 and \
                        self.session.vars['gamma'][i] == self.gamma:
                    found = True
                    self.session.vars['n_offered'][i] = self.session.vars['n_offered'][i] + 1
                    if self.offer_accepted:
                        self.session.vars['n_accepted'][i] = self.session.vars['n_accepted'][i] + 1
                        if self.effort_binary == 1:
                            self.session.vars['n_high_effort'][i] = self.session.vars['n_high_effort'][i] + 1
                        if self.effort_binary == 0:
                            self.session.vars['n_low_effort'][i] = self.session.vars['n_low_effort'][i] + 1
            if not found:
                self.session.vars['alpha0'].append(self.alpha0)
                self.session.vars['alpha1'].append(self.alpha1)
                self.session.vars['gamma'].append(self.gamma)
                self.session.vars['w0'].append(self.w0)
                self.session.vars['w1'].append(self.w1)
                self.session.vars['n_offered'].append(1)
                if self.offer_accepted:
                    self.session.vars['n_accepted'].append(1)
                    if self.effort_binary == 1:
                        self.session.vars['n_high_effort'].append(1)
                        self.session.vars['n_low_effort'].append(0)
                    if self.effort_binary == 0:
                        self.session.vars['n_high_effort'].append(0)
                        self.session.vars['n_low_effort'].append(1)
                else:
                    self.session.vars['n_accepted'].append(0)
                    self.session.vars['n_high_effort'].append(0)
                    self.session.vars['n_low_effort'].append(0)
                u0 = self.alpha0 * agent_payoff(self.w1, 0, self.gamma) + \
                     (1 - self.alpha0) * agent_payoff(self.w0, 0, self.gamma)
                u1 = self.alpha1 * agent_payoff(self.w1, 1, self.gamma) + \
                     (1 - self.alpha1) * agent_payoff(self.w0, 1, self.gamma)
                if u0 > u1:
                    self.session.vars['opt_effort'].append(0)
                    pi = self.alpha0 * principal_payoff(1, self.w1) + (1 - self.alpha0) * principal_payoff(0, self.w0)
                else:
                    self.session.vars['opt_effort'].append(1)
                    pi = self.alpha1 * principal_payoff(1, self.w1) + (1 - self.alpha1) * principal_payoff(0, self.w0)
                self.session.vars['principal_payoff'].append(pi)
                self.session.vars['agentL_payoff'].append(u0)
                self.session.vars['agentH_payoff'].append(u1)
        else:
            for i in range(len(self.session.vars['gamma'])):
                if self.session.vars['t'][i] == self.t and \
                        self.session.vars['s'][i] == self.s and \
                        self.session.vars['sigma'][i] == self.sigma and \
                        self.session.vars['gamma'][i] == self.gamma:
                    found = True
                    self.session.vars['n_offered'][i] = self.session.vars['n_offered'][i] + 1
                    if self.offer_accepted:
                        self.session.vars['n_accepted'][i] = self.session.vars['n_accepted'][i] + 1
            if not found:
                self.session.vars['sigma'].append(self.sigma)
                self.session.vars['gamma'].append(self.gamma)
                self.session.vars['t'].append(self.t)
                self.session.vars['s'].append(self.s)
                self.session.vars['n_offered'].append(1)
                if self.offer_accepted:
                    self.session.vars['n_accepted'].append(1)
                else:
                    self.session.vars['n_accepted'].append(0)
                opt_effort = opt_cont_effort(self.t, self.s, self.gamma, self.sigma)
                self.session.vars['opt_effort'].append(opt_effort)
                pi = principal_payoff(opt_effort, self.t + self.s * opt_effort)
                self.session.vars['principal_payoff'].append(pi)

    def set_payoffs(self):
        p1, p2 = self.get_players()

        if self.offer_accepted:
            if self.session.config['binary']:
                u = random.random()
                self.q_binary = 0
                self.w = self.w0
                if self.effort_binary == 0:
                    if u < self.alpha0:
                        self.q_binary = 1
                        self.w = self.w1
                if self.effort_binary == 1:
                    if u < self.alpha1:
                        self.q_binary = 1
                        self.w = self.w1
                p1.payoff = \
                    principal_payoff(self.q_binary, self.w) \
                    / self.session.config['real_world_currency_per_point']
                p2.payoff = \
                    agent_payoff(self.w, self.effort_binary, self.gamma) \
                    / self.session.config['real_world_currency_per_point']
            else:
                u = random.gauss(0, self.sigma)
                self.q_cont = self.effort_cont + u
                self.w = self.t + self.s * self.q_cont
                p1.payoff = \
                    principal_payoff(self.q_cont, self.w) \
                    / self.session.config['real_world_currency_per_point']
                p2.payoff = \
                    agent_payoff(self.w, self.effort_cont, self.gamma) \
                    / self.session.config['real_world_currency_per_point']

        self.include_entry()


class Player(BasePlayer):
    pass
