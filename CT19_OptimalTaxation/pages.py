from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, utility_function


class Government(Page):
    form_model = 'player'
    form_fields = ['income_1', 'income_2', 'tax_1', 'tax_2']

    timeout_seconds = 600
    timeout_submission = {'income_1': 0, 'tax_1': 0, 'income_2': 0, 'tax_2': 0}

    def vars_for_template(self):
        return {'n_high': self.session.vars['n_high'],
                'n_low': self.session.vars['n_low'],
                'thetaH': self.session.config['thetaH'],
                'thetaL': self.session.config['thetaL'],
                'twice_thetaH': self.session.config['thetaH'] * 2}

    def is_displayed(self):
        return self.round_number == 1

    def error_message(self, values):
        if values["income_1"] == values["income_2"]:
            if values["tax_1"] != values["tax_2"]:
                return 'Since q1=q2, please make sure that p(q1)=p(q2)'

    def before_next_page(self):
        self.participant.vars['income_1'] = self.player.income_1
        self.participant.vars['income_2'] = self.player.income_2
        self.participant.vars['tax_1'] = self.player.tax_1
        self.participant.vars['tax_2'] = self.player.tax_2


class GovernmentWaitPage(WaitPage):
    def after_all_players_arrive(self):
        if self.round_number > 1:
            for p in self.group.get_players():
                p.income_1 = p.in_round(1).income_1
                p.income_2 = p.in_round(1).income_2
                p.tax_1 = p.in_round(1).tax_1
                p.tax_2 = p.in_round(1).tax_2
                p.theta = p.in_round(1).theta
        p = self.group.get_player_by_id(self.round_number)
        self.group.income_1 = p.income_1
        self.group.income_2 = p.income_2
        self.group.tax_1 = p.tax_1
        self.group.tax_2 = p.tax_2


class Worker(Page):
    form_model = 'player'
    form_fields = ['income']

    timeout_seconds = 600
    timeout_submission = {'income': 0}

    def vars_for_template(self):
        return {'theta': self.player.theta,
                'q1': self.group.income_1,
                'q2': self.group.income_2,
                'p1': self.group.tax_1,
                'p2': self.group.tax_2,
                'num_rounds': self.session.vars['num_rounds'],
                'twice_thetaH': self.session.config['thetaH'] * 2}


class WorkerWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            if p.income == self.group.income_1:
                p.tax = self.group.tax_1
            elif p.income == self.group.income_2:
                p.tax = self.group.tax_2
            else:
                p.tax = p.income - p.income * p.income / 2 / self.session.config['thetaH']
            p.payoff = utility_function(p.tax, p.income, p.theta) / self.session.vars['num_rounds']
        bankrupt = sum([p.tax for p in self.group.get_players()]) < 0
        government = self.group.get_player_by_id(self.round_number)
        if not bankrupt:
            government.participant.vars['government_payoff'] = sum([p.payoff for p in self.group.get_players()])
        else:
            government.participant.vars['government_payoff'] = sum([p.tax for p in self.group.get_players()])
        government.payoff = government.payoff + government.participant.vars['government_payoff']


class Results(Page):
    def vars_for_template(self):
        payoff_total = sum([p.payoff for p in self.player.in_all_rounds()])
        return {'theta': self.player.theta,
                'q1': self.player.income_1,
                'q2': self.player.income_2,
                'p1': self.player.tax_1,
                'p2': self.player.tax_2,
                'n_high': self.session.vars['n_high'],
                'n_low': self.session.vars['n_low'],
                'thetaH': self.session.config['thetaH'],
                'thetaL': self.session.config['thetaL'],
                'government_payoff': self.participant.vars['government_payoff'],
                'worker_payoff': payoff_total - self.participant.vars['government_payoff'],
                'payoff_total': payoff_total}

    def is_displayed(self):
        return self.round_number == self.session.vars['num_rounds']


page_sequence = [
    Government,
    GovernmentWaitPage,
    Worker,
    WorkerWaitPage,
    Results
]
