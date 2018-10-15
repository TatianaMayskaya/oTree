from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random, csv


author = 'Your name here'

doc = """
Your app description
"""


def add_currency(currency_used, num):
    if currency_used == 0:
        return '$' + str(num)
    elif currency_used == 1:
        return '£' + str(num)
    else:
        if num != 1:
            return str(num) + ' рублей'
        else:
            return str(num) + ' рубль'


class Constants(BaseConstants):
    name_in_url = 'GameOct18'
    players_per_group = 2
    num_rounds = 5
    language = 2  # 1=EN, 2=RU
    currency_used = 2  # 0=USD, 1=POUNDS, 2=RUBLES

    if language == 1:
        instructions_template = 'GameOct18/InstructionsEn.html'
        wait_page_title = 'Please wait'
        wait_page_body = 'Waiting for the other participants'
    else:
        instructions_template = 'GameOct18/InstructionsRus.html'
        wait_page_title = 'Пожалуйста, подождите'
        wait_page_body = 'Не все участники ещё закончили игру'

    if currency_used == 0:
        show_up = 5
        rate = 0.2
        rate_survey = 0.02
    elif currency_used == 1:
        show_up = 3
        rate = 0.2
        rate_survey = 0.02
    else:
        show_up = 200
        rate = 10
        rate_survey = 1
    show_up_text = add_currency(currency_used, show_up)
    rate_text = add_currency(currency_used, rate)
    rate_survey_text = add_currency(currency_used, rate_survey)

    endowment = 100
    payoff_if_rejected = 0
    offer_increment = 10

    offer_choices = range(0, endowment + offer_increment, offer_increment)
    offer_choices_count = len(offer_choices)

    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))

    offer_options_in_words = []
    for give, keep in keep_give_amounts:
        if language == 1:
            offer_options_in_words.append((give, 'Player 2 gets {} tokens (you keep {} tokens)'.format(give, keep)))
        else:
            offer_options_in_words.append((give, 'Игрок 2 получает {} жетонов (у Вас останется {} жетонов)'.format(give, keep)))

    endowment_RiskyProject = [100, 100]
    invest_increment = 10
    invest_options_RiskyProject1 = range(0, endowment_RiskyProject[0] + invest_increment, invest_increment)
    prob_success_RiskyProject = [50, 35]
    return_RiskyProject = [2, 3]
    invest_options_RiskyProject2 = range(0, endowment_RiskyProject[1] + invest_increment, invest_increment)

    LoseBalls_RiskyUrns = [15, 10]
    WinBalls_RiskyUrns = [15, 10]
    WinPayoff_RiskyUrns = [150, 100]
    Step_RiskyUrns = [10, 10]
    Options_RiskyUrns1 = range(0, WinPayoff_RiskyUrns[0] + Step_RiskyUrns[0], Step_RiskyUrns[0])
    Options_RiskyUrns2 = range(0, WinPayoff_RiskyUrns[1] + Step_RiskyUrns[1], Step_RiskyUrns[1])

    Prisoner_both_cooperate_payoff = [300, 200]  # [95, 80]
    Prisoner_both_defect_payoff = [200, 100]  # [62, 50]
    Prisoner_betrayed_payoff = [100, 0]  # [31, 24]
    Prisoner_betray_payoff = [400, 300]  # [120, 100]
    Prisoner_cooperate = 'A1'
    Prisoner_defect = 'A2'

    SurveyPersonal_number = 4

    survey1_question_1 = []
    survey1_question_2 = []
    survey1_question_3 = []
    SurveyPersonal_question = []
    if language == 1:
        question_RiskyProject = 'Please choose how many tokens you want to invest in the risky project.'
        label_RiskyUrns = 'Choose one option'
        choice1_RiskyUrns = 'Urn gamble'
        choice2_RiskyUrns = '{} tokens'

    else:
        question_RiskyProject = 'Пожалуйста, выберите, сколько жетонов Вы проинвестируете в рискованный проект.'
        label_RiskyUrns = 'Выберите одну опцию'
        choice1_RiskyUrns = 'Лотерея'
        choice2_RiskyUrns = '{} жетонов'

    if language == 1:
        with open('GameOct18/quiz_en.csv') as quiz_file:
            quiz_file_list = list(csv.DictReader(quiz_file))
        with open('GameOct18/survey_en.csv') as survey_file:
            survey_list = list(csv.DictReader(survey_file))
    else:
        with open('GameOct18/quiz_ru.csv', encoding='utf-8') as quiz_file:
            quiz_file_list = list(csv.DictReader(quiz_file))
        with open('GameOct18/survey_ru.csv', encoding='utf-8') as survey_file:
            survey_list = list(csv.DictReader(survey_file))

    quiz_questions_count = len(quiz_file_list)
    quiz_questions_range = range(1, quiz_questions_count + 1, 1)
    survey1_question_1 = []
    survey1_question_2 = []
    survey1_question_3 = []
    survey1_question_4 = []
    SurveyPersonal_question = []
    for i in range(0, len(survey_list), 1):
        if survey_list[i]['survey'] == '1':
            survey1_question_1.append(survey_list[i]['question'])
        elif survey_list[i]['survey'] == '2':
            survey1_question_2.append(survey_list[i]['question'])
        elif survey_list[i]['survey'] == '3':
            survey1_question_3.append(survey_list[i]['question'])
        elif survey_list[i]['survey'] == '4':
            survey1_question_4.append(survey_list[i]['question'])
        else:
            if survey_list[i]['choice1']:
                SurveyPersonal_question.append([survey_list[i]['question'], survey_list[i]['choice1'],
                                                survey_list[i]['choice2'], survey_list[i]['choice3']])
            else:
                SurveyPersonal_question.append(survey_list[i]['question'])
    survey1_questions_1_count = len(survey1_question_1)
    survey1_questions_1_range = range(1, survey1_questions_1_count + 1, 1)
    survey1_questions_2_count = len(survey1_question_2)
    survey1_questions_2_range = range(1, survey1_questions_2_count + 1, 1)
    survey1_questions_3_count = len(survey1_question_3)
    survey1_questions_3_range = range(1, survey1_questions_3_count + 1, 1)

    survey2_questions_count = 4
    survey2_questions_range = range(1, survey2_questions_count + 1, 1)

    survey_personal_count = len(SurveyPersonal_question)
    survey_personal_range = range(1, survey_personal_count + 1, 1)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)


def make_field(offer):
    if Constants.language == 1:
        return models.BooleanField(
            choices=[[True, 'Accept'], [False, 'Reject']],
            widget=widgets.RadioSelectHorizontal,
            label='You get {} tokens (player 1 keeps {} tokens)'.format(offer, Constants.endowment - offer))
    else:
        return models.BooleanField(
            choices=[[True, 'Принять'], [False, 'Отказаться']],
            widget=widgets.RadioSelectHorizontal,
            label='Вы получаете {} жетонов (у игрока 1 останется {} жетонов)'.format(offer, Constants.endowment - offer))


def make_primary_field(num):
    if Constants.language == 1:
        if num == 0:
            label_text = "Choose how many tokens you want to offer to player 2"
        elif num == 1:
            label_text = "Choose how many tokens you want to offer to player 2 if player 2 chooses game 1"
        else:
            label_text = "Choose how many tokens you want to offer to player 2 if player 2 chooses game 2"
    else:
        if num == 0:
            label_text = "Выберете, сколько жетонов Вы хотите предложить игроку 2"
        elif num == 1:
            label_text = "Выберете, сколько жетонов Вы хотите предложить игроку 2 в случае, если игрок 2 выберет игру 1"
        else:
            label_text = "Выберете, сколько жетонов Вы хотите предложить игроку 2 в случае, если игрок 2 выберет игру 2"
    return models.IntegerField(
        choices=Constants.offer_options_in_words,
        widget=widgets.RadioSelect,
        label=label_text
    )


def make_game_field():
    if Constants.language == 1:
        return models.IntegerField(
            choices=[[1, 'Game 1'], [2, 'Game 2']],
            widget=widgets.RadioSelectHorizontal,
            label='Choose which game to play'
        )
    else:
        return models.IntegerField(
            choices=[[1, 'Игра 1'], [2, 'Игра 2']],
            widget=widgets.RadioSelectHorizontal,
            label='Выберете, какую игру дальше играть'
        )


class Group(BaseGroup):
    amount_offered = make_primary_field(0)
    amount_offered_1 = make_primary_field(1)
    amount_offered_2 = make_primary_field(2)

    response_0 = make_field(0)
    response_10 = make_field(10)
    response_20 = make_field(20)
    response_30 = make_field(30)
    response_40 = make_field(40)
    response_50 = make_field(50)
    response_60 = make_field(60)
    response_70 = make_field(70)
    response_80 = make_field(80)
    response_90 = make_field(90)
    response_100 = make_field(100)

    game_played = make_game_field()

    def set_payoffs(self):
        p1, p2 = self.get_players()

        if self.round_number == 1:
            p1.participant.vars['amount_offered_G1'] = self.amount_offered
            p1.participant.vars['offer_accepted_G1'] = getattr(self, 'response_{}'.format(self.amount_offered))
            p2.participant.vars['amount_offered_G1'] = self.amount_offered
            p2.participant.vars['offer_accepted_G1'] = p1.participant.vars['offer_accepted_G1']
            if p1.participant.vars['offer_accepted_G1']:
                p1.participant.vars['payoff_G1'] = Constants.endowment - self.amount_offered
                p2.participant.vars['payoff_G1'] = self.amount_offered
            else:
                p1.participant.vars['payoff_G1'] = Constants.payoff_if_rejected
                p2.participant.vars['payoff_G1'] = Constants.payoff_if_rejected
        elif self.round_number == 2:
            p1.participant.vars['amount_offered_G2'] = self.amount_offered
            p2.participant.vars['amount_offered_G2'] = self.amount_offered
            p1.participant.vars['payoff_G2'] = Constants.endowment - self.amount_offered
            p2.participant.vars['payoff_G2'] = self.amount_offered
        else:
            p1.game_chosen = self.game_played
            p2.game_chosen = self.game_played
            p1.amount_offered_G3_G1 = self.amount_offered_1
            p1.amount_offered_G3_G2 = self.amount_offered_2
            p2.amount_offered_G3_G1 = self.amount_offered_1
            p2.amount_offered_G3_G2 = self.amount_offered_2
            if self.game_played == 1:
                p1.offer_accepted_G3_G1 = getattr(self, 'response_{}'.format(self.amount_offered_1))
                p2.offer_accepted_G3_G1 = p1.offer_accepted_G3_G1
                if p1.offer_accepted_G3_G1:
                    p1.payoff_G3 = Constants.endowment - self.amount_offered_1
                    p2.payoff_G3 = self.amount_offered_1
                else:
                    p1.payoff_G3 = Constants.payoff_if_rejected
                    p2.payoff_G3 = Constants.payoff_if_rejected
            else:
                p1.payoff_G3 = Constants.endowment - self.amount_offered_2
                p2.payoff_G3 = self.amount_offered_2
            for p in self.get_players():
                p.amount_offered_G1 = p.participant.vars['amount_offered_G1']
                p.offer_accepted_G1 = p.participant.vars['offer_accepted_G1']
                p.amount_offered_G2 = p.participant.vars['amount_offered_G2']
                p.payoff_G1 = p.participant.vars['payoff_G1']
                p.payoff_G2 = p.participant.vars['payoff_G2']
                p.set_final_payoff()


def make_quiz_question(num, model_format, choices_num):
    if model_format == 'String' and choices_num == 3:
        return models.StringField(
            choices=[Constants.quiz_file_list[num-1]['choice1'], Constants.quiz_file_list[num-1]['choice2'],
                     Constants.quiz_file_list[num-1]['choice3']],
            label=Constants.quiz_file_list[num-1]['question'],
            widget=widgets.RadioSelectHorizontal
        )
    elif model_format == 'String' and choices_num == 6:
        return models.StringField(
            choices=[Constants.quiz_file_list[num - 1]['choice1'], Constants.quiz_file_list[num - 1]['choice2'],
                     Constants.quiz_file_list[num - 1]['choice3'], Constants.quiz_file_list[num - 1]['choice4'],
                     Constants.quiz_file_list[num - 1]['choice5'], Constants.quiz_file_list[num - 1]['choice6']],
            label=Constants.quiz_file_list[num - 1]['question'],
            widget=widgets.RadioSelectHorizontal
        )
    elif model_format == 'Integer':
        return models.IntegerField(
            label=Constants.quiz_file_list[num - 1]['question']
        )
    else:
        return []


def make_survey1_question_str(lnum, num):
    if lnum == 1:
        return models.LongStringField(
            label=Constants.survey1_question_1[num-1]
        )
    elif lnum == 3:
        return models.LongStringField(
            label=Constants.survey1_question_3[num - 1]
        )
    elif lnum == 4:
        return models.LongStringField(
            blank=True,
            label=Constants.survey1_question_4[num - 1]
        )
    else:
        return []


def make_survey1_question(num):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
        label=Constants.survey1_question_2[num-1]
    )


def make_survey2_urn(num):
    return models.IntegerField(
        choices=[[1, Constants.choice1_RiskyUrns], [2, str(Constants.choice2_RiskyUrns).format(num)]],
        widget=widgets.RadioSelectHorizontal,
        verbose_name=Constants.label_RiskyUrns
    )


def make_survey_personal(num):
    return models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
        label=Constants.SurveyPersonal_question[num-1])


class Player(BasePlayer):
    amount_offered_G1 = models.IntegerField()
    amount_offered_G2 = models.IntegerField()
    amount_offered_G3_G1 = models.IntegerField()
    amount_offered_G3_G2 = models.IntegerField()
    offer_accepted_G1 = models.BooleanField()
    offer_accepted_G3_G1 = models.BooleanField()
    game_chosen = models.IntegerField()
    payoff_G1 = models.IntegerField()
    payoff_G2 = models.IntegerField()
    payoff_G3 = models.IntegerField()
    payoff_game = models.IntegerField()
    payoff_text = models.StringField()

    quiz_questions_1 = make_quiz_question(1, 'String', 3)
    quiz_questions_2 = make_quiz_question(2, 'String', 3)
    quiz_questions_3 = make_quiz_question(3, 'Integer', 0)
    quiz_questions_4 = make_quiz_question(4, 'Integer', 0)
    quiz_questions_5 = make_quiz_question(5, 'Integer', 0)
    quiz_questions_6 = make_quiz_question(6, 'String', 3)
    quiz_questions_7 = make_quiz_question(7, 'String', 3)
    quiz_questions_8 = make_quiz_question(8, 'Integer', 0)
    quiz_questions_9 = make_quiz_question(9, 'String', 6)
    quiz_questions_10 = make_quiz_question(10, 'String', 3)

    def check_correct(self, p):
        answer = str(getattr(self, 'quiz_questions_{}'.format(p)))
        return answer == Constants.quiz_file_list[p-1]['solution']

    def number_correct(self):
        n = 0
        for p in Constants.quiz_questions_range:
            if self.check_correct(p):
                n = n + 1
        return n

    def set_final_payoff(self):
        self.payoff_game = random.choice([1, 2, 3])
        if self.payoff_game == 1:
            self.payoff = Constants.show_up + self.payoff_G1 * Constants.rate
        elif self.payoff_game == 2:
            self.payoff = Constants.show_up + self.payoff_G2 * Constants.rate
        else:
            self.payoff = Constants.show_up + self.payoff_G3 * Constants.rate
        self.payoff_text = add_currency(Constants.currency_used, int(self.payoff))

    survey1_questions_1_1 = make_survey1_question_str(1, 1)
    survey1_questions_1_2 = make_survey1_question_str(1, 2)
    survey1_questions_1_3 = make_survey1_question_str(1, 3)

    survey1_questions_2_1_response_0 = make_field(0)
    survey1_questions_2_1_response_10 = make_field(10)
    survey1_questions_2_1_response_20 = make_field(20)
    survey1_questions_2_1_response_30 = make_field(30)
    survey1_questions_2_1_response_40 = make_field(40)
    survey1_questions_2_1_response_50 = make_field(50)
    survey1_questions_2_1_response_60 = make_field(60)
    survey1_questions_2_1_response_70 = make_field(70)
    survey1_questions_2_1_response_80 = make_field(80)
    survey1_questions_2_1_response_90 = make_field(90)
    survey1_questions_2_1_response_100 = make_field(100)
    survey1_questions_2_2_amount_offered = make_primary_field(0)
    survey1_questions_3_1_game_played = make_game_field()
    survey1_questions_3_2_amount_offered = make_primary_field(0)
    survey1_questions_4_1_response_0 = make_field(0)
    survey1_questions_4_1_response_10 = make_field(10)
    survey1_questions_4_1_response_20 = make_field(20)
    survey1_questions_4_1_response_30 = make_field(30)
    survey1_questions_4_1_response_40 = make_field(40)
    survey1_questions_4_1_response_50 = make_field(50)
    survey1_questions_4_1_response_60 = make_field(60)
    survey1_questions_4_1_response_70 = make_field(70)
    survey1_questions_4_1_response_80 = make_field(80)
    survey1_questions_4_1_response_90 = make_field(90)
    survey1_questions_4_1_response_100 = make_field(100)
    survey1_questions_4_2_amount_offered_1 = make_primary_field(1)
    survey1_questions_4_2_amount_offered_2 = make_primary_field(2)

    survey1_questions_5_1 = make_survey1_question(1)
    survey1_questions_5_2 = make_survey1_question(2)
    survey1_questions_5_3 = make_survey1_question(3)
    survey1_questions_5_4 = make_survey1_question(4)
    survey1_questions_5_5 = make_survey1_question(5)
    survey1_questions_5_6 = make_survey1_question(6)
    survey1_questions_5_7 = make_survey1_question(7)
    survey1_questions_5_8 = make_survey1_question(8)
    survey1_questions_5_9 = make_survey1_question(9)
    survey1_questions_5_10 = make_survey1_question(10)
    survey1_questions_5_11 = make_survey1_question(11)
    survey1_questions_5_12 = make_survey1_question(12)
    survey1_questions_5_13 = make_survey1_question(13)
    survey1_questions_5_14 = make_survey1_question(14)
    survey1_questions_5_15 = make_survey1_question(15)
    survey1_questions_5_16 = make_survey1_question(16)
    survey1_questions_5_17 = make_survey1_question(17)
    survey1_questions_5_18 = make_survey1_question(18)
    survey1_questions_5_19 = make_survey1_question(19)
    survey1_questions_5_20 = make_survey1_question(20)
    survey1_questions_5_21 = make_survey1_question(21)
    survey1_questions_5_22 = make_survey1_question(22)
    survey1_questions_5_23 = make_survey1_question(23)
    survey1_questions_5_24 = make_survey1_question(24)
    survey1_questions_5_25 = make_survey1_question(25)
    survey1_questions_5_26 = make_survey1_question(26)
    survey1_questions_5_27 = make_survey1_question(27)
    survey1_questions_5_28 = make_survey1_question(28)

    survey1_questions_6_1 = make_survey1_question_str(3, 1)
    survey1_questions_6_2 = make_survey1_question_str(3, 2)
    survey1_questions_6_3 = make_survey1_question_str(3, 3)
    survey1_questions_6_4 = make_survey1_question_str(3, 4)

    survey1_questions_7 = make_survey1_question_str(4, 1)

    order_questions = models.StringField()

    survey2_question_RiskyProject1 = models.IntegerField(
        choices=Constants.invest_options_RiskyProject1,
        label=Constants.question_RiskyProject)
    survey2_RiskyProject1_earned = models.IntegerField()
    survey2_RiskyProject1_left = models.IntegerField()
    survey2_RiskyProject1_success = models.BooleanField()
    survey2_RiskyProject1_payoff = models.IntegerField()

    survey2_question_RiskyProject2 = models.IntegerField(
        choices=Constants.invest_options_RiskyProject2,
        label=Constants.question_RiskyProject)
    survey2_RiskyProject2_earned = models.IntegerField()
    survey2_RiskyProject2_left = models.IntegerField()
    survey2_RiskyProject2_success = models.BooleanField()
    survey2_RiskyProject2_payoff = models.IntegerField()

    survey2_RiskyUrns1_0 = make_survey2_urn(Constants.Options_RiskyUrns1[0])
    survey2_RiskyUrns1_10 = make_survey2_urn(Constants.Options_RiskyUrns1[1])
    survey2_RiskyUrns1_20 = make_survey2_urn(Constants.Options_RiskyUrns1[2])
    survey2_RiskyUrns1_30 = make_survey2_urn(Constants.Options_RiskyUrns1[3])
    survey2_RiskyUrns1_40 = make_survey2_urn(Constants.Options_RiskyUrns1[4])
    survey2_RiskyUrns1_50 = make_survey2_urn(Constants.Options_RiskyUrns1[5])
    survey2_RiskyUrns1_60 = make_survey2_urn(Constants.Options_RiskyUrns1[6])
    survey2_RiskyUrns1_70 = make_survey2_urn(Constants.Options_RiskyUrns1[7])
    survey2_RiskyUrns1_80 = make_survey2_urn(Constants.Options_RiskyUrns1[8])
    survey2_RiskyUrns1_90 = make_survey2_urn(Constants.Options_RiskyUrns1[9])
    survey2_RiskyUrns1_100 = make_survey2_urn(Constants.Options_RiskyUrns1[10])
    survey2_RiskyUrns1_110 = make_survey2_urn(Constants.Options_RiskyUrns1[11])
    survey2_RiskyUrns1_120 = make_survey2_urn(Constants.Options_RiskyUrns1[12])
    survey2_RiskyUrns1_130 = make_survey2_urn(Constants.Options_RiskyUrns1[13])
    survey2_RiskyUrns1_140 = make_survey2_urn(Constants.Options_RiskyUrns1[14])
    survey2_RiskyUrns1_150 = make_survey2_urn(Constants.Options_RiskyUrns1[15])
    survey2_RiskyUrns1_sure = models.StringField()
    survey2_RiskyUrns1_choice = models.StringField()
    survey2_RiskyUrns1_choice_num = models.IntegerField()
    survey2_RiskyUrns1_payoff = models.IntegerField()

    survey2_RiskyUrns2_0 = make_survey2_urn(Constants.Options_RiskyUrns2[0])
    survey2_RiskyUrns2_10 = make_survey2_urn(Constants.Options_RiskyUrns2[1])
    survey2_RiskyUrns2_20 = make_survey2_urn(Constants.Options_RiskyUrns2[2])
    survey2_RiskyUrns2_30 = make_survey2_urn(Constants.Options_RiskyUrns2[3])
    survey2_RiskyUrns2_40 = make_survey2_urn(Constants.Options_RiskyUrns2[4])
    survey2_RiskyUrns2_50 = make_survey2_urn(Constants.Options_RiskyUrns2[5])
    survey2_RiskyUrns2_60 = make_survey2_urn(Constants.Options_RiskyUrns2[6])
    survey2_RiskyUrns2_70 = make_survey2_urn(Constants.Options_RiskyUrns2[7])
    survey2_RiskyUrns2_80 = make_survey2_urn(Constants.Options_RiskyUrns2[8])
    survey2_RiskyUrns2_90 = make_survey2_urn(Constants.Options_RiskyUrns2[9])
    survey2_RiskyUrns2_100 = make_survey2_urn(Constants.Options_RiskyUrns2[10])
    survey2_RiskyUrns2_sure = models.StringField()
    survey2_RiskyUrns2_choice = models.StringField()
    survey2_RiskyUrns2_choice_num = models.IntegerField()
    survey2_RiskyUrns2_payoff = models.IntegerField()

    survey2_payment_question_in_order_for_subject = models.IntegerField()
    survey2_payment_question_in_internal_order = models.IntegerField()
    survey2_payoff = models.IntegerField()
    survey2_payoff_text = models.StringField()

    def get_payoff_survey2(self):
        num = self.participant.vars['order_questions'][self.participant.vars['question_number']]
        if num == 1 or num == 2:
            if num == 1:
                invested = self.survey2_question_RiskyProject1
            else:
                invested = self.survey2_question_RiskyProject2
            left = Constants.endowment_RiskyProject[num-1] - invested
            success = random.uniform(0, 100) < Constants.prob_success_RiskyProject[num-1]
            if success:
                earned = Constants.return_RiskyProject[num-1] * invested
            else:
                earned = 0
            if num == 1:
                self.survey2_RiskyProject1_left = left
                self.survey2_RiskyProject1_success = success
                self.survey2_RiskyProject1_earned = earned
                self.survey2_RiskyProject1_payoff = left + earned
            else:
                self.survey2_RiskyProject2_left = left
                self.survey2_RiskyProject2_success = success
                self.survey2_RiskyProject2_earned = earned
                self.survey2_RiskyProject2_payoff = left + earned
        else:
            if num == 3:
                sure = random.choice(Constants.Options_RiskyUrns1)
            else:
                sure = random.choice(Constants.Options_RiskyUrns2)
            sure_text = str(Constants.choice2_RiskyUrns).format(sure)
            choice_num = getattr(self, 'survey2_RiskyUrns{}_{}'.format(num-2, sure))
            if choice_num == 1:
                choice = Constants.choice1_RiskyUrns
                ball = random.randint(1, Constants.LoseBalls_RiskyUrns[num-3] + Constants.WinBalls_RiskyUrns[num-3])
                if ball > Constants.LoseBalls_RiskyUrns[num-3]:
                    pay_off = Constants.WinPayoff_RiskyUrns[num-3]
                else:
                    pay_off = 0
            else:
                choice = sure_text
                pay_off = sure
            if num == 3:
                self.survey2_RiskyUrns1_sure = sure_text
                self.survey2_RiskyUrns1_choice_num = choice_num
                self.survey2_RiskyUrns1_choice = choice
                self.survey2_RiskyUrns1_payoff = pay_off
            else:
                self.survey2_RiskyUrns2_sure = sure_text
                self.survey2_RiskyUrns2_choice_num = choice_num
                self.survey2_RiskyUrns2_choice = choice
                self.survey2_RiskyUrns2_payoff = pay_off
        if self.participant.vars['question_number'] == Constants.survey2_questions_count - 1:
            self.survey2_payment_question_in_order_for_subject = random.choice(Constants.survey2_questions_range)
            self.survey2_payment_question_in_internal_order = \
                self.participant.vars['order_questions'][self.survey2_payment_question_in_order_for_subject - 1]
            if self.survey2_payment_question_in_internal_order == 1:
                self.survey2_payoff = self.survey2_RiskyProject1_payoff
            elif self.survey2_payment_question_in_internal_order == 2:
                self.survey2_payoff = self.survey2_RiskyProject2_payoff
            elif self.survey2_payment_question_in_internal_order == 3:
                self.survey2_payoff = self.survey2_RiskyUrns1_payoff
            else:
                self.survey2_payoff = self.survey2_RiskyUrns2_payoff
            self.survey2_payoff = self.survey2_payoff * Constants.rate_survey
            self.payoff = self.payoff + self.survey2_payoff
            self.survey2_payoff_text = add_currency(Constants.currency_used, int(self.survey2_payoff))

    Prisoner_decision = models.StringField(
        choices=[Constants.Prisoner_cooperate, Constants.Prisoner_defect],
        widget=widgets.RadioSelect
    )
    Prisoner_payoff = models.IntegerField()
    survey3_payment_question = models.IntegerField()
    survey3_payoff = models.IntegerField()
    survey3_payoff_text = models.StringField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_prisoner_payoff(self):
        payoff_matrix = {
            Constants.Prisoner_cooperate:
                {
                    Constants.Prisoner_cooperate: Constants.Prisoner_both_cooperate_payoff[self.round_number-4],
                    Constants.Prisoner_defect: Constants.Prisoner_betrayed_payoff[self.round_number - 4]
                },
            Constants.Prisoner_defect:
                {
                    Constants.Prisoner_cooperate: Constants.Prisoner_betray_payoff[self.round_number - 4],
                    Constants.Prisoner_defect: Constants.Prisoner_both_defect_payoff[self.round_number-4]
                }
        }
        self.Prisoner_payoff = payoff_matrix[self.Prisoner_decision][self.other_player().Prisoner_decision]
        self.participant.vars['prisoner_payoffs'].append(self.Prisoner_payoff)

    def set_final_prisoner_payoff(self):
        self.survey3_payment_question = random.randint(1, len(self.participant.vars['prisoner_payoffs']))
        self.survey3_payoff = int(self.participant.vars['prisoner_payoffs'][self.survey3_payment_question - 1])
        self.payoff = self.payoff + self.survey3_payoff
        self.survey3_payoff_text = add_currency(Constants.currency_used, int(self.survey3_payoff))

    survey_personal_questions_1 = models.StringField(
        choices=[Constants.SurveyPersonal_question[0][1], Constants.SurveyPersonal_question[0][2],
                 Constants.SurveyPersonal_question[0][3]],
        widget=widgets.RadioSelectHorizontal,
        label=Constants.SurveyPersonal_question[0][0])
    survey_personal_questions_2 = models.IntegerField(
        min=0, max=150,
        label=Constants.SurveyPersonal_question[1])
    survey_personal_questions_3 = models.StringField(
        label=Constants.SurveyPersonal_question[2])
    survey_personal_questions_4 = models.IntegerField(
        min=0, max=50,
        label=Constants.SurveyPersonal_question[3])
    survey_personal_questions_5 = make_survey_personal(5)
    survey_personal_questions_6 = make_survey_personal(6)
    survey_personal_questions_7 = make_survey_personal(7)
    survey_personal_questions_8 = make_survey_personal(8)
    survey_personal_questions_9 = make_survey_personal(9)
    survey_personal_questions_10 = make_survey_personal(10)
    survey_personal_questions_11 = make_survey_personal(11)
    survey_personal_questions_12 = make_survey_personal(12)
    survey_personal_questions_13 = make_survey_personal(13)
    survey_personal_questions_14 = make_survey_personal(14)
    survey_personal_questions_15 = make_survey_personal(15)
    survey_personal_questions_16 = make_survey_personal(16)
    survey_personal_questions_17 = make_survey_personal(17)



