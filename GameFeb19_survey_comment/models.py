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
Survey. Comments (not obligatory questions in text format)
"""


class Constants(BaseConstants):
    name_in_url = 'GameFeb19_survey_comment'
    players_per_group = None

    # this is done only to count the number of questions
    # (assuming Russian and English versions have the same number)
    with open('GameFeb19_survey_comment/survey_comment_en.csv') as questions_file:
        questions = list(csv.DictReader(questions_file))

    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        assert self.session.config['language'] in translated_languages, TRNSL_ERR_MSG
        if self.round_number == 1:
            if self.session.config['language'] == 'en':
                with open('GameFeb19_survey_comment/survey_comment_en.csv') as questions_file:
                    self.session.vars['survey_comment_list'] = list(csv.DictReader(questions_file))
            else:
                with open('GameFeb19_survey_comment/survey_comment_ru.csv', encoding='utf-8') as questions_file:
                    self.session.vars['survey_comment_list'] = list(csv.DictReader(questions_file))
            for p in self.get_players():
                p.random_questions()
        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']

    def vars_for_admin_report(self):
        players = []
        for p in self.get_players():
            players.append((p.participant.label, p.question, p.submitted_answer))
        return {'players': players}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def random_questions(self):
        randomized_questions = random.sample(range(1, Constants.num_rounds + 1, 1), Constants.num_rounds)
        self.participant.vars['questions_order'] = randomized_questions

    question_id = models.IntegerField()
    question = models.StringField()
    submitted_answer = models.LongStringField(blank=True)

    def current_question(self):
        num = self.participant.vars['questions_order'][self.round_number - 1]
        return self.session.vars['survey_comment_list'][num - 1]
