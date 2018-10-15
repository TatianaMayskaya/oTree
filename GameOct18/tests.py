from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
            yield (pages.Quiz, {'quiz_questions_1': 'Нет',
                                'quiz_questions_2': 'Ваш партнёр будет выбираться случайным образом перед каждой игрой',
                                'quiz_questions_3': 0,
                                'quiz_questions_4': 100,
                                'quiz_questions_5': 0,
                                'quiz_questions_6': 'После',
                                'quiz_questions_7': 'Нет',
                                'quiz_questions_8': 2,
                                'quiz_questions_9': '1 или 12 в зависимости от первого решения',
                                'quiz_questions_10': 'Да'})
            yield (pages.QuizResults)
            yield (pages.RoleInGame)
        if self.round_number <= 3:
            yield (pages.GameAnnouncement)
        if self.player.id_in_group == 1 and self.round_number <= 2:
            yield (pages.Offer, {'amount_offered': 20})
        if self.player.id_in_group == 1 and self.round_number == 3:
            yield (pages.Offer, {'amount_offered_1': 30, 'amount_offered_2': 40})
        if self.player.id_in_group == 2 and self.round_number == 3:
            yield (pages.GameChoice, {'game_played': 1})
        if self.player.id_in_group == 2 and self.round_number <= 3:
            if self.round_number == 1 or (self.round_number == 3 and self.group.game_played == 1):
                yield (pages.Accept, {'response_0': False,
                                      'response_10': False,
                                      'response_20': False,
                                      'response_30': True,
                                      'response_40': True,
                                      'response_50': True,
                                      'response_60': True,
                                      'response_70': True,
                                      'response_80': True,
                                      'response_90': True,
                                      'response_100': True})
            else:
                yield (pages.Accept)
        if self.round_number == 3:
            yield (pages.Results)
            yield (pages.Survey11, {'survey1_questions_1_1': '-',
                                    'survey1_questions_1_2': '-',
                                    'survey1_questions_1_3': '-'})
            if self.player.id_in_group == 1:
                yield (pages.Survey12, {'survey1_questions_2_1_response_0': False,
                                        'survey1_questions_2_1_response_10': False,
                                        'survey1_questions_2_1_response_20': False,
                                        'survey1_questions_2_1_response_30': False,
                                        'survey1_questions_2_1_response_40': False,
                                        'survey1_questions_2_1_response_50': True,
                                        'survey1_questions_2_1_response_60': True,
                                        'survey1_questions_2_1_response_70': True,
                                        'survey1_questions_2_1_response_80': True,
                                        'survey1_questions_2_1_response_90': True,
                                        'survey1_questions_2_1_response_100': True})
            else:
                yield (pages.Survey12, {'survey1_questions_2_2_amount_offered': 20})
            if self.player.id_in_group == 1:
                yield (pages.Survey13, {'survey1_questions_3_1_game_played': 2})
            else:
                yield (pages.Survey13, {'survey1_questions_3_2_amount_offered': 10})
            if self.player.id_in_group == 1 and self.player.survey1_questions_3_1_game_played == 1:
                yield (pages.Survey14, {'survey1_questions_4_1_response_0': False,
                                        'survey1_questions_4_1_response_10': False,
                                        'survey1_questions_4_1_response_20': False,
                                        'survey1_questions_4_1_response_30': True,
                                        'survey1_questions_4_1_response_40': True,
                                        'survey1_questions_4_1_response_50': True,
                                        'survey1_questions_4_1_response_60': True,
                                        'survey1_questions_4_1_response_70': True,
                                        'survey1_questions_4_1_response_80': True,
                                        'survey1_questions_4_1_response_90': True,
                                        'survey1_questions_4_1_response_100': True})
            if self.player.id_in_group == 2:
                yield (pages.Survey14, {'survey1_questions_4_2_amount_offered_1': 50,
                                        'survey1_questions_4_2_amount_offered_2': 30})
            yield (pages.Survey15, {'survey1_questions_5_1': 1,
                                    'survey1_questions_5_2': 1,
                                    'survey1_questions_5_3': 1,
                                    'survey1_questions_5_4': 1,
                                    'survey1_questions_5_5': 1,
                                    'survey1_questions_5_6': 1,
                                    'survey1_questions_5_7': 1,
                                    'survey1_questions_5_8': 1,
                                    'survey1_questions_5_9': 1,
                                    'survey1_questions_5_10': 1,
                                    'survey1_questions_5_11': 1,
                                    'survey1_questions_5_12': 1,
                                    'survey1_questions_5_13': 1,
                                    'survey1_questions_5_14': 1,
                                    'survey1_questions_5_15': 1,
                                    'survey1_questions_5_16': 1,
                                    'survey1_questions_5_17': 1,
                                    'survey1_questions_5_18': 1,
                                    'survey1_questions_5_19': 1,
                                    'survey1_questions_5_20': 1,
                                    'survey1_questions_5_21': 1,
                                    'survey1_questions_5_22': 1,
                                    'survey1_questions_5_23': 1,
                                    'survey1_questions_5_24': 1,
                                    'survey1_questions_5_25': 1,
                                    'survey1_questions_5_26': 1,
                                    'survey1_questions_5_27': 1,
                                    'survey1_questions_5_28': 1})
            yield (pages.Survey16, {'survey1_questions_6_1': '-',
                                    'survey1_questions_6_2': '-',
                                    'survey1_questions_6_3': '-',
                                    'survey1_questions_6_4': '-'})
            yield (pages.Survey17)
            yield (pages.Survey2intro)
            for num in self.participant.vars['order_questions']:
                if num == 1:
                    yield (pages.Survey2, {'survey2_question_RiskyProject1': 30})
                elif num == 2:
                    yield (pages.Survey2, {'survey2_question_RiskyProject2': 10})
                elif num == 3:
                    yield (pages.Survey2, {'survey2_RiskyUrns1_0': 1,
                                           'survey2_RiskyUrns1_10': 1,
                                           'survey2_RiskyUrns1_20': 1,
                                           'survey2_RiskyUrns1_30': 1,
                                           'survey2_RiskyUrns1_40': 1,
                                           'survey2_RiskyUrns1_50': 1,
                                           'survey2_RiskyUrns1_60': 1,
                                           'survey2_RiskyUrns1_70': 1,
                                           'survey2_RiskyUrns1_80': 1,
                                           'survey2_RiskyUrns1_90': 1,
                                           'survey2_RiskyUrns1_100': 1,
                                           'survey2_RiskyUrns1_110': 1,
                                           'survey2_RiskyUrns1_120': 1,
                                           'survey2_RiskyUrns1_130': 1,
                                           'survey2_RiskyUrns1_140': 1,
                                           'survey2_RiskyUrns1_150': 1})
                else:
                    yield (pages.Survey2, {'survey2_RiskyUrns2_0': 1,
                                           'survey2_RiskyUrns2_10': 1,
                                           'survey2_RiskyUrns2_20': 1,
                                           'survey2_RiskyUrns2_30': 1,
                                           'survey2_RiskyUrns2_40': 1,
                                           'survey2_RiskyUrns2_50': 1,
                                           'survey2_RiskyUrns2_60': 1,
                                           'survey2_RiskyUrns2_70': 2,
                                           'survey2_RiskyUrns2_80': 2,
                                           'survey2_RiskyUrns2_90': 2,
                                           'survey2_RiskyUrns2_100': 2})
                yield (pages.Survey2res)
            yield (pages.Survey2Results)
            yield (pages.Survey3intro)
        if self.round_number == 4 or self.round_number == 5:
            yield (pages.Prisoner, {'Prisoner_decision': 'A1'})
            yield (pages.PrisonerResults)
        if self.round_number == 5:
            yield (pages.Survey3Results)
            yield (pages.SurveyPersonal, {'survey_personal_questions_1': 'Женский',
                                          'survey_personal_questions_2': 25,
                                          'survey_personal_questions_3': '-',
                                          'survey_personal_questions_4': 0,
                                          'survey_personal_questions_5': 0,
                                          'survey_personal_questions_6': 0,
                                          'survey_personal_questions_7': 0,
                                          'survey_personal_questions_8': 0,
                                          'survey_personal_questions_9': 0,
                                          'survey_personal_questions_10': 10,
                                          'survey_personal_questions_11': 5,
                                          'survey_personal_questions_12': 0,
                                          'survey_personal_questions_13': 0,
                                          'survey_personal_questions_14': 0,
                                          'survey_personal_questions_15': 0,
                                          'survey_personal_questions_16': 0,
                                          'survey_personal_questions_17': 0})
