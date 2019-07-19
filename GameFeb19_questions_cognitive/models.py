from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.utils.translation import ugettext_lazy as _

from GameFeb19_intro.models import add_currency, add_tokens, TRNSL_ERR_MSG, translated_languages

import csv
import random

author = 'Tatiana Mayskaya'

doc = """
Cognitive Reflection Test & IQ Test & GRE-based Test :: whatever counts as cognitive test
"""


class Constants(BaseConstants):
    name_in_url = 'GameFeb19_questions_cognitive'
    players_per_group = None

    # this is done only to count the number of questions in the quiz
    # (assuming Russian and English versions have the same number)
    with open('GameFeb19_questions_cognitive/cognitive_en.csv') as file:
        questions = list(csv.DictReader(file))

    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        assert self.session.config['language'] in translated_languages, TRNSL_ERR_MSG
        if self.round_number == 1:
            if self.session.config['language'] == 'en':
                with open('GameFeb19_questions_cognitive/cognitive_en.csv', encoding='utf-8-sig') as test_file:
                    self.session.vars['test_file_list'] = list(csv.DictReader(test_file))
            else:
                with open('GameFeb19_questions_cognitive/cognitive_ru.csv', encoding='utf-8-sig') as test_file:
                    self.session.vars['test_file_list'] = list(csv.DictReader(test_file))
            for p in self.get_players():
                p.random_questions()
            self.session.vars['num_questions_CT'] = Constants.num_rounds
        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']
            p.solution = int(question_data['solution'])
            if int(question_data['n_choices']) == 0:
                p.solution_text = question_data['solution']
            else:
                p.solution_text = question_data['choice{}'.format(p.solution)]
            p.participant.vars['questions_CT'] = []

    def vars_for_admin_report(self):
        players = []
        for p in self.get_players():
            players.append((p.participant.label, p.question, p.submitted_answer_text, p.solution_text,
                            p.get_is_correct_display()))
        return {'players': players}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    solution = models.IntegerField()
    solution_text = models.StringField()
    submitted_answer = models.IntegerField()
    submitted_answer_options = models.IntegerField(widget=widgets.RadioSelect)
    submitted_answer_text = models.StringField()
    is_correct = models.BooleanField(initial=False, choices=[[True, _('Yes')], [False, _('No')]])

    def random_questions(self):
        randomized_questions = random.sample(range(1, Constants.num_rounds + 1, 1), Constants.num_rounds)
        self.participant.vars['questions_order_CT'] = randomized_questions

    def current_question(self):
        num = self.participant.vars['questions_order_CT'][self.round_number - 1]
        return self.session.vars['test_file_list'][num - 1]

    def check_correct(self):
        question_data = self.current_question()
        if int(question_data['n_choices']) > 0:
            self.submitted_answer = self.submitted_answer_options
        self.is_correct = (self.submitted_answer == self.solution)
        if int(question_data['n_choices']) == 0:
            self.submitted_answer_text = str(self.submitted_answer)
        else:
            self.submitted_answer_text = question_data['choice{}'.format(self.submitted_answer)]
        self.participant.vars['questions_CT'].append(
            (self.round_number, self.question, self.submitted_answer_text, self.solution_text,
             self.get_is_correct_display()))
        if self.is_correct:
            self.payoff = self.session.vars['rate_CT']

    def set_payoffs(self):
        self.participant.vars['questions_correct_CT'] = sum([int(p.is_correct) for p in self.in_all_rounds()])
        self.participant.vars['payment_formula'] = \
            self.participant.vars['payment_formula'] + \
            ' + ' + str(self.participant.vars['questions_correct_CT']) + '*' + \
            add_currency(self.session.config['currency_used'],
                         self.session.vars['rate_CT'] * self.session.config['real_world_currency_per_point'])
