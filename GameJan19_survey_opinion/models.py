from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import csv, random

author = 'Tatiana Mayskaya'

doc = """
Survey. Opinion questions.
"""


class Constants(BaseConstants):
    name_in_url = 'GameJan19_survey_opinion'
    players_per_group = None

    # this is done only to count the number of questions
    # (assuming Russian and English versions have the same number)
    with open('GameJan19_intro/survey_opinion_en.csv') as questions_file:
        questions = list(csv.DictReader(questions_file))

    num_rounds = len(questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.random_questions()
        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def random_questions(self):
        randomized_questions = random.sample(range(1, Constants.num_rounds + 1, 1), Constants.num_rounds)
        self.participant.vars['questions_order'] = randomized_questions

    question_id = models.IntegerField()
    question = models.StringField()
    submitted_answer = models.IntegerField(
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal)

    def current_question(self):
        num = self.participant.vars['questions_order'][self.round_number - 1]
        return self.session.vars['survey_opinion_list'][num - 1]
