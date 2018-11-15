from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import csv

author = 'Tatiana Mayskaya'

doc = """
Endogenous Choice Between ultimatum and Dictator Games: Experimental Evidence
Survey. Part 3. Opinion questions.
"""


class Constants(BaseConstants):
    name_in_url = 'GameNov18_survey3_opinion'
    players_per_group = None

    # this is done only to count the number of questions
    # (assuming Russian and English versions have the same number)
    with open('GameNov18_intro/survey3_en.csv') as questions_file:
        questions = list(csv.DictReader(questions_file))

    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    submitted_answer = models.IntegerField(
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal)

    def current_question(self):
        return self.session.vars['survey3_list'][self.round_number - 1]