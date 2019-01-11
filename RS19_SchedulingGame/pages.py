from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class MyPage(Page):
    form_model = 'player'
    form_fields = ['order']

    def order_choices(self):
        choices = []
        for i in range(len(Constants.data)):
            if not self.session.vars['assigned'][i]:
                choices.append([self.session.vars['order'][i],
                                str(self.session.vars['order'][i]) + ', ' + self.session.vars['date'][i]])
        return choices

    def is_displayed(self):
        if self.round_number > 1:
            return self.player.in_round(self.round_number - 1).in_game
        else:
            return True


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        if not self.session.vars['game_completed']:
            self.session.vars['game_completed'] = True
            for p in self.group.get_players():
                if self.round_number > 1:
                    if not p.in_round(self.round_number - 1).in_game:
                        p.order = p.in_round(self.round_number - 1).order
                    else:
                        self.session.vars['game_completed'] = False
                else:
                    self.session.vars['game_completed'] = False
                p.in_game = True
            for i in range(len(Constants.data)):
                students = []
                for p in self.group.get_players():
                    if p.order == self.session.vars['order'][i]:
                        students.append(p)
                if len(students) > 0:
                    p = random.choice(students)
                    p.in_game = False
                    self.session.vars['assigned'][i] = True
                    self.session.vars['name'][i] = p.participant.label
        else:
            for p in self.group.get_players():
                p.in_game = False
                p.order = p.in_round(self.round_number - 1).order


class Results(Page):

    def vars_for_template(self):
        n = 0
        for i in range(len(Constants.data)):
            if self.player.order == self.session.vars['order'][i]:
                n = i
        return {'date': self.session.vars['date'][n]}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
