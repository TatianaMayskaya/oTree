from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import csv

author = 'Tatiana Mayskaya'

doc = """
Base Game: Ultimatum Game with 4 players in a group and endogenous pairing
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
    name_in_url = 'GameJan19_intro'
    players_per_group = None

    # this is done only to count the number of questions in the quiz
    # (assuming Russian and English versions have the same number)
    with open('GameJan19_intro/quiz_en.csv') as quiz_file:
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
                self.session.config['real_world_currency_per_point'] = 0.01
                self.session.config['participation_fee'] = 5
            elif self.session.config['currency_used'] == 1:
                self.session.config['real_world_currency_per_point'] = 0.02
                self.session.config['participation_fee'] = 3
            else:
                self.session.config['real_world_currency_per_point'] = 1.00
                self.session.config['participation_fee'] = 200
            self.session.vars['rate'] = 10
            self.session.vars['rate_reversed'] = 10
            self.session.vars['rate_survey'] = 1

            if self.session.config['language'] == 1:
                self.session.vars['wait_page_title'] = 'Please wait'
                self.session.vars['wait_page_body'] = 'Waiting for the other participants'
                self.session.vars['offer'] = \
                    'You have {} tokens. Choose how many tokens you want to offer to Player 2'.format(
                        self.session.vars['endowment'])
                self.session.vars['response'] = 'Choose the minimum offer that you would accept'
                self.session.vars['player_choice'] = 'Choose your partner'
                with open('GameJan19_intro/quiz_en.csv') as quiz_file:
                    self.session.vars['quiz_file_list'] = list(csv.DictReader(quiz_file))
                with open('GameJan19_intro/survey_opinion_en.csv') as survey_opinion_file:
                    self.session.vars['survey_opinion_list'] = list(csv.DictReader(survey_opinion_file))
                with open('GameJan19_intro/survey_comment_en.csv') as survey_comment_file:
                    self.session.vars['survey_comment_list'] = list(csv.DictReader(survey_comment_file))
            else:
                self.session.vars['wait_page_title'] = 'Пожалуйста, подождите'
                self.session.vars['wait_page_body'] = 'Не все участники ещё закончили игру'
                self.session.vars['offer'] = \
                    'Вы получили {} жетонов. Выберите, сколько жетонов Вы хотите предложить игроку 2'.format(
                        self.session.vars['endowment'])
                self.session.vars['response'] = 'Выберите минимальное предложение, от которого Вы не откажитесь'
                self.session.vars['player_choice'] = 'Выберите своего партнёра'
                with open('GameJan19_intro/quiz_ru.csv', encoding='utf-8') as quiz_file:
                    self.session.vars['quiz_file_list'] = list(csv.DictReader(quiz_file))
                with open('GameJan19_intro/survey_opinion_ru.csv', encoding='utf-8') as survey_opinion_file:
                    self.session.vars['survey_opinion_list'] = list(csv.DictReader(survey_opinion_file))
                with open('GameJan19_intro/survey_comment_ru.csv', encoding='utf-8') as survey_comment_file:
                    self.session.vars['survey_comment_list'] = list(csv.DictReader(survey_comment_file))

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']
            p.solution = int(question_data['solution'])
            p.explanation = question_data['explanation']
            p.solution_text = question_data['solution']
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
    n_try = models.IntegerField(initial=1)

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
        self.submitted_answer_text = str(self.submitted_answer)
        if not self.is_correct:
            self.n_try = self.n_try + 1
