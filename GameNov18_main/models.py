from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Tatiana Mayskaya'

doc = """
Endogenous Choice Between ultimatum and Dictator Games: Experimental Evidence
main part
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
    name_in_url = 'GameNov18_main'
    players_per_group = 2
    num_rounds = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):

    amount_offered = models.IntegerField(min=0)
    amount_offered_1 = models.IntegerField(min=0)
    amount_offered_2 = models.IntegerField(min=0)
    response = models.IntegerField(min=0)
    game_played = models.IntegerField(widget=widgets.RadioSelectHorizontal)

    def set_payoffs(self):
        p1, p2 = self.get_players()

        if self.round_number == 1:
            p1.participant.vars['amount_offered_G1'] = self.amount_offered
            p1.participant.vars['offer_accepted_G1'] = self.response <= self.amount_offered
            p2.participant.vars['amount_offered_G1'] = p1.participant.vars['amount_offered_G1']
            p2.participant.vars['offer_accepted_G1'] = p1.participant.vars['offer_accepted_G1']
            if p1.participant.vars['offer_accepted_G1']:
                p1.participant.vars['payoff_G1'] = self.session.vars['endowment'] - self.amount_offered
                p2.participant.vars['payoff_G1'] = self.amount_offered
            else:
                p1.participant.vars['payoff_G1'] = self.session.vars['payoff_if_rejected']
                p2.participant.vars['payoff_G1'] = self.session.vars['payoff_if_rejected']
        elif self.round_number == 2:
            p1.participant.vars['amount_offered_G2'] = self.amount_offered
            p2.participant.vars['amount_offered_G2'] = self.amount_offered
            p1.participant.vars['payoff_G2'] = self.session.vars['endowment'] - self.amount_offered
            p2.participant.vars['payoff_G2'] = self.amount_offered
        else:
            p1.game_chosen = self.game_played
            p2.game_chosen = self.game_played
            p1.amount_offered_G3_G1 = self.amount_offered_1
            p1.amount_offered_G3_G2 = self.amount_offered_2
            p2.amount_offered_G3_G1 = self.amount_offered_1
            p2.amount_offered_G3_G2 = self.amount_offered_2
            if self.game_played == 1:
                p1.offer_accepted_G3_G1 = self.response <= self.amount_offered_1
                p2.offer_accepted_G3_G1 = p1.offer_accepted_G3_G1
                if p1.offer_accepted_G3_G1:
                    p1.payoff_G3 = self.session.vars['endowment'] - self.amount_offered_1
                    p2.payoff_G3 = self.amount_offered_1
                else:
                    p1.payoff_G3 = self.session.vars['payoff_if_rejected']
                    p2.payoff_G3 = self.session.vars['payoff_if_rejected']
            else:
                p1.payoff_G3 = self.session.vars['endowment'] - self.amount_offered_2
                p2.payoff_G3 = self.amount_offered_2
            for p in self.get_players():
                p.amount_offered_G1 = p.participant.vars['amount_offered_G1']
                p.offer_accepted_G1 = p.participant.vars['offer_accepted_G1']
                p.amount_offered_G2 = p.participant.vars['amount_offered_G2']
                p.payoff_G1 = p.participant.vars['payoff_G1']
                p.payoff_G2 = p.participant.vars['payoff_G2']
                p.set_final_payoff()


class Player(BasePlayer):
    amount_offered_G1 = models.IntegerField()
    amount_offered_G2 = models.IntegerField()
    amount_offered_G3_G1 = models.IntegerField()
    amount_offered_G3_G2 = models.IntegerField()
    offer_accepted_G1 = models.BooleanField()
    offer_accepted_G3_G1 = models.BooleanField()
    game_chosen = models.IntegerField()
    payoff_G1 = models.IntegerField()
    payoff_G2 = models.IntegerField()
    payoff_G3 = models.IntegerField()
    payoff_game = models.IntegerField()
    payoff_tokens = models.IntegerField()
    payoff_text = models.StringField()

    def set_final_payoff(self):
        self.payoff_game = random.choice([1, 2, 3])
        if self.payoff_game == 1:
            self.payoff_tokens = self.payoff_G1
        elif self.payoff_game == 2:
            self.payoff_tokens = self.payoff_G2
        else:
            self.payoff_tokens = self.payoff_G3
        self.payoff = self.session.vars['show_up'] + self.payoff_tokens * self.session.vars['rate']
        self.payoff_text = add_currency(self.session.config['currency_used'], int(self.payoff))
        self.participant.vars['payment_formula'] = \
            add_currency(self.session.config['currency_used'], self.session.vars['show_up']) + \
            ' + ' + str(self.payoff_tokens) + '*' + \
            add_currency(self.session.config['currency_used'], self.session.vars['rate'])
