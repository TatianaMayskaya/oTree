from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Principal(Page):
    form_model = 'group'
    form_fields = ['alpha1', 'alpha2', 'beta']

    timeout_seconds = 600
    timeout_submission = {'alpha1': 0, 'alpha2': 0, 'beta': 0}

    def vars_for_template(self):
        return {'num_rounds': self.session.vars['num_rounds'],
                'sigma1': self.group.sigma1,
                'sigma2': self.group.sigma2,
                'rho': self.group.rho,
                'kappa': self.group.kappa,
                'eta': self.group.eta,
                'gamma': self.group.gamma,
                'k': self.group.k}

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
            return ['effort1', 'effort2']

    timeout_seconds = 600

    def before_next_page(self):
        if self.timeout_happened:
            if self.group.offer_accepted is None:
                self.group.offer_accepted = False
            else:
                self.group.effort1 = 0
                self.group.effort2 = 0

    def vars_for_template(self):
        if self.group.offer_accepted is None:
            accept = False
        else:
            accept = self.group.offer_accepted
        return {'num_rounds': self.session.vars['num_rounds'],
                'sigma1': self.group.sigma1,
                'sigma2': self.group.sigma2,
                'rho': self.group.rho,
                'kappa': self.group.kappa,
                'eta': self.group.eta,
                'gamma': self.group.gamma,
                'k': self.group.k,
                'alpha1': self.group.alpha1,
                'alpha2': self.group.alpha2,
                'beta': self.group.beta,
                'accept': accept}

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
                'sigma1': self.group.sigma1,
                'sigma2': self.group.sigma2,
                'rho': self.group.rho,
                'kappa': self.group.kappa,
                'eta': self.group.eta,
                'gamma': self.group.gamma,
                'k': self.group.k,
                'alpha1': self.group.alpha1,
                'alpha2': self.group.alpha2,
                'beta': self.group.beta,
                'accept': self.group.offer_accepted,
                'effort1': self.group.effort1,
                'effort2': self.group.effort2,
                'production1': self.group.q1,
                'production2': self.group.q2,
                'wage': self.group.alpha1 * self.group.q1 + self.group.alpha2 * self.group.q2 + self.group.beta,
                'payoff': int(self.player.payoff) * self.session.config['real_world_currency_per_point'],
                'payoff_total': float(self.participant.payoff_plus_participation_fee())}


page_sequence = [
    Principal,
    WaitForPrincipal,
    Agent, Agent,
    WaitForAgent,
    WaitForAllGroups,
    Results
]
