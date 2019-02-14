from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Principal(Page):
    form_model = 'group'

    def get_form_fields(self):
        if self.session.config['binary']:
            return ['w0', 'w1']
        else:
            return ['t', 's']

    timeout_seconds = 600
    timeout_submission = {'w0': 0, 'w1': 1}

    def before_next_page(self):
        if self.timeout_happened:
            if self.session.config['binary']:
                self.group.w0 = 0
                self.group.w1 = 0
            else:
                self.group.t = 0
                self.group.s = 0

    def vars_for_template(self):
        return {'num_rounds': self.session.vars['num_rounds'],
                'binary': self.session.config['binary'],
                'sigma': self.group.sigma,
                'alpha0': self.group.alpha0,
                'alpha1': self.group.alpha1,
                'gamma': self.group.gamma}

    def is_displayed(self):
        return self.player.id_in_group == 1


class WaitForPrincipal(WaitPage):
    pass


class Agent(Page):
    form_model = 'group'

    def get_form_fields(self):
        if self.group.offer_accepted is None:
            return ['offer_accepted']
        elif self.group.offer_accepted:
            if self.session.config['binary']:
                return ['effort_binary']
            else:
                return ['effort_cont']

    timeout_seconds = 600

    def before_next_page(self):
        if self.timeout_happened:
            if self.group.offer_accepted is None:
                self.group.offer_accepted = False
            else:
                if self.session.config['binary']:
                    self.group.effort_binary = 0
                else:
                    self.group.effort_cont = 0

    def vars_for_template(self):
        return {'num_rounds': self.session.vars['num_rounds'],
                'binary': self.session.config['binary'],
                'sigma': self.group.sigma,
                'alpha0': self.group.alpha0,
                'alpha1': self.group.alpha1,
                'gamma': self.group.gamma,
                'w0': self.group.w0,
                'w1': self.group.w1,
                's': self.group.s,
                't': self.group.t}

    def is_displayed(self):
        displayed = False
        if self.player.id_in_group == 2:
            if self.group.offer_accepted is None:
                displayed = True
            elif self.group.offer_accepted:
                displayed = True
        return displayed


class WaitForAgent(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class WaitForAllGroups(WaitPage):
    wait_for_all_groups = True


class Results(Page):
    def vars_for_template(self):
        if self.session.config['binary']:
            effort = self.group.effort_binary
            q = self.group.q_binary
        else:
            effort = self.group.effort_cont
            q = self.group.q_cont
        return {'num_rounds': self.session.vars['num_rounds'],
                'binary': self.session.config['binary'],
                'sigma': self.group.sigma,
                'alpha0': self.group.alpha0,
                'alpha1': self.group.alpha1,
                'gamma': self.group.gamma,
                'w0': self.group.w0,
                'w1': self.group.w1,
                's': self.group.s,
                't': self.group.t,
                'accept': self.group.offer_accepted,
                'effort': effort,
                'production': q,
                'wage': self.group.w,
                'payoff': int(self.player.payoff)*self.session.config['real_world_currency_per_point'],
                'payoff_total': float(self.participant.payoff_plus_participation_fee())}


page_sequence = [
    Principal,
    WaitForPrincipal,
    Agent, Agent,
    WaitForAgent,
    WaitForAllGroups,
    Results
]
