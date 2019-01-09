from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Seller(Page):
    form_model = 'group'
    form_fields = ['price_1', 'price_2', 'price_3', 'price_4', 'price_5',
                   'quality_1', 'quality_2', 'quality_3', 'quality_4', 'quality_5']

    def vars_for_template(self):
        return {'cost': self.group.cost,
                'beta': self.group.beta,
                'thetaL': self.group.thetaL,
                'thetaH': self.group.thetaH,
                'uL': self.group.uL,
                'uH': self.group.uH
                }

    def is_displayed(self):
        return self.player.id_in_group == 1


class WaitForSeller(WaitPage):
    pass


class Buyer(Page):
    form_model = 'group'
    form_fields = ['offer_accepted']

    def vars_for_template(self):
        if self.group.type:
            type_str = 'LOW'
        else:
            type_str = 'HIGH'
        return {'cost': self.group.cost,
                'beta': self.group.beta,
                'thetaL': self.group.thetaL,
                'thetaH': self.group.thetaH,
                'uL': self.group.uL,
                'uH': self.group.uH,
                'type': type_str,
                'p1': self.group.price_1,
                'q1': self.group.quality_1,
                'p2': self.group.price_2,
                'q2': self.group.quality_2,
                'p3': self.group.price_3,
                'q3': self.group.quality_3,
                'p4': self.group.price_4,
                'q4': self.group.quality_4,
                'p5': self.group.price_5,
                'q5': self.group.quality_5
                }

    def is_displayed(self):
        return self.player.id_in_group == 2


class WaitForBuyer(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        if self.group.type:
            type_str = 'LOW'
        else:
            type_str = 'HIGH'
        return {'cost': self.group.cost,
                'beta': self.group.beta,
                'thetaL': self.group.thetaL,
                'thetaH': self.group.thetaH,
                'uL': self.group.uL,
                'uH': self.group.uH,
                'type': type_str,
                'p1': self.group.price_1,
                'q1': self.group.quality_1,
                'p2': self.group.price_2,
                'q2': self.group.quality_2,
                'p3': self.group.price_3,
                'q3': self.group.quality_3,
                'p4': self.group.price_4,
                'q4': self.group.quality_4,
                'p5': self.group.price_5,
                'q5': self.group.quality_5,
                'product': self.group.offer_accepted,
                'payoff': self.player.payoff,
                'payoff_total': self.participant.payoff
                }


page_sequence = [
    Seller,
    WaitForSeller,
    Buyer,
    WaitForBuyer,
    Results
]
