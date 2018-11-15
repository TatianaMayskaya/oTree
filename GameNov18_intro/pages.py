from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, add_currency


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        if self.session.config['language'] == 1:
            instructions_template = 'GameNov18_intro/InstructionsEn.html'
        else:
            instructions_template = 'GameNov18_intro/InstructionsRus.html'
        return {'language': self.session.config['language'],
                'instructions_template': instructions_template,
                'show_up_text': add_currency(self.session.config['currency_used'], self.session.vars['show_up']),
                'rate_text': add_currency(self.session.config['currency_used'], self.session.vars['rate']),
                'rate_survey_text': add_currency(self.session.config['currency_used'], self.session.vars['rate_survey']),
                'endowment': self.session.vars['endowment'],
                'payoff_if_rejected': self.session.vars['payoff_if_rejected']
                }


class Question(Page):
    form_model = 'player'
    form_fields = ['submitted_answer']

    def submitted_answer_choices(self):
        qd = self.player.current_question()
        if int(qd['n_choices']) > 0:
            return [[i, qd['choice{}'.format(i)]] for i in range(1, int(qd['n_choices'])+1, 1)]

    def vars_for_template(self):
        return {'language': self.session.config['language']}

    def before_next_page(self):
        self.player.check_correct()


class Results(Page):

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'language': self.session.config['language'],
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds]),
            'is_correct': self.player.get_is_correct_display()
        }


page_sequence = [
    Introduction,
    Question,
    Results
]
