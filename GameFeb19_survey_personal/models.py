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
Survey. Personal questions
"""


class Constants(BaseConstants):
    name_in_url = 'GameFeb19_survey_personal'
    players_per_group = None
    num_rounds = 12


class Subsession(BaseSubsession):
    def creating_session(self):
        assert self.session.config['language'] in translated_languages, TRNSL_ERR_MSG
        if self.round_number == 1:
            for p in self.get_players():
                p.random_questions()

    def vars_for_admin_report(self):
        players = []
        for p in self.get_players():
            num = p.participant.vars['questions'][self.round_number - 1]
            if num == 1:
                question = 'Age'
                submitted_answer = p.age
            elif num == 2:
                question = 'Gender'
                submitted_answer = p.gender
            elif num == 3:
                question = 'Field'
                submitted_answer = p.field
            elif num == 4:
                question = 'Native_language'
                submitted_answer = p.native_language
            elif num == 5:
                question = 'Income level (1-5)'
                submitted_answer = p.income
            elif num == 6:
                question = 'Risk attitude (0-10)'
                submitted_answer = p.riskat
            elif num == 7:
                question = 'Level of happiness now (0-10)'
                submitted_answer = p.happy_now
            elif num == 8:
                question = 'Level of happiness in the future (0-10)'
                submitted_answer = p.happy_future
            elif num == 9:
                question = 'Trust people (0-10)'
                submitted_answer = p.trust
            elif num == 10:
                question = 'Free to control my fate (0-10)'
                submitted_answer = p.freedom
            elif num == 11:
                question = 'Believe in democracy (0-10)'
                submitted_answer = p.democracy
            elif num == 12:
                question = 'Live in a democratic country (0-10)'
                submitted_answer = p.democracy_live
            players.append((p.participant.label, question, submitted_answer))
        return {'players': players}


class Group(BaseGroup):
    pass


def make_question(label_text):
    return models.PositiveIntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
        label=label_text)


class Player(BasePlayer):
    def random_questions(self):
        randomized_questions = random.sample(range(1, Constants.num_rounds + 1, 1), Constants.num_rounds)
        self.participant.vars['questions'] = randomized_questions

    age = models.IntegerField(min=13, max=95, initial=None, label=_('Age'))
    gender = models.IntegerField(initial=None, widget=widgets.RadioSelect(), label=_('Gender'),
                                 choices=[[0, _('Female')], [1, _('Male')], [-1, _('Other')]])
    field = models.PositiveIntegerField(widget=widgets.RadioSelect(), label=_('Field of expertise'),
                                        choices=[[1, _('Economics, finance, management')],
                                                 [2, _('Social sciences, psychology, political science')],
                                                 [3, _('Law')],
                                                 [4, _('International relations')],
                                                 [5, _('Mathematics, physics, computer science')],
                                                 [6, _('Biology, chemistry')],
                                                 [7, _('Humanities')],
                                                 [8, _('Media')],
                                                 [9, _('Other field')]])
    native_language = models.StringField(label=_('What is(are) your native language(s)?'))
    income = models.PositiveIntegerField(widget=widgets.RadioSelect(),
                                         label=_('''
                                         Which statement best describes the financial situation in your family?
                                         '''),
                                         choices=[[1, _('Barely enough to survive.')],
                                                  [2, _('''
                                                  We have enough money for food and other daily essentials but we have 
                                                  no capacity to make savings.
                                                  ''')],
                                                  [3, _('We can afford vacation every year.')],
                                                  [4, _('We can travel abroad every year.')],
                                                  [5, _('We have no financial constraints.')]])
    riskat = make_question(_('''
    How do you see yourself: Are you generally a person who is fully prepared to take risks 
    or do you try to avoid taking risks? Please tick a box on the scale, 
    where the value 0 means: 'Not at all willing to take risks' and 
    the value 10 means: 'Very willing to take risks'.
    '''))
    happy_now = make_question(_('''
    Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. 
    The top of the ladder represents the best possible life for you and the bottom of the ladder 
    represents the worst possible life for you. On which step of the ladder would you say 
    you personally feel you stand at this time?
    '''))
    happy_future = make_question(_('''
    Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. 
    The top of the ladder represents the best possible life for you and the bottom of the ladder 
    represents the worst possible life for you. Just your best guess, on which step fo you think 
    you will stand in the future, say about five years from now?
    '''))
    trust = make_question(_('''
    Do you think you could trust most people or they are generally not trustworthy? Please tick 
    a box on the scale, where the value 0 means: 'I never trust people' and 
    the value 10 means: 'I always trust people'.
    '''))
    freedom = make_question(_('''
    Some people feel like they have complete freedom of choice and control of their lives, 
    whereas others believe their actions have no effect on their fate. What about you? 
    Please tick a box on the scale, where the value 0 means: 'I have no control of my fate' and 
    the value 10 means: 'I have complete control of my life'.
    '''))
    democracy = make_question(_('''
    How important is it for you to live in a country that is governed based on democracy principals, 
    that is, where the citizens exercise power by voting? 
    Please tick a box on the scale, where the value 0 means: 'It does not matter' and 
    the value 10 means: 'It is very important'.
    '''))
    democracy_live = make_question(_('''
    Do you think the country of your citizenship is democratic? 
    Please tick a box on the scale, where the value 0 means: 'It is not democratic at all' and 
    the value 10 means: 'It is governed strictly based on democracy principals'.
    '''))
