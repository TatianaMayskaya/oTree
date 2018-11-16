from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import csv


author = 'Tatiana Mayskaya'

doc = """
Endogenous Choice Between ultimatum and Dictator Games: Experimental Evidence
introduction + quiz
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


class Constants(BaseConstants):
    name_in_url = 'GameNov18_intro'
    players_per_group = None

    # this is done only to count the number of questions in the quiz
    # (assuming Russian and English versions have the same number)
    with open('GameNov18_intro/quiz_en.csv') as quiz_file:
        questions = list(csv.DictReader(quiz_file))

    # num_rounds = 1
    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)
        if self.round_number == 1:
            self.session.vars['endowment'] = 100
            self.session.vars['payoff_if_rejected'] = 0
            if self.session.config['currency_used'] == 0:
                self.session.vars['show_up'] = 5
                self.session.vars['rate'] = 0.1  # 0.2
                self.session.vars['rate_survey'] = 0.01  # 0.02
            elif self.session.config['currency_used'] == 1:
                self.session.vars['show_up'] = 3
                self.session.vars['rate'] = 0.2
                self.session.vars['rate_survey'] = 0.02
            else:
                self.session.vars['show_up'] = 200
                self.session.vars['rate'] = 10
                self.session.vars['rate_survey'] = 1
            self.session.vars['rate_survey_text'] = add_currency(self.session.config['currency_used'],
                                                                 self.session.vars['rate_survey'])

            if self.session.config['language'] == 1:
                self.session.vars['wait_page_title'] = 'Please wait'
                self.session.vars['wait_page_body'] = 'Waiting for the other participants'
                self.session.vars['too_little_offered'] = 'You cannot offer less than 0 tokens'
                self.session.vars['too_much_offered'] = 'You cannot offer more than {} tokens'.format(
                    self.session.vars['endowment'])
                self.session.vars['too_little_accepted'] = 'Please choose a non-negative integer'
                self.session.vars['offer0'] = \
                    'You have {} tokens. Choose how many tokens you want to offer to player 2'.format(
                        self.session.vars['endowment'])
                self.session.vars['offer1'] = \
                    'You have {} tokens. Choose how many tokens you want to offer to player 2 ' \
                    'if player 2 chooses game 1'.format(self.session.vars['endowment'])
                self.session.vars['offer2'] = \
                    'You have {} tokens. Choose how many tokens you want to offer to player 2 ' \
                    'if player 2 chooses game 2'.format(self.session.vars['endowment'])
                self.session.vars['response'] = 'Choose the minimum offer that you would accept'
                self.session.vars['game'] = 'Choose which game to play'
                with open('GameNov18_intro/quiz_en.csv') as quiz_file:
                    self.session.vars['quiz_file_list'] = list(csv.DictReader(quiz_file))
                with open('GameNov18_intro/survey1_en.csv') as survey1_file:
                    self.session.vars['survey1_list'] = list(csv.DictReader(survey1_file))
                with open('GameNov18_intro/survey3_en.csv') as survey3_file:
                    self.session.vars['survey3_list'] = list(csv.DictReader(survey3_file))
                with open('GameNov18_intro/survey4_en.csv') as survey4_file:
                    self.session.vars['survey4_list'] = list(csv.DictReader(survey4_file))
            else:
                self.session.vars['wait_page_title'] = 'Пожалуйста, подождите'
                self.session.vars['wait_page_body'] = 'Не все участники ещё закончили игру'
                self.session.vars['too_little_offered'] = 'Вы не можете предложить меньше 0 жетонов'
                self.session.vars['too_much_offered'] = 'Вы не можете предложить больше {} жетонов'.format(
                    self.session.vars['endowment'])
                self.session.vars['too_little_accepted'] = 'Пожалуйста, выберите неотрицательное число'
                self.session.vars['offer0'] = \
                    'Вы получили {} жетонов. Выберите, сколько жетонов Вы хотите предложить игроку 2'.format(
                        self.session.vars['endowment'])
                self.session.vars['offer1'] = \
                    'Вы получили {} жетонов. Выберите, сколько жетонов Вы хотите предложить игроку 2 в случае, ' \
                    'если игрок 2 выберет игру 1'.format(self.session.vars['endowment'])
                self.session.vars['offer2'] = \
                    'Вы получили {} жетонов. Выберите, сколько жетонов Вы хотите предложить игроку 2 в случае, ' \
                    'если игрок 2 выберет игру 2'.format(self.session.vars['endowment'])
                self.session.vars['response'] = 'Выберите минимальное предложение, от которого Вы не откажитесь'
                self.session.vars['game'] = 'Выберите, какую игру дальше играть'
                with open('GameNov18_intro/quiz_ru.csv', encoding='utf-8') as quiz_file:
                    self.session.vars['quiz_file_list'] = list(csv.DictReader(quiz_file))
                with open('GameNov18_intro/survey1_ru.csv', encoding='utf-8') as survey1_file:
                    self.session.vars['survey1_list'] = list(csv.DictReader(survey1_file))
                with open('GameNov18_intro/survey3_ru.csv', encoding='utf-8') as survey3_file:
                    self.session.vars['survey3_list'] = list(csv.DictReader(survey3_file))
                with open('GameNov18_intro/survey4_ru.csv', encoding='utf-8') as survey4_file:
                    self.session.vars['survey4_list'] = list(csv.DictReader(survey4_file))

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']
            p.solution = int(question_data['solution'])
            p.explanation = question_data['explanation']
            if int(question_data['n_choices']) == 0:
                p.solution_text = question_data['solution']
            else:
                p.solution_text = question_data['choice{}'.format(p.solution)]
            p.is_correct_choices()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    solution = models.IntegerField()
    solution_text = models.StringField()
    submitted_answer_text = models.StringField()
    submitted_answer = models.IntegerField()
    is_correct = models.BooleanField(initial=False)
    explanation = models.StringField()

    def current_question(self):
        return self.session.vars['quiz_file_list'][self.round_number - 1]

    def is_correct_choices(self):
        if self.session.config['language'] == 1:
            return [[True, 'Yes'], [False, 'No']]
        else:
            return [[True, 'Да'], [False, 'Нет']]

    def check_correct(self):
        self.is_correct = (self.submitted_answer == self.solution)
        self.is_correct_choices()
        question_data = self.current_question()
        if int(question_data['n_choices']) == 0:
            self.submitted_answer_text = str(self.submitted_answer)
        else:
            self.submitted_answer_text = question_data['choice{}'.format(self.submitted_answer)]
