from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Tatiana Mayskaya'

doc = """
Endogenous Choice Between ultimatum and Dictator Games: Experimental Evidence
Survey. Risk
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
    name_in_url = 'GameNov18_survey_risk'
    players_per_group = None
    num_rounds = 4

    endowment_RiskyProject = [100, 100]
    prob_success_RiskyProject = [50, 35]
    return_RiskyProject = [2, 3]

    LoseBalls_RiskyUrns = [15, 10]
    WinBalls_RiskyUrns = [15, 10]
    WinPayoff_RiskyUrns = [150, 100]
    Step_RiskyUrns = [10, 10]
    Options_RiskyUrns1 = range(0, WinPayoff_RiskyUrns[0] + Step_RiskyUrns[0], Step_RiskyUrns[0])
    Options_RiskyUrns2 = range(0, WinPayoff_RiskyUrns[1] + Step_RiskyUrns[1], Step_RiskyUrns[1])


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.random_questions()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def random_questions(self):
        randomized_questions = random.sample(range(1, Constants.num_rounds + 1, 1), Constants.num_rounds)
        self.participant.vars['questions_order'] = randomized_questions
        if self.session.config['language'] == 1:
            self.participant.vars['question_RiskyProject'] = \
                'Please choose how many tokens you want to invest in the risky project.'
            self.participant.vars['label_RiskyUrns'] = 'Choose one option'
            self.participant.vars['choice1_RiskyUrns'] = 'Urn gamble'
            self.participant.vars['choice2_RiskyUrns'] = '{} tokens'

        else:
            self.participant.vars['question_RiskyProject'] = \
                'Пожалуйста, выберите, сколько жетонов Вы проинвестируете в рискованный проект.'
            self.participant.vars['label_RiskyUrns'] = 'Выберите одну опцию'
            self.participant.vars['choice1_RiskyUrns'] = 'Лотерея'
            self.participant.vars['choice2_RiskyUrns'] = '{} жетонов'

    question_RiskyProject1 = models.IntegerField(
        min=0, max=Constants.endowment_RiskyProject[0])
    RiskyProject1_earned = models.IntegerField()
    RiskyProject1_left = models.IntegerField()
    RiskyProject1_success = models.BooleanField()
    RiskyProject1_payoff = models.IntegerField()

    question_RiskyProject2 = models.IntegerField(
        min=0, max=Constants.endowment_RiskyProject[1])
    RiskyProject2_earned = models.IntegerField()
    RiskyProject2_left = models.IntegerField()
    RiskyProject2_success = models.BooleanField()
    RiskyProject2_payoff = models.IntegerField()

    RiskyUrns1_0 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_10 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_20 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_30 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_40 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_50 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_60 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_70 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_80 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_90 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_100 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_110 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_120 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_130 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_140 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns1_150 = models.IntegerField(widget=widgets.RadioSelectHorizontal)

    RiskyUrns2_0 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_10 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_20 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_30 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_40 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_50 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_60 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_70 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_80 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_90 = models.IntegerField(widget=widgets.RadioSelectHorizontal)
    RiskyUrns2_100 = models.IntegerField(widget=widgets.RadioSelectHorizontal)

    RiskyUrns1_sure = models.StringField()
    RiskyUrns1_choice = models.StringField()
    RiskyUrns1_choice_num = models.IntegerField()
    RiskyUrns1_payoff = models.IntegerField()

    RiskyUrns2_sure = models.StringField()
    RiskyUrns2_choice = models.StringField()
    RiskyUrns2_choice_num = models.IntegerField()
    RiskyUrns2_payoff = models.IntegerField()

    payment_question_in_order_for_subject = models.IntegerField()
    payment_question_in_internal_order = models.IntegerField()
    payoff_text = models.StringField()

    def get_payoff(self):
        num = self.participant.vars['questions_order'][self.round_number - 1]
        if num == 1 or num == 2:
            if num == 1:
                invested = self.question_RiskyProject1
            else:
                invested = self.question_RiskyProject2
            left = Constants.endowment_RiskyProject[num - 1] - invested
            success = random.uniform(0, 100) < Constants.prob_success_RiskyProject[num - 1]
            if success:
                earned = Constants.return_RiskyProject[num - 1] * invested
            else:
                earned = 0
            if num == 1:
                self.RiskyProject1_left = left
                self.RiskyProject1_success = success
                self.RiskyProject1_earned = earned
                self.RiskyProject1_payoff = left + earned
                self.participant.vars['RiskyProject1_payoff']=self.RiskyProject1_payoff
            else:
                self.RiskyProject2_left = left
                self.RiskyProject2_success = success
                self.RiskyProject2_earned = earned
                self.RiskyProject2_payoff = left + earned
                self.participant.vars['RiskyProject2_payoff'] = self.RiskyProject2_payoff
        else:
            if num == 3:
                sure = random.choice(Constants.Options_RiskyUrns1)
            else:
                sure = random.choice(Constants.Options_RiskyUrns2)
            sure_text = str(self.participant.vars['choice2_RiskyUrns']).format(sure)
            choice_num = getattr(self, 'RiskyUrns{}_{}'.format(num - 2, sure))
            if choice_num == 1:
                choice = self.participant.vars['choice1_RiskyUrns']
                ball = random.randint(1, Constants.LoseBalls_RiskyUrns[num - 3] + Constants.WinBalls_RiskyUrns[num - 3])
                if ball > Constants.LoseBalls_RiskyUrns[num - 3]:
                    pay_off = Constants.WinPayoff_RiskyUrns[num - 3]
                else:
                    pay_off = 0
            else:
                choice = sure_text
                pay_off = sure
            if num == 3:
                self.RiskyUrns1_sure = sure_text
                self.RiskyUrns1_choice_num = choice_num
                self.RiskyUrns1_choice = choice
                self.RiskyUrns1_payoff = pay_off
                self.participant.vars['RiskyUrns1_payoff'] = self.RiskyUrns1_payoff
            else:
                self.RiskyUrns2_sure = sure_text
                self.RiskyUrns2_choice_num = choice_num
                self.RiskyUrns2_choice = choice
                self.RiskyUrns2_payoff = pay_off
                self.participant.vars['RiskyUrns2_payoff'] = self.RiskyUrns2_payoff
        if self.round_number == Constants.num_rounds:
            self.payment_question_in_order_for_subject = random.choice(range(1, Constants.num_rounds + 1, 1))
            self.payment_question_in_internal_order = \
                self.participant.vars['questions_order'][self.payment_question_in_order_for_subject - 1]
            if self.payment_question_in_internal_order == 1:
                payoff_tokens = self.participant.vars['RiskyProject1_payoff']
            elif self.payment_question_in_internal_order == 2:
                payoff_tokens = self.participant.vars['RiskyProject2_payoff']
            elif self.payment_question_in_internal_order == 3:
                payoff_tokens = self.participant.vars['RiskyUrns1_payoff']
            else:
                payoff_tokens = self.participant.vars['RiskyUrns2_payoff']
            self.payoff = payoff_tokens
            self.payoff_text = add_tokens(self.session.config['language'], int(self.payoff))
            self.participant.vars['payment_formula'] = self.participant.vars['payment_formula'] + \
                ' + ' + str(payoff_tokens) + '*' + \
                add_currency(self.session.config['currency_used'], self.session.vars['rate_survey'])
            self.payoff = self.payoff * self.session.vars['rate_survey']
