from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Tatiana Mayskaya'

doc = """
Endogenous Choice Between ultimatum and Dictator Games: Experimental Evidence
Survey. Trust Game
"""


def add_currency(currency_used, num):
    if currency_used == 0:
        return '$' + str(num)
    elif currency_used == 1:
        return '£' + str(num)
    else:
        if num % 10 == 1:
            return str(num) + ' рубль'
        elif (num % 10 == 2) | (num % 10 == 3) | (num % 10 == 4):
            return str(num) + ' рубля'
        else:
            return str(num) + ' рублей'


def add_tokens(language, num):
    if language == 1:
        if num != 1:
            return str(num) + ' tokens'
        else:
            return str(num) + ' token'
    else:
        if num % 10 == 1:
            return str(num) + ' жетон'
        elif (num % 10 == 2) | (num % 10 == 3) | (num % 10 == 4):
            return str(num) + ' жетона'
        else:
            return str(num) + ' жетонов'


class Constants(BaseConstants):
    name_in_url = 'GameNov18_survey_trust'
    players_per_group = 2

    endowment = 100
    multiplier = [2, 2, 3, 3, 2, 3, 3, 2]

    num_rounds = len(multiplier)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=False)


class Group(BaseGroup):
    sent_amount = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""Amount sent by P1""",
    )

    sent_back_amount = models.IntegerField(
        doc="""Amount sent back by P2""",
        min=0,
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff_trust = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff_trust = self.sent_amount * Constants.multiplier[self.round_number - 1] - self.sent_back_amount
        p1.payoff_trust_text = add_tokens(self.session.config['language'], p1.payoff_trust)
        p2.payoff_trust_text = add_tokens(self.session.config['language'], p2.payoff_trust)


class Player(BasePlayer):
    payoff_trust = models.IntegerField()
    payment_question = models.IntegerField()
    payoff_trust_text = models.StringField()
    payoff_text = models.StringField()

    def set_final_payoff(self):
        self.participant.vars['payoffs_trust'] = [p.payoff_trust for p in self.in_all_rounds()]
        self.payment_question = random.randint(1, len(self.participant.vars['payoffs_trust']))
        self.payoff = int(self.participant.vars['payoffs_trust'][self.payment_question - 1])
        self.payoff_text = add_tokens(self.session.config['language'], int(self.payoff))
        self.participant.vars['payment_formula'] = self.participant.vars['payment_formula'] + \
            ' + ' + str(int(self.payoff)) + '*' + \
            add_currency(self.session.config['currency_used'], self.session.vars['rate_survey'])
        self.payoff = self.payoff * self.session.vars['rate_survey']

    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]
