from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Quiz(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 1:
            return ['quiz_questions_{}'.format(i) for i in Constants.quiz_questions_range]
        else:
            return []

    def is_displayed(self):
        return self.round_number == 1


class QuizResults(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        quiz_table = []
        for p in Constants.quiz_questions_range:
            answer = getattr(self.player, 'quiz_questions_{}'.format(p))
            quiz_table.append(((Constants.quiz_question[p-1], answer, Constants.quiz_correct_answers[p-1],
                                Constants.quiz_explanation[p-1])))
        return {'quiz_table': quiz_table}


class RoleInGame(Page):
    def is_displayed(self):
        return self.round_number == 1


class GameAnnouncement(Page):
    def is_displayed(self):
        return self.round_number <= 3


class Offer(Page):
    form_model = 'group'

    def get_form_fields(self):
        if self.round_number == 3:
            return ['amount_offered_1', 'amount_offered_2']
        else:
            return ['amount_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number <= 3


class GameChoice(Page):
    form_model = 'group'
    form_fields = ['game_played']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == 3


class Accept(Page):
    form_model = 'group'

    def get_form_fields(self):
        if self.round_number == 1 or (self.round_number == 3 and self.group.game_played == 1):
            return ['response_{}'.format(int(i)) for i in Constants.offer_choices]
        else:
            return []

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number <= 3


class ResultsWaitPage(WaitPage):
    title_text = Constants.wait_page_title
    body_text = Constants.wait_page_body

    def is_displayed(self):
        return self.round_number <= 3

    def after_all_players_arrive(self):
        if self.round_number <= 3:
            self.group.set_payoffs()


class Results(Page):
    def is_displayed(self):
        return self.round_number == 3


class Survey11(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3:
            return ['survey1_questions_1_{}'.format(i) for i in Constants.survey1_questions_1_range]
        else:
            return []

    def is_displayed(self):
        return self.round_number == 3


class Survey12(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3 and self.player.id_in_group == 1:
            return ['survey1_questions_2_1_response_{}'.format(int(i)) for i in Constants.offer_choices]
        elif self.round_number == 3 and self.player.id_in_group == 2:
            return ['survey1_questions_2_2_amount_offered']
        else:
            return []

    def is_displayed(self):
        return self.round_number == 3


class Survey13(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3 and self.player.id_in_group == 1:
            return ['survey1_questions_3_1_game_played']
        elif self.round_number == 3 and self.player.id_in_group == 2:
            return ['survey1_questions_3_2_amount_offered']
        else:
            return []

    def is_displayed(self):
        return self.round_number == 3


class Survey14(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3 and self.player.id_in_group == 1 and \
                self.player.survey1_questions_3_1_game_played == 1:
            return ['survey1_questions_4_1_response_{}'.format(int(i)) for i in Constants.offer_choices]
        elif self.round_number == 3 and self.player.id_in_group == 2:
            return ['survey1_questions_4_2_amount_offered_1', 'survey1_questions_4_2_amount_offered_2']
        else:
            return []

    def is_displayed(self):
        return self.round_number == 3


class Survey15(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3:
            return ['survey1_questions_5_{}'.format(i) for i in Constants.survey1_questions_2_range]
        else:
            return []

    def is_displayed(self):
        return self.round_number == 3


class Survey16(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3:
            return ['survey1_questions_6_{}'.format(i) for i in Constants.survey1_questions_3_range]
        else:
            return []

    def is_displayed(self):
        return self.round_number == 3


class Survey17(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3:
            return ['survey1_questions_7']
        else:
            return []

    def is_displayed(self):
        return self.round_number == 3


class Survey2intro(Page):
    def is_displayed(self):
        return self.round_number == 3

    def before_next_page(self):
        if self.round_number == 3:
            self.participant.vars['order_questions'] = \
                random.sample(Constants.survey2_questions_range, Constants.survey2_questions_count)
            self.player.order_questions = str(self.participant.vars['order_questions'])
            self.participant.vars['question_template'] = []
            self.participant.vars['result_template'] = []
            self.participant.vars['question_form'] = []
            self.participant.vars['question_number'] = 0
            self.player.survey2_total_payoff = 0
            for i in self.participant.vars['order_questions']:
                if i == 1:
                    self.participant.vars['question_template'].append('GameOct18/RiskyProject1.html')
                    self.participant.vars['result_template'].append('GameOct18/RiskyProject1Results.html')
                    self.participant.vars['question_form'].append(['survey2_question_RiskyProject1'])
                elif i == 2:
                    self.participant.vars['question_template'].append('GameOct18/RiskyProject2.html')
                    self.participant.vars['result_template'].append('GameOct18/RiskyProject2Results.html')
                    self.participant.vars['question_form'].append(['survey2_question_RiskyProject2'])
                elif i == 3:
                    self.participant.vars['question_template'].append('GameOct18/RiskyUrns1.html')
                    self.participant.vars['result_template'].append('GameOct18/RiskyUrns1Results.html')
                    lst = ['survey2_RiskyUrns1_{}'.format(j) for j in Constants.Options_RiskyUrns1]
                    self.participant.vars['question_form'].append(lst)
                else:
                    self.participant.vars['question_template'].append('GameOct18/RiskyUrns2.html')
                    self.participant.vars['result_template'].append('GameOct18/RiskyUrns2Results.html')
                    lst = ['survey2_RiskyUrns2_{}'.format(j) for j in Constants.Options_RiskyUrns2]
                    self.participant.vars['question_form'].append(lst)


class Survey2(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 3:
            return self.participant.vars['question_form'][self.participant.vars['question_number']]
        else:
            return []

    def is_displayed(self):
        return self.round_number == 3

    def vars_for_template(self):
        return {'template': self.participant.vars['question_template'][self.participant.vars['question_number']]}

    def before_next_page(self):
        if self.round_number == 3:
            self.player.get_payoff_survey2()


class Survey2res(Page):
    def is_displayed(self):
        return self.round_number == 3

    def vars_for_template(self):
        return {'template': self.participant.vars['result_template'][self.participant.vars['question_number']]}

    def before_next_page(self):
        if self.round_number == 3:
            self.participant.vars['question_number'] = self.participant.vars['question_number'] + 1


class Survey3intro(Page):
    def is_displayed(self):
        return self.round_number == 3


class Prisoner(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 4 or self.round_number == 5:
            return ['Prisoner_decision']
        else:
            return []

    def is_displayed(self):
        return self.round_number == 4 or self.round_number == 5

    def vars_for_template(self):
        return {
            'both_cooperate_payoff': Constants.Prisoner_both_cooperate_payoff[self.round_number-4],
            'both_defect_payoff': Constants.Prisoner_both_defect_payoff[self.round_number-4],
            'betrayed_payoff': Constants.Prisoner_betrayed_payoff[self.round_number - 4],
            'betray_payoff': Constants.Prisoner_betray_payoff[self.round_number - 4]
        }


class PrisonerWaitPage(WaitPage):
    title_text = Constants.wait_page_title
    body_text = Constants.wait_page_body

    def is_displayed(self):
        return self.round_number == 4 or self.round_number == 5

    def after_all_players_arrive(self):
        if self.round_number == 4 or self.round_number == 5:
            for p in self.group.get_players():
                p.set_prisoner_payoff()


class PrisonerResults(Page):
    def is_displayed(self):
        return self.round_number == 4 or self.round_number == 5

    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'my_decision': me.Prisoner_decision,
            'opponent_decision': opponent.Prisoner_decision,
            'payoff': me.Prisoner_payoff
        }


class SurveyPersonal(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.round_number == 6:
            return ['survey_personal_questions_{}'.format(i) for i in Constants.survey_personal_range]
        else:
            return []

    def is_displayed(self):
        return self.round_number == 6


page_sequence = [
    # Introduction,
    # Quiz,
    # QuizResults,
    # RoleInGame,
    # GameAnnouncement,
    # Offer,
    # GameChoice,
    # Accept,
    # ResultsWaitPage,
    # Results,
    # Survey11,
    # Survey12,
    # Survey13,
    # Survey14,
    # Survey15,
    # Survey16,
    # Survey17,
    Survey2intro
]

# for i in Constants.survey2_questions_range:
#     page_sequence.append(Survey2)
#     page_sequence.append(Survey2res)
#
# page_sequence.append(Survey3intro)
# page_sequence.append(Prisoner)
# page_sequence.append(PrisonerWaitPage)
# page_sequence.append(PrisonerResults)
page_sequence.append(SurveyPersonal)
