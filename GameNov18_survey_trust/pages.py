from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, add_tokens, add_currency


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'rate_survey_text': self.session.vars['rate_survey_text'],
                'part_num': self.participant.vars['survey_part']}


class Rules(Page):
    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'endowment': Constants.endowment,
                'multiplier': Constants.multiplier[self.round_number - 1],
                'part_num': self.participant.vars['survey_part']}


class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        if self.session.config['language'] == 1:
            question_label = 'Please enter an amount from 0 to {}:'.format(Constants.endowment)
        else:
            question_label = 'Пожалуйста, введите число от 0 до {}:'.format(Constants.endowment)
        return {'language': self.session.config['language'],
                'endowment': Constants.endowment,
                'multiplier': Constants.multiplier[self.round_number - 1],
                'question_label': question_label,
                'part_num': self.participant.vars['survey_part']}


class SendBackWaitPage(WaitPage):
    def vars_for_template(self):
        return {'title_text': self.session.vars['wait_page_title'], 'body_text': self.session.vars['wait_page_body']}


class SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        multiplied_amount = self.group.sent_amount * Constants.multiplier[self.round_number - 1]
        if self.session.config['language'] == 1:
            question_label = 'Please enter an amount from 0 to {}:'.format(multiplied_amount)
        else:
            question_label = 'Пожалуйста, введите число от 0 до {}:'.format(multiplied_amount)
        return {'language': self.session.config['language'],
                'endowment': Constants.endowment,
                'multiplier': Constants.multiplier[self.round_number - 1],
                'sent_amount': self.group.sent_amount,
                'multiplied_amount': multiplied_amount,
                'multiplied_amount_text': add_tokens(self.session.config['language'], multiplied_amount),
                'question_label': question_label,
                'part_num': self.participant.vars['survey_part']}

    def sent_back_amount_max(self):
        return self.group.sent_amount * Constants.multiplier[self.round_number - 1]


class ResultsWaitPage(WaitPage):
    def vars_for_template(self):
        return {'title_text': self.session.vars['wait_page_title'], 'body_text': self.session.vars['wait_page_body']}

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class TrustResults(Page):
    def vars_for_template(self):
        multiplied_amount = self.group.sent_amount * Constants.multiplier[self.round_number - 1]
        return {'language': self.session.config['language'],
                'endowment': Constants.endowment,
                'multiplier': Constants.multiplier[self.round_number - 1],
                'multiplied_amount': multiplied_amount,
                'multiplied_amount_text': add_tokens(self.session.config['language'], multiplied_amount),
                'sent_amount': self.group.sent_amount,
                'sent_back_amount': self.group.sent_back_amount,
                'sent_amount_text': add_tokens(self.session.config['language'], self.group.sent_amount),
                'sent_back_amount_text': add_tokens(self.session.config['language'], self.group.sent_back_amount),
                'payoff_text': add_tokens(self.session.config['language'], self.player.payoff_trust),
                'part_num': self.participant.vars['survey_part']}

    def before_next_page(self):
        self.group.set_payoffs()
        if self.round_number == Constants.num_rounds:
            self.player.set_final_payoff()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'player_in_all_rounds': self.player.in_all_rounds(),
                'payment_question': self.player.payment_question,
                'payment': self.player.payoff_text,
                'part_num': self.participant.vars['survey_part']}

    def before_next_page(self):
        if self.round_number == Constants.num_rounds:
            self.participant.vars['survey_part'] = self.participant.vars['survey_part'] + 1


page_sequence = [
    Introduction,
    Rules,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    TrustResults,
    Results
]
