from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Principal(Page):
    form_model = 'group'
    form_fields = ['w0', 'w1']

    timeout_seconds = 600
    timeout_submission = {'w0': 0, 'w1': 1}

    def vars_for_template(self):
        return {'num_rounds': self.session.vars['num_rounds'],
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
            return ['effort']

    timeout_seconds = 600

    def before_next_page(self):
        if self.timeout_happened:
            if self.group.offer_accepted is None:
                self.group.offer_accepted = False
            else:
                self.group.effort = 0

    def vars_for_template(self):
        return {'num_rounds': self.session.vars['num_rounds'],
                'alpha0': self.group.alpha0,
                'alpha1': self.group.alpha1,
                'gamma': self.group.gamma,
                'w0': self.group.w0,
                'w1': self.group.w1}

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
        return {'num_rounds': self.session.vars['num_rounds'],
                'alpha0': self.group.alpha0,
                'alpha1': self.group.alpha1,
                'gamma': self.group.gamma,
                'w0': self.group.w0,
                'w1': self.group.w1,
                'accept': self.group.offer_accepted,
                'effort': self.group.effort,
                'production': self.group.q,
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
