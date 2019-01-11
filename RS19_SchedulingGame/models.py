from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import csv
import random

author = 'Tatiana Mayskaya'

doc = """
Research Seminar Scheduling Game year 2019
"""


class Constants(BaseConstants):
    name_in_url = 'RS19_SchedulingGame'
    players_per_group = None

    with open('RS19_SchedulingGame/data.csv') as data_file:
        data = list(csv.DictReader(data_file))
    num_rounds = len(data)+1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['game_completed'] = False
            self.session.vars['order'] = []
            self.session.vars['date'] = []
            self.session.vars['assigned'] = []
            self.session.vars['name'] = []
            for i in range(len(Constants.data)):
                data_line = Constants.data[i]
                self.session.vars['order'].append(int(data_line['Order']))
                self.session.vars['date'].append(data_line['Date'])
                self.session.vars['assigned'].append(False)
                self.session.vars['name'].append('-')

    def vars_for_admin_report(self):
        results_table = []
        for i in range(len(Constants.data)):
            results_table.append((self.session.vars['order'][i], self.session.vars['date'][i],
                                  self.session.vars['name'][i]))
            # if self.session.vars['assigned'][i]:
            #     for p in self.get_players():
            #         if p.order == self.session.vars['order'][i]:
            #             results_table.append((self.session.vars['order'][i], self.session.vars['date'][i],
            #                                   p.participant.label))
            # else:
            #     results_table.append((self.session.vars['order'][i],  self.session.vars['date'][i], "-"))
        return {'results_table': results_table}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    order = models.IntegerField(widget=widgets.RadioSelect, label='Please choose your preferred slot')
    in_game = models.BooleanField()
