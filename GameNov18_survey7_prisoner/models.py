from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Tatiana Mayskaya'

doc = """
Endogenous Choice Between ultimatum and Dictator Games: Experimental Evidence
Survey. Part 7. Prisoner Dilemma
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
    name_in_url = 'GameNov18_survey7_prisoner'
    players_per_group = 2
    num_rounds = 2

    Prisoner_both_cooperate_payoff = [300, 200]  # [95, 80]
    Prisoner_both_defect_payoff = [200, 100]  # [62, 50]
    Prisoner_betrayed_payoff = [100, 0]  # [31, 24]
    Prisoner_betray_payoff = [400, 300]  # [120, 100]
    Prisoner_cooperate = 'A1'
    Prisoner_defect = 'A2'


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Prisoner_decision = models.StringField(
        choices=[Constants.Prisoner_cooperate, Constants.Prisoner_defect],
        widget=widgets.RadioSelect
    )
    Prisoner_payoff = models.IntegerField()
    payment_question = models.IntegerField()
    payoff_text = models.StringField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_prisoner_payoff(self):
        payoff_matrix = {
            Constants.Prisoner_cooperate:
                {
                    Constants.Prisoner_cooperate: Constants.Prisoner_both_cooperate_payoff[self.round_number - 1],
                    Constants.Prisoner_defect: Constants.Prisoner_betrayed_payoff[self.round_number - 1]
                },
            Constants.Prisoner_defect:
                {
                    Constants.Prisoner_cooperate: Constants.Prisoner_betray_payoff[self.round_number - 1],
                    Constants.Prisoner_defect: Constants.Prisoner_both_defect_payoff[self.round_number - 1]
                }
        }
        self.Prisoner_payoff = payoff_matrix[self.Prisoner_decision][self.other_player().Prisoner_decision]
        self.participant.vars['prisoner_payoffs'].append(self.Prisoner_payoff)

    def set_final_prisoner_payoff(self):
        self.payment_question = random.randint(1, len(self.participant.vars['prisoner_payoffs']))
        self.payoff = int(self.participant.vars['prisoner_payoffs'][self.payment_question - 1])
        self.payoff = self.payoff * self.session.vars['rate_survey']
        self.payoff_text = add_currency(self.session.config['currency_used'], int(self.payoff))
