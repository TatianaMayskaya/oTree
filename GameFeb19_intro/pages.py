from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, add_currency

from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# =====================================================================================================================
# Use this for dynamically change language based on app config when session starts ====================================

class TransMixin:
    def get_context_data(self, **context):
        user_language = self.session.config.get('language', 'en')
        translation.activate(user_language)
        if hasattr(settings, 'LANGUAGE_SESSION_KEY'):
            self.request.session[settings.LANGUAGE_SESSION_KEY] = user_language
        return super().get_context_data(**context)


class Page(TransMixin, Page):
    pass


class WaitPage(TransMixin, WaitPage):
    pass


# =====================================================================================================================
# 'Normal pages' begin ================================================================================================


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        if self.session.config['language'] == 'en':
            instructions_template = 'GameFeb19_intro/InstructionsEn.html'
        else:
            instructions_template = 'GameFeb19_intro/InstructionsRu.html'
        return {'instructions_template': instructions_template,
                'show_up_text': add_currency(self.session.config['currency_used'],
                                             self.session.config['participation_fee']),
                'endowment': self.session.vars['endowment'],
                'endowment_plus_1': self.session.vars['endowment'] + 1,
                'payoff_if_rejected': self.session.vars['payoff_if_rejected'],
                'n_rounds': self.session.config['n_rounds']
                }

    def app_after_this_page(self, upcoming_apps):
        if self.session.config['skip_test']:
            return upcoming_apps[0]


class Question(Page):
    form_model = 'player'
    form_fields = ['submitted_answer']

    def vars_for_template(self):
        return {'try': self.player.n_try,
                'round': self.round_number,
                'num_rounds': Constants.num_rounds}

    def is_displayed(self):
        return not self.player.is_correct

    def before_next_page(self):
        self.player.check_correct()


class Results(Page):
    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds]),
            'is_correct': self.player.get_is_correct_display(),
            'round': self.round_number,
            'num_rounds': Constants.num_rounds
        }


page_sequence = [
    Introduction,
    Question, Question, Question, Question, Question,
    Results
]
