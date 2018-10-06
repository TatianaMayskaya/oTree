from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1
    timeout_seconds = 600


class RoleInGame(Page):
    def is_displayed(self):
        return self.round_number == 1
    timeout_seconds = 600


class ResponderChoice(Page):
    form_model = 'group'
    form_fields = ['informed_dictator', 'uninformed_dictator']

    def is_displayed(self):
        return self.player.id_in_group == 2
    timeout_seconds = 600


class Wait(WaitPage):
    pass


class ComputerChoice(Page):
    timeout_seconds = 600


class Offer(Page):
    form_model = 'group'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1
    timeout_seconds = 600


class AcceptStrategy(Page):
    form_model = 'group'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        gm = self.group.game()
        print(gm)
        return self.player.id_in_group == 2 and gm == "RESPOND"


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Introduction,
    RoleInGame,
    ResponderChoice,
    Wait,
    ComputerChoice,
    Offer,
    AcceptStrategy,
    ResultsWaitPage,
    Results
]
