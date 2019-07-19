from otree.api import widgets, Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from GameFeb19_intro.pages import Page, WaitPage

from GameFeb19_intro.models import add_currency

import random

from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class SessionWideWaitingPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.session.vars['questions_part'] = self.session.vars['questions_part'] + 1
        self.session.vars['CT_part'] = self.session.vars['questions_part']

    def is_displayed(self):
        return self.round_number == 1


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'part_num': self.session.vars['questions_part'],
                'num_rounds': Constants.num_rounds,
                'rate_CT': add_currency(
            self.session.config['currency_used'],
            self.session.vars['rate_CT'] * self.session.config['real_world_currency_per_point'])}

    def app_after_this_page(self, upcoming_apps):
        if self.session.config['skip_CognitiveTest']:
            return upcoming_apps[0]


class Question(Page):
    template_name = 'global/Question.html'

    form_model = 'player'

    def get_form_fields(self):
        qd = self.player.current_question()
        if int(qd['n_choices']) > 0:
            return ['submitted_answer_options']
        else:
            return ['submitted_answer']

    def submitted_answer_options_choices(self):
        qd = self.player.current_question()
        if int(qd['n_choices']) > 0:
            return [[i, qd['choice{}'.format(i)]] for i in range(1, int(qd['n_choices'])+1, 1)]

    def vars_for_template(self):
        qd = self.player.current_question()
        return {'round': self.round_number,
                'num_rounds': Constants.num_rounds,
                'n_choices': int(qd['n_choices'])}

    def before_next_page(self):
        self.player.check_correct()
        if self.round_number == Constants.num_rounds:
            self.player.set_payoffs()


page_sequence = [
    SessionWideWaitingPage,
    Introduction,
    Question
]
