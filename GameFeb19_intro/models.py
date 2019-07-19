from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.utils.translation import ugettext_lazy as _

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
        if num % 100 >= 5 & num % 100 <= 20:
            return str(num) + ' рублей'
        elif num % 10 == 1:
            return str(num) + ' рубль'
        elif (num % 10 == 2) | (num % 10 == 3) | (num % 10 == 4):
            return str(num) + ' рубля'
        else:
            return str(num) + ' рублей'


def add_tokens(language, num):
    if language == 'en':
        if num != 1:
            return str(num) + ' tokens'
        else:
            return str(num) + ' token'
    else:
        if num % 100 >= 5 & num % 100 <= 20:
            return str(num) + ' жетонов'
        elif num % 10 == 1:
            return str(num) + ' жетон'
        elif (num % 10 == 2) | (num % 10 == 3) | (num % 10 == 4):
            return str(num) + ' жетона'
        else:
            return str(num) + ' жетонов'


class Constants(BaseConstants):
    name_in_url = 'GameFeb19_intro'
    players_per_group = None

    # this is done only to count the number of questions in the quiz
    # (assuming Russian and English versions have the same number)
    with open('GameFeb19_intro/quiz_en.csv') as quiz_file:
        questions = list(csv.DictReader(quiz_file))

    # num_rounds = 1
    num_rounds = len(questions)


translated_languages = ['en', 'ru']  # This is the list of allowed languages

TRNSL_ERR_MSG = 'Translation for this language does not exist'


class Subsession(BaseSubsession):
    def creating_session(self):
        assert self.session.config['language'] in translated_languages, TRNSL_ERR_MSG
        self.group_randomly(fixed_id_in_group=True)
        if self.round_number == 1:
            self.session.vars['endowment'] = self.session.config['endowment']
            self.session.vars['payoff_if_rejected'] = self.session.config['payoff_if_rejected']
            # if self.session.config['currency_used'] == 0:
            #     self.session.config['real_world_currency_per_point'] = 0.01
            #     self.session.config['participation_fee'] = 5
            # elif self.session.config['currency_used'] == 1:
            #     self.session.config['real_world_currency_per_point'] = 0.02
            #     self.session.config['participation_fee'] = 3
            # else:
            #     self.session.config['real_world_currency_per_point'] = 1.00
            #     self.session.config['participation_fee'] = 200
            self.session.vars['rate'] = self.session.config['rate']
            self.session.vars['rate_reversed'] = self.session.config['rate_reversed']
            self.session.vars['rate_UG'] = self.session.config['rate_UG']
            self.session.vars['rate_UG_reversed'] = self.session.config['rate_UG_reversed']
            self.session.vars['rate_CT'] = self.session.config['rate_CT']  # rate per one question for cognitive test
            # self.session.vars['rate_Q'] = self.session.config['rate_Q']  # rate per one point for choice questions
            # self.session.vars['n_questions'] = self.session.config['n_questions']  # number of paid questions in choice questions session

            if self.session.config['test_mode']:
                self.session.config['n_rounds'] = self.session.config['min_n_rounds']

            self.session.vars['survey_part'] = 0
            self.session.vars['questions_part'] = 0

            if self.session.config['language'] == 'en':
                with open('GameFeb19_intro/quiz_en.csv') as quiz_file:
                    self.session.vars['quiz_file_list'] = list(csv.DictReader(quiz_file))
            else:
                with open('GameFeb19_intro/quiz_ru.csv', encoding='utf-8') as quiz_file:
                    self.session.vars['quiz_file_list'] = list(csv.DictReader(quiz_file))

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']
            p.solution = int(question_data['solution'])
            p.explanation = question_data['explanation']
            p.solution_text = question_data['solution']

    def vars_for_admin_report(self):
        players = []
        for p in self.get_players():
            players.append((p.participant.label, p.submitted_answer, p.solution, p.is_correct, p.n_try))
        return {'players': players}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    solution = models.IntegerField()
    solution_text = models.StringField()
    submitted_answer_text = models.StringField()
    submitted_answer = models.IntegerField()
    is_correct = models.BooleanField(initial=False, choices=[[True, _('Yes')], [False, _('No')]])
    explanation = models.StringField()
    n_try = models.IntegerField(initial=1)

    def current_question(self):
        return self.session.vars['quiz_file_list'][self.round_number - 1]

    def check_correct(self):
        self.is_correct = (self.submitted_answer == self.solution)
        self.submitted_answer_text = str(self.submitted_answer)
        if not self.is_correct:
            self.n_try = self.n_try + 1
