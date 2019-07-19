from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from GameFeb19_intro.pages import Page, WaitPage

from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class SessionWideWaitingPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.session.vars['survey_part'] = self.session.vars['survey_part'] + 1

    def is_displayed(self):
        return self.round_number == 1


class Question(Page):
    form_model = 'player'
    form_fields = ['submitted_answer']

    def vars_for_template(self):
        return {'round': self.round_number,
                'num_rounds': Constants.num_rounds,
                'part_num': self.session.vars['survey_part']}

    def app_after_this_page(self, upcoming_apps):
        if self.session.config['skip_survey']:
            return upcoming_apps[0]


page_sequence = [
    SessionWideWaitingPage,
    Question
]
