from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Your name here'

doc = """
Combination of Ultimatum and Dictator games. At first, the responder chooses 
which game to play (Ultimatum or Dictator). The proposer is informed about 
the responder's choice. Then the chosen game is played. 
"""


class Constants(BaseConstants):
    name_in_url = 'my_game'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'my_game/Instructions.html'
    game_choice = 'my_game/GameChoice.html'

    endowment = c(10)
    payoff_if_rejected = c(0)
    offer_increment = c(1)

    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choices_count = len(offer_choices)

    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))

    computer_choices1 = ["INFORMED", "UNINFORMED"]
    computer_choices2 = ["RESPONDER'S CHOICE", "RESPOND", "ACCEPT"]


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)
        # randomize to treatments
        for g in self.get_groups():
            g.computer_choice1 = random.choice(Constants.computer_choices1)
            g.computer_choice2 = random.choice(Constants.computer_choices2)


def make_field(amount):
    return models.BooleanField(
        widget=widgets.RadioSelectHorizontal,
        label='Would you accept an offer of {}?'.format(c(amount)))


class Group(BaseGroup):
    computer_choice1 = models.StringField()
    computer_choice2 = models.StringField()

    informed_dictator = models.StringField(widget=widgets.RadioSelect, label='', choices=("ACCEPT", "RESPOND"))

    uninformed_dictator = models.StringField(widget=widgets.RadioSelect, label='', choices=("ACCEPT", "RESPOND"))

    amount_offered = models.CurrencyField(choices=Constants.offer_choices)

    offer_accepted = models.BooleanField()

    response_0 = make_field(0)
    response_1 = make_field(1)
    response_2 = make_field(2)
    response_3 = make_field(3)
    response_4 = make_field(4)
    response_5 = make_field(5)
    response_6 = make_field(6)
    response_7 = make_field(7)
    response_8 = make_field(8)
    response_9 = make_field(9)
    response_10 = make_field(10)

    def game(self):
        if self.computer_choice2 == "RESPONDER'S CHOICE":
            if self.computer_choice1 == "INFORMED":
                return self.informed_dictator
            else:
                return self.uninformed_dictator
        else:
            return self.computer_choice2

    def set_payoffs(self):
        p1, p2 = self.get_players()
        gm = self.game()

        if gm == "RESPOND":
            self.offer_accepted = getattr(self, 'response_{}'.format(int(self.amount_offered)))
        else:
            self.offer_accepted = True

        if self.offer_accepted:
            p1.payoff = Constants.endowment - self.amount_offered
            p2.payoff = self.amount_offered
        else:
            p1.payoff = Constants.payoff_if_rejected
            p2.payoff = Constants.payoff_if_rejected


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'proposer'
        else:
            return 'responder'
