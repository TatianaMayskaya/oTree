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
    name_in_url = 'GameFeb19_questions_choice'
    players_per_group = None

    # this is done only to count the number of questions in the quiz
    # (assuming Russian and English versions have the same number)
    with open('GameFeb19_questions_choice/choice_en.csv') as file:
        questions = list(csv.DictReader(file))

    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        assert self.session.config['language'] in translated_languages, TRNSL_ERR_MSG
        if self.round_number == 1:
            if self.session.config['language'] == 'en':
                with open('GameFeb19_questions_choice/choice_en.csv') as choice_file:
                    self.session.vars['choice_file_list'] = list(csv.DictReader(choice_file))
            else:
                with open('GameFeb19_questions_choice/choice_ru.csv', encoding='utf-8') as choice_file:
                    self.session.vars['choice_file_list'] = list(csv.DictReader(choice_file))
            for p in self.get_players():
                p.random_questions()
            self.session.vars['num_questions_Q'] = Constants.num_rounds
        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']
            p.participant.vars['questions_Q'] = []
            p.participant.vars['sum_points'] = []

    def vars_for_admin_report(self):
        players = []
        for p in self.get_players():
            players.append((p.participant.label, p.question, p.submitted_answer_text))
        return {'players': players}


class Group(BaseGroup):
    pass


def generate_payoff0(n, p, a_max, b_max, a_min, b_min):
    u = random.random()
    if u < p:
        return a_max * n + b_max
    else:
        return a_min * n + b_min


def generate_payoff1(pi, max_i, min_i):
    u = random.random()
    if u < pi:
        return max_i
    else:
        return min_i


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    submitted_answer = models.IntegerField()
    submitted_answer_options = models.IntegerField(widget=widgets.RadioSelect)
    submitted_answer_text = models.StringField()
    payment_round = models.BooleanField(initial=False, choices=[[True, _('Yes')], [False, _('No')]])

    def random_questions(self):
        randomized_questions = random.sample(range(1, Constants.num_rounds + 1, 1), Constants.num_rounds)
        self.participant.vars['questions_order_Q'] = randomized_questions

    def current_question(self):
        num = self.participant.vars['questions_order_Q'][self.round_number - 1]
        return self.session.vars['choice_file_list'][num - 1]

    def submission(self):
        if self.round_number == 1:
            self.participant.vars['payment_rounds_Q'] = random.sample(range(1, Constants.num_rounds + 1),
                                                                      self.session.config['n_questions'])
        if self.round_number in self.participant.vars['payment_rounds']:
            self.payment_round = True
        question_data = self.current_question()
        if int(question_data['n_choices']) > 0:
            self.submitted_answer = self.submitted_answer_options
        if int(question_data['n_choices']) == 0:
            self.submitted_answer_text = str(self.submitted_answer)
            self.payoff = generate_payoff0(int(self.submitted_answer), float(question_data['p']),
                                           float(question_data['a_max']), float(question_data['b_max']),
                                           float(question_data['a_min']), float(question_data['b_min']))
        else:
            self.submitted_answer_text = question_data['choice{}'.format(self.submitted_answer)]
            pi = float(question_data['p{}'.format(self.submitted_answer)])
            max_i = float(question_data['max_{}'.format(self.submitted_answer)])
            min_i = float(question_data['min_{}'.format(self.submitted_answer)])
            self.payoff = generate_payoff1(pi, max_i, min_i)
        self.participant.vars['questions_Q'].append(
            (self.round_number, self.question, self.submitted_answer_text,
             add_tokens(self.session.config['language'], int(self.payoff)), self.payment_round))
        if self.payment_round:
            if self.participant.vars['sum_points']:
                self.participant.vars['sum_points'] = self.participant.vars['sum_points'] + ' + '
            self.participant.vars['sum_points'] = self.participant.vars['sum_points'] + str(int(self.payoff))
            self.payoff = self.payoff * self.session.config['rate_Q']
        else:
            self.payoff = 0

    def set_payoffs(self):
        self.participant.vars['payment_formula'] = \
            self.participant.vars['payment_formula'] + \
            ' + (' + self.participant.vars['sum_points'] + ')*' + \
            add_currency(self.session.config['currency_used'],
                         self.session.vars['rate_Q'] * self.session.config['real_world_currency_per_point'])
