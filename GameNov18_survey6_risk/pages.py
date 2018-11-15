from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'language': self.session.config['language'],
                'rate_survey_text': self.session.vars['rate_survey_text']}


class RiskyProject(Page):
    form_model = 'player'

    def get_form_fields(self):
        num = self.participant.vars['questions_order'][self.round_number - 1]
        if num == 1:
            return ['question_RiskyProject1']
        elif num == 2:
            return ['question_RiskyProject2']
        else:
            return []

    def is_displayed(self):
        return self.participant.vars['questions_order'][self.round_number - 1] <= 2

    def vars_for_template(self):
        num = self.participant.vars['questions_order'][self.round_number - 1]
        return {'language': self.session.config['language'],
                'endowment': Constants.endowment_RiskyProject[num - 1],
                'prob': Constants.prob_success_RiskyProject[num - 1],
                'return': Constants.return_RiskyProject[num - 1],
                'question_label': self.participant.vars['question_RiskyProject'],
                'num': num
                }

    def before_next_page(self):
        self.player.get_payoff()


class RiskyProjectResults(Page):
    def is_displayed(self):
        return self.participant.vars['questions_order'][self.round_number - 1] <= 2

    def vars_for_template(self):
        num = self.participant.vars['questions_order'][self.round_number - 1]
        if num == 1:
            invested = self.player.question_RiskyProject1
            success = self.player.RiskyProject1_success
            earned = self.player.RiskyProject1_earned
            payoff = self.player.RiskyProject1_payoff
        else:
            invested = self.player.question_RiskyProject2
            success = self.player.RiskyProject2_success
            earned = self.player.RiskyProject2_earned
            payoff = self.player.RiskyProject2_payoff
        return {'language': self.session.config['language'],
                'invested': invested,
                'endowment': Constants.endowment_RiskyProject[num - 1],
                'prob': Constants.prob_success_RiskyProject[num - 1],
                'return': Constants.return_RiskyProject[num - 1],
                'success': success,
                'earned': earned,
                'payoff': payoff
                }


class RiskyUrns(Page):
    form_model = 'player'

    def get_form_fields(self):
        num = self.participant.vars['questions_order'][self.round_number - 1]
        if num == 3:
            return ['RiskyUrns1_{}'.format(j) for j in Constants.Options_RiskyUrns1]
        elif num == 4:
            return ['RiskyUrns2_{}'.format(j) for j in Constants.Options_RiskyUrns2]
        else:
            return []

    def RiskyUrns1_0_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[0])]]

    def RiskyUrns1_10_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[1])]]

    def RiskyUrns1_20_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[2])]]

    def RiskyUrns1_30_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[3])]]

    def RiskyUrns1_40_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[4])]]

    def RiskyUrns1_50_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[5])]]

    def RiskyUrns1_60_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[6])]]

    def RiskyUrns1_70_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[7])]]

    def RiskyUrns1_80_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[8])]]

    def RiskyUrns1_90_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[9])]]

    def RiskyUrns1_100_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[10])]]

    def RiskyUrns1_110_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[11])]]

    def RiskyUrns1_120_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[12])]]

    def RiskyUrns1_130_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[13])]]

    def RiskyUrns1_140_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[14])]]

    def RiskyUrns1_150_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns1[15])]]

    def RiskyUrns2_0_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[0])]]

    def RiskyUrns2_10_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[1])]]

    def RiskyUrns2_20_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[2])]]

    def RiskyUrns2_30_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[3])]]

    def RiskyUrns2_40_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[4])]]

    def RiskyUrns2_50_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[5])]]

    def RiskyUrns2_60_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[6])]]

    def RiskyUrns2_70_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[7])]]

    def RiskyUrns2_80_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[8])]]

    def RiskyUrns2_90_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[9])]]

    def RiskyUrns2_100_choices(self):
        return [[1, self.participant.vars['choice1_RiskyUrns']],
                [2, str(self.participant.vars['choice2_RiskyUrns']).format(Constants.Options_RiskyUrns2[10])]]

    def is_displayed(self):
        return self.participant.vars['questions_order'][self.round_number - 1] > 2

    def vars_for_template(self):
        num = self.participant.vars['questions_order'][self.round_number - 1]
        return {'language': self.session.config['language'],
                'lose_balls': Constants.LoseBalls_RiskyUrns[num - 3],
                'win_balls': Constants.WinBalls_RiskyUrns[num - 3],
                'win_payoff': Constants.WinPayoff_RiskyUrns[num - 3],
                'question_label': self.participant.vars['label_RiskyUrns'],
                'urn_num': num - 2
                }

    def before_next_page(self):
        self.player.get_payoff()


class RiskyUrnsResults(Page):
    def is_displayed(self):
        return self.participant.vars['questions_order'][self.round_number - 1] > 2

    def vars_for_template(self):
        num = self.participant.vars['questions_order'][self.round_number - 1]
        if num == 3:
            sure = self.player.RiskyUrns1_sure
            choice_num = self.player.RiskyUrns1_choice_num
            choice = self.player.RiskyUrns1_choice
            payoff = self.player.RiskyUrns1_payoff
        else:
            sure = self.player.RiskyUrns2_sure
            choice_num = self.player.RiskyUrns2_choice_num
            choice = self.player.RiskyUrns2_choice
            payoff = self.player.RiskyUrns2_payoff
        return {'language': self.session.config['language'],
                'lose_balls': Constants.LoseBalls_RiskyUrns[num - 3],
                'win_balls': Constants.WinBalls_RiskyUrns[num - 3],
                'win_payoff': Constants.WinPayoff_RiskyUrns[num - 3],
                'urn_num': num - 2,
                'sure': sure,
                'choice_num': choice_num,
                'choice': choice,
                'payoff': payoff,
                'choice1_RiskyUrns': self.participant.vars['choice1_RiskyUrns']
                }


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        payoff = [self.participant.vars['RiskyProject1_payoff'],
                  self.participant.vars['RiskyProject2_payoff'],
                  self.participant.vars['RiskyUrns1_payoff'],
                  self.participant.vars['RiskyUrns2_payoff']]
        return {
            'language': self.session.config['language'],
            'payoff_1': payoff[self.participant.vars['questions_order'][0] - 1],
            'payoff_2': payoff[self.participant.vars['questions_order'][1] - 1],
            'payoff_3': payoff[self.participant.vars['questions_order'][2] - 1],
            'payoff_4': payoff[self.participant.vars['questions_order'][3] - 1],
            'payment_question': self.player.payment_question_in_order_for_subject,
            'payment': self.player.payoff_text
        }


page_sequence = [
    Introduction,
    RiskyProject,
    RiskyProjectResults,
    RiskyUrns,
    RiskyUrnsResults,
    Results
]
