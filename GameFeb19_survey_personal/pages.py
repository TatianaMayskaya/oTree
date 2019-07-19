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

    def get_form_fields(self):
        num = self.participant.vars['questions'][self.round_number - 1]
        if num == 1:
            return ['age']
        elif num == 2:
            return ['gender']
        elif num == 3:
            return ['field']
        elif num == 4:
            return ['native_language']
        elif num == 5:
            return ['income']
        elif num == 6:
            return ['riskat']
        elif num == 7:
            return ['happy_now']
        elif num == 8:
            return ['happy_future']
        elif num == 9:
            return ['trust']
        elif num == 10:
            return ['freedom']
        elif num == 11:
            return ['democracy']
        elif num == 12:
            return ['democracy_live']

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
