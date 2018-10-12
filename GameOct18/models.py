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
        return str(num) + ' рублей'


class Constants(BaseConstants):
    name_in_url = 'GameOct18'
    players_per_group = 2
    num_rounds = 6
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
    elif currency_used == 1:
        show_up = 3
        rate = 0.2
    else:
        show_up = 200
        rate = 10
    show_up_text = add_currency(currency_used, show_up)
    rate_text = add_currency(currency_used, rate)

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

    endowment_RiskyProject1 = 200
    prob_success_RiskyProject1 = 50
    return_RiskyProject1 = 2
    endowment_RiskyProject2 = 100
    prob_success_RiskyProject2 = 35
    return_RiskyProject2 = 3

    LoseBalls_RiskyUrns1 = 15
    WinBalls_RiskyUrns1 = 15
    WinPayoff_RiskyUrns1 = 150
    Step_RiskyUrns1 = 10
    Options_RiskyUrns1 = range(0, WinPayoff_RiskyUrns1 + Step_RiskyUrns1, Step_RiskyUrns1)
    LoseBalls_RiskyUrns2 = 10
    WinBalls_RiskyUrns2 = 10
    WinPayoff_RiskyUrns2 = 100
    Step_RiskyUrns2 = 10
    Options_RiskyUrns2 = range(0, WinPayoff_RiskyUrns2 + Step_RiskyUrns2, Step_RiskyUrns2)

    Prisoner_both_cooperate_payoff = [95, 80]
    Prisoner_both_defect_payoff = [62, 50]
    Prisoner_betrayed_payoff = [31, 24]
    Prisoner_betray_payoff = [120, 100]
    Prisoner_cooperate = 'A1'
    Prisoner_defect = 'A2'

    SurveyPersonal_number = 4

    quiz_question = []
    quiz_explanation = []
    survey1_question_1 = []
    survey1_question_2 = []
    survey1_question_3 = []
    SurveyPersonal_question = []
    if language == 1:
        quiz_question.append('Is it possible that your role (player 1 / player 2) will be changed '
                             'during the experiment?')
        quiz_question.append('How likely is it that you get the same partner in all three games?')
        quiz_question.append('How many tokens will you get in a game if an offer is rejected?')
        quiz_question.append('What is the maximum number of tokens you can get during the experiment '
                             'to exchange for the actual payment?')
        quiz_question.append('What is the minimum number of tokens you can get during the experiment '
                             'to exchange for the actual payment?')
        quiz_question.append('In game 1, will player 2 see the offer before or after she makes her move in the game?')
        quiz_question.append('In game 2, does player 2 have to do anything?')
        quiz_question.append('How many decisions player 1 has to make in game 3?')
        quiz_question.append('How many decisions player 2 has to make in game 3?')
        quiz_question.append('In game 3, can player 1 make an offer conditional on player 2\'s choice of the game?')
        quiz_answer_1 = ['Yes', 'No', 'I do not know']
        quiz_answer_2 = ['Your partner is the same in all three games',
                         'Your partner is chosen randomly at the beginning of each game', 'I do not know']
        quiz_answer_6 = ['Before', 'After', 'I do not know']
        quiz_answer_7 = ['Yes', 'No', 'I do not know']
        quiz_answer_9 = ['1', '2', '3', '1 or 2 depending on the first decision',
                         '1 or 12 depending on the first decision', 'I do not know']
        quiz_answer_10 = ['Yes', 'No', 'I do not know']
        quiz_explanation.append('Your role remains the same throughout the whole experiment')
        quiz_explanation.append('Most likely, you will get a new partner for each game')
        quiz_explanation.append(
            'The answer does not depend on your role, both player 1 and player 2 get 0 tokens in case of rejection')
        quiz_explanation.append(
            'You get paid from only one randomly chosen game, at most you can get 100 tokens from one game')
        quiz_explanation.append('The minimum payment in one game is 0 tokens')
        quiz_explanation.append('Player 2 has to make 11 conditional decisions, for each of 11 possible offers')
        quiz_explanation.append('Both players\' payoffs are fully determined by the proposer\'s actions')
        quiz_explanation.append(
            'First, how much to offer if player 2 chose game 1. Second, how much to offer is player 2 chose game 2')
        quiz_explanation.append(
            'If player 2 chose game 1, he has to make 11 conditional decisions, for each of 11 possible offers')
        quiz_explanation.append('The fact that player 1 makes two choices means exactly that')
        survey1_question_1.append('Explain your logic for game 1')
        survey1_question_1.append('Explain your logic for game 2')
        survey1_question_1.append('Explain your logic for game 3')
        survey1_question_2.append(
            'Player 2 should always accept any offer, even 0 tokens. Any other behavior is just stupid.')
        survey1_question_2.append(
            'Player 2 should always accept any positive offer, though '
            'she might reasonably decline the offer of 0 tokens. Any other behavior is just stupid.')
        survey1_question_2.append('Player 2 would normally reject low offers. '
                                  'Most people accept an offer of at least 30 tokens.')
        survey1_question_2.append('Player 2 should reject anything below 50 tokens.')
        survey1_question_2.append('Player 1 should give 50 tokens in any game, aiming for a fair division.')
        survey1_question_2.append(
            'Player 1 has moral right to offer 0 tokens in game 2. There is no shame in doing it.')
        survey1_question_2.append('In game 3, player 1 should give more to player 2 who chose game 1.')
        survey1_question_2.append('In game 3, player 1 should give more to player 2 who chose game 2.')
        survey1_question_2.append('In game 3, the choice of game 1 is a sign of non-cooperative behavior.')
        survey1_question_2.append(
            'Player 1 should give more to player 2 in game 1 if player 2 chose to play that game (as in game 3), '
            'as this indicates that player 2 would more likely reject low offers.')
        survey1_question_2.append(
            'Player 1 should give less to player 2 in game 1 if player 2 chose to play that game (as in game 3), '
            'to punish player 2.')
        survey1_question_2.append(
            'Player 1 should give more to player 2 in game 2 if player 2 chose to play that game (as in game 3), '
            'to reward player 2 for her cooperative behavior.')
        survey1_question_2.append(
            'Player 1 should give less to player 2 in game 2 if player 2 chose to play that game (as in game 3), '
            'as this indicates that player 2 understands that the power lies with player 1 in this experiment and '
            'player 1 has moral right to offer very little (or even nothing).')
        survey1_question_2.append('Player 2 should choose game 1 because it makes no sense to voluntarily '
                                  'giving up on the opportunity to reject offers.')
        survey1_question_2.append(
            'Player 2 should choose game 1 because she would receive a higher offer by using this strategy.')
        survey1_question_2.append(
            'Player 2 should choose game 2 because he would receive a higher offer by using this strategy.')
        survey1_question_2.append('Player 2 should choose game 2 to signal her trust to player 1.')
        survey1_question_2.append(
            'Player 2 should choose game 2 because it makes no sense to reject offers and everybody understand it.')
        survey1_question_2.append(
            'Player 2 should be more agreeable (accept more offers) in game 1 if he chose to play that game.')
        survey1_question_2.append(
            'Player 2 should be less agreeable (accept less offers) in game 1 if he chose to play that game.')
        survey1_question_2.append(
            'Player 2 should be more agreeable (accept more offers) in game 1 if she chose to play that game '
            'because she already have exercised some control over the situation.')
        survey1_question_2.append(
            'Player 2 should be less agreeable (accept less offers) in game 1 if she chose to play that game '
            'because by choosing game 1 she warned player 1 of her intent to reject low offers.')
        survey1_question_2.append('Player 2 should expect to get more in game 3 than in game 1.')
        survey1_question_2.append('Player 2 should expect to get less in game 3 than in game 1.')
        survey1_question_2.append('Player 2 should expect to get more in game 3 than in game 2.')
        survey1_question_2.append('Player 2 should expect to get less in game 3 than in game 2.')
        survey1_question_2.append(
            'When playing game 1, it does not make any difference for player 1 whether player 2 chose to play '
            'that game (as in game 3) or it was the computer\'s choice (as in game 1).')
        survey1_question_2.append(
            'When playing game 2, it does not make any difference for player 1 whether player 2 chose to play '
            'that game (as in game 3) or it was the computer\'s choice (as in game 2).')
        survey1_question_3.append(
            'Any amount player 1 offers to player 2 is doubled in size: if player 1 gives x tokens out of 100 tokens '
            'to player 2 and the offer is accepted, then player 2 gets 2*x tokens, while player 1 gets 100-x tokens.')
        survey1_question_3.append(
            'Any amount player 1 offers to player 2 is halved: if player 1 gives x tokens out of 100 tokens '
            'to player 2 and the offer is accepted, then player 2 gets x/2 tokens, while player 1 gets 100-x tokens.')
        survey1_question_3.append(
            'In game 3, when player 2 chooses game 1 player 1 gets 100 tokens to divide (same as before). '
            'However, when player 2 chooses game 2 player 1 gets 200 tokens to divide.')
        survey1_question_3.append(
            'In game 3, when player 2 chooses game 1 player 1 gets 200 tokens to divide; '
            'when player 2 chooses game 2 player 1 gets 100 tokens to divide.')
        survey1_question_4 = ['Type in any comments you have about the experiment.']
        question_RiskyProject1 = 'Please choose how many tokens you want to invest in the risky project. ' \
                                 'Note that you can pick any number between 0 and ' +\
                                 str(endowment_RiskyProject1) + ', including 0 or ' + \
                                 str(endowment_RiskyProject1)
        question_RiskyProject2 = 'Please choose how many tokens you want to invest in the risky project. ' \
                                 'Note that you can pick any number between 0 and ' +\
                                 str(endowment_RiskyProject2) + ', including 0 or ' + \
                                 str(endowment_RiskyProject2)
        label_RiskyUrns = 'Choose one option'
        choice1_RiskyUrns = 'Urn gamble'
        choice2_RiskyUrns = '{} tokens'
        SurveyPersonal_question.append(['What is your gender?', 'Male', 'Female', 'Other'])
        SurveyPersonal_question.append('What is your age?')
        SurveyPersonal_question.append('What is your main field of study (your major)?')
        SurveyPersonal_question.append('What is(are) your native language(s)?')
        SurveyPersonal_question.append('How many siblings do you have?')
        preambul = 'How well does the following statement describe you as a person ' \
                   '(0 - does not describe me at all; 10 - describes me perfectly)? '
        SurveyPersonal_question.append(preambul + '\"Winning a debate matters less to you than making sure '
                                                  'no one gets upset.\"')
        SurveyPersonal_question.append(preambul + '\"You do not mind being at the center of attention.\"')
        SurveyPersonal_question.append(preambul + '\"If someone does not respond to your e-mail quickly, you start '
                                                  'worrying if you said something wrong.\"')
        SurveyPersonal_question.append(preambul + '\"You do not let other people influence your actions\".')
        SurveyPersonal_question.append(preambul + '\"If you had a business, you would find it very difficult to fire '
                                                  'loyal but underperforming employees.\"')
        SurveyPersonal_question.append(preambul + '\"Logic is usually more important than heart when it comes '
                                                  'to making important decisions.\"')
        SurveyPersonal_question.append(preambul + '\"Keeping your options open is more important than having '
                                                  'a to-do list.\"')
        SurveyPersonal_question.append(preambul + '\"You think that everyone\'s views should be respected regardless '
                                                  'of whether they are supported by facts or not.\"')
        SurveyPersonal_question.append(preambul + '\"You feel more energetic after spending time talking to '
                                                  'somebody.\"')
        SurveyPersonal_question.append(preambul + '\"You believe that it is more rewarding to be respected '
                                                  'by others than to be powerful.\"')
        SurveyPersonal_question.append(
            'Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. '
            'The top of the ladder represents the best possible life for you and the bottom of the ladder '
            'represents the worst possible life for you. On which step of the ladder would you say you '
            'personally feel you stand at this time?')
        SurveyPersonal_question.append(
            'Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. '
            'The top of the ladder represents the best possible life for you and the bottom of the ladder '
            'represents the worst possible life for you. Just your best guess, on which step fo you think '
            'you will stand in the future, say about five years from now?')

    else:
        quiz_question.append('Возможно ли, что Ваша роль (игрок 1 / игрок 2) изменится в течение эксперимента?')
        quiz_question.append(
            'Какова вероятность того, что у Вас будет один и тот же участник эксперимента '
            'в качестве партнёра во всей трёх играх?')
        quiz_question.append('Сколько жетонов Вы получите, если предложение игрока 1 будет отклонено?')
        quiz_question.append('Какое максимальное количество жетонов Вы можете получить для оплаты в '
                             'течение эксперимента?')
        quiz_question.append('Какое минимальное количество жетонов Вы можете получить для оплаты в '
                             'течение эксперимента?')
        quiz_question.append('В игре 1 игрок 2 видит предложение игрока 1 до или после того, как сделает выбор?')
        quiz_question.append('Должен ли что-то делать игрок 2 в игре 2?')
        quiz_question.append('Сколько решений должен принять игрок 1 в игре 3?')
        quiz_question.append('Сколько решений должен принять игрок 2 в игре 3?')
        quiz_question.append('Во время игры 3 может ли игрок 1 предложить разное количество жетонов игроку 2, '
                             'в зависимости от того, какую игру выбрал игрок 2?')
        quiz_answer_1 = ['Да', 'Нет', 'Не знаю']
        quiz_answer_2 = ['Ваш партнёр не меняется',
                         'Ваш партнёр будет выбираться случайным образом перед каждой игрой', 'Не знаю']
        quiz_answer_6 = ['До', 'После', 'Не знаю']
        quiz_answer_7 = ['Да', 'Нет', 'Не знаю']
        quiz_answer_9 = ['1', '2', '3', '1 или 2 в зависимости от первого решения',
                         '1 или 12 в зависимости от первого решения', 'Не знаю']
        quiz_answer_10 = ['Да', 'Нет', 'Не знаю']
        quiz_explanation.append('Ваша роль останется неизменной в течение всего эксперимента')
        quiz_explanation.append('Скорее всего у Вас будет новый партнёр в каждой следующей игре')
        quiz_explanation.append(
            'Ответ не зависит от Вашей роли, оба игрока получают 0 жетонов в случае отказа от предложения')
        quiz_explanation.append(
            'Только одна из трёх игр будет случайно выбрана для оплаты, а в каждой игре можно получить '
            'самое большее 100 жетонов')
        quiz_explanation.append('В каждой игре минимальная выплата - 0 жетонов')
        quiz_explanation.append('Игроку 2 предстоит сделать 11 выборов, для всех возможных решений игрока 1')
        quiz_explanation.append('Что получат оба игрока - решать только игроку 1')
        quiz_explanation.append(
            'Во-первых, игрок 1 должен решить сколько предложить игроку 2, если игрок 2 выберет игру 1. '
            'Во-вторых, игрок 1 должен решить сколько предложить игроку 2, если игрок 2 выберет игру 2')
        quiz_explanation.append('Если игрок 2 выбрал игру 2, он должен сделать еще 11 выборов, '
                                'по одному для каждого возможного предложения игрока 1')
        quiz_explanation.append('Тот факт, что игрок 1 делает два выбора, означает ровно это')
        survey1_question_1.append('Объясните Вашу логику в игре 1')
        survey1_question_1.append('Объясните Вашу логику в игре 2')
        survey1_question_1.append('Объясните Вашу логику в игре 3')
        survey1_question_2.append(
            'Игроку 2 следует всегда принимать любое предложение, даже если игрок 1 предложил ему 0 жетонов. '
            'Любое другое поведение просто глупо.')
        survey1_question_2.append(
            'Игроку 2 следует всегда принимать любое предложение, кроме, возможно, того случая, '
            'когда игрок 1 предлагает 0 жетонов. Любое другое поведение просто глупо.')
        survey1_question_2.append('Отвергать маленькие предложения - достаточно типичное поведение для игрока 2. '
                                  'Большинство людей принимают предложения в 30 жетонов и более.')
        survey1_question_2.append('Игроку 2 следует отвергнуть любые предложение, которые меньше 50 жетонов.')
        survey1_question_2.append(
            'Игроку 1 следует предложить 50 жетонов игроку 2, потому что только это является справедливым дележом.')
        survey1_question_2.append(
            'Игрок 1 имеет полное моральное право предложить 0 жетонов в игре 2. Ничего зазорного в этом нет.')
        survey1_question_2.append('В игре 3 игроку 1 следует дать больше игроку 2, если тот выбрал игру 1.')
        survey1_question_2.append('В игре 3 игроку 1 следует дать больше игроку 2, если тот выбрал игру 2.')
        survey1_question_2.append('Выбор игры 1 - признак некооперативного поведения.')
        survey1_question_2.append(
            'Игроку 1 следует дать больше игроку 2 в игре 1 в том случае, если тот выбрал эту игру сам (как в игре 3), '
            'так как такой выбор означает, что игрок 2 откажется от маленьких предложений с большей вероятностью.')
        survey1_question_2.append(
            'Игроку 1 следует дать меньше игроку 2 в игре 1 в том случае, если тот выбрал эту игру сам (как в игре 3), '
            'из-за желания наказать игрока 2.')
        survey1_question_2.append(
            'Игроку 1 следует дать больше игроку 2 в игре 2 в том случае, если тот выбрал эту игру сам (как в игре 3), '
            'чтобы наградить игрока 2 за кооперативное поведение.')
        survey1_question_2.append(
            'Игроку 1 следует дать меньше игроку 2 в игре 2 в том случае, если тот выбрал эту игру сам (как в игре 3), '
            'так как такой выбор означает, что игрок 2 понимает, что в этом эксперименте вся власть на стороне '
            'игрока 1, и игрок 1 имеет полное моральное право предложить очень мало (или даже вообще ничего).')
        survey1_question_2.append('Игроку 2 следует выбрать игру 1, так как добровольно отказаться от возможности '
                                  'отвергнуть преложение - просто глупо.')
        survey1_question_2.append(
            'Игроку 2 следует выбрать игру 1, так как такая стратегия ведёт к более высокому предложению.')
        survey1_question_2.append(
            'Игроку 2 следует выбрать игру 2, так как такая стратегия ведёт к более высокому предложению.')
        survey1_question_2.append(
            'Игроку 2 следует выбрать игру 2, продемонстрировав таким образом игроку 1 своё доверие.')
        survey1_question_2.append(
            'Игроку 2 следует выбрать игру 2, потому что глупо отвергать любые предложения, и все это понимают.')
        survey1_question_2.append(
            'Игроку 2 следует быть более сговорчивым (принимать больше предложений) в игре 1 в том случае, '
            'если он сам выбрал эту игру.')
        survey1_question_2.append(
            'Игроку 2 следует быть менее сговорчивым (принимать меньше предложений) в игре 1 в том случае, '
            'если он сам выбрал эту игру.')
        survey1_question_2.append(
            'Игроку 2 следует быть более сговорчивым (принимать больше предложений) в игре 1 в том случае, '
            'если он сам выбрал эту игру, так как он уже в какой-то мере повлиял на ситуацию.')
        survey1_question_2.append(
            'Игроку 2 следует быть менее сговорчивым (принимать меньше предложений) в игре 1 в том случае, '
            'если он сам выбрал эту игру, так как таким выбором он фактически предупредил игрока 1 о своём '
            'намерении отвергнуть достаточно низкие предложения.')
        survey1_question_2.append('Обычно игрок 2 получает больше в игре 3, чем в игре 1.')
        survey1_question_2.append('Обычно игрок 2 получает меньше в игре 3, чем в игре 1.')
        survey1_question_2.append('Обычно игрок 2 получает больше в игре 3, чем в игре 2.')
        survey1_question_2.append('Обычно игрок 2 получает меньше в игре 3, чем в игре 2.')
        survey1_question_2.append(
            'Когда игрок 1 решает, что предложить игроку 2 в игре 1, для него не важно, была ли эта игра выбрана '
            'игроком 2 (как в игре 3) или же компьютером (как в игре 1).')
        survey1_question_2.append(
            'Когда игрок 1 решает, что предложить игроку 2 в игре 2, для него не важно, была ли эта игра выбрана '
            'игроком 2 (как в игре 3) или же компьютером (как в игре 2).')
        survey1_question_3.append(
            'Любая сумма, предложенная игроком 1 игроку 2, увеличивается в два раза: если игрок 1 предложит x жетонов '
            'из 100 и игрок 2 согласится, игрок 2 получает 2*x жетонов, в то время как игрок 1 получает 100-x жетонов.')
        survey1_question_3.append(
            'Любая сумма, предложенная игроком 1 игроку 2, делится на два: если игрок 1 предложит x жетонов '
            'из 100 и игрок 2 согласится, игрок 2 получает x/2 жетонов, в то время как игрок 1 получает 100-x жетонов.')
        survey1_question_3.append(
            'Когда игрок 2 выбирает игру 1 в игре 3, игрок 1 делит 100 жетонов (как и раньше). '
            'Однако, когда игрок 2 выбирает игру 2, игрок 1 делит 200 жетонов.')
        survey1_question_3.append(
            'Когда игрок 2 выбирает игру 1 в игре 3, игрок 1 делит 200 жетонов; '
            'когда игрок 2 выбирает игру 2, игрок 1 делит 100 жетонов.')
        survey1_question_4 = ['Если у Вас есть дополнительные комментарии, напишите их здесь.']
        question_RiskyProject1 = 'Пожалуйста, выберите, сколько жетонов Вы проинвестируете в рискованный проект. ' \
                                 'Вы можете выбрать любое число от 0 до ' + \
                                 str(endowment_RiskyProject1) + ', включая 0 и ' + \
                                 str(endowment_RiskyProject1)
        question_RiskyProject2 = 'Пожалуйста, выберите, сколько жетонов Вы проинвестируете в рискованный проект. ' \
                                 'Вы можете выбрать любое число от 0 до ' + \
                                 str(endowment_RiskyProject2) + ', включая 0 и ' + \
                                 str(endowment_RiskyProject2)
        label_RiskyUrns = 'Выберите одну опцию'
        choice1_RiskyUrns = 'Лотерея'
        choice2_RiskyUrns = '{} жетонов'
        SurveyPersonal_question.append(['Укажите Ваш пол', 'Мужской', 'Женский', 'Другой'])
        SurveyPersonal_question.append('Сколько Вам полных лет?')
        SurveyPersonal_question.append('Какая у Вас специальность (на каком факультете Вы учитесь?')
        SurveyPersonal_question.append('Какой Ваш родной язык? (укажите все, если их больше одного)')
        SurveyPersonal_question.append('Сколько у Вас братьев и сестер?')
        preambul = 'В какой мере по шкале от 0 до 10 следующее утверждение Вас характеризует ' \
                   '(0 - вообще для Вас не характерно; 10 - идеально Вас описывает)? '
        SurveyPersonal_question.append(preambul + '\"Выиграть спор для меня менее важно, чем не расстроить других\".')
        SurveyPersonal_question.append(preambul + '\"Вы совсем не против оказаться в центре внимания\".')
        SurveyPersonal_question.append(preambul + '\"Если кто-то достаточно быстро не отвечает на Ваши электронные '
                                                  'письма, Вы начинаете волноваться о том, что сказали что-то не то\".')
        SurveyPersonal_question.append(preambul + '\"Вы не даёте другим людям влиять на Ваши действия\".')
        SurveyPersonal_question.append(preambul + '\"Если бы у Вас был бизнес, Вам бы было морально очень сложно '
                                                  'уволить лояльных сотрудников, не справляющихся с работой\".')
        SurveyPersonal_question.append(preambul + '\"Когда надо принять важное решение, разум важнее чувств\".')
        SurveyPersonal_question.append(preambul + '\"Лучше иметь свободу выбора, чем чёткий план действий\".')
        SurveyPersonal_question.append(preambul + '\"Мнение каждого достойно уважения, вне зависимости от того, '
                                                  'подкреплено оно фактами или нет\".')
        SurveyPersonal_question.append(preambul + '\"Вы чувствуйте себя лучше после того, как пообщались '
                                                  'с кем-нибудь\".')
        SurveyPersonal_question.append(preambul + '\"Лучше иметь уважение других, чем власть над ними\".')
        SurveyPersonal_question.append(
            'Представьте себе лестницу, у которой 11 ступенек, пронумерованных от 0 (самая нижняя) до 10. '
            'Самая верхняя ступенька символизирует самую лучшую жизнь, а самая нижняя - самую худшую. '
            'На какой ступеньке Вы сейчас находитесь?')
        SurveyPersonal_question.append(
            'Представьте себе лестницу, у которой 11 ступенек, пронумерованных от 0 (самая нижняя) до 10. '
            'Самая верхняя ступенька символизирует самую лучшую жизнь, а самая нижняя - самую худшую. '
            'Как Вы думаете, на какой ступеньке Вы будете находиться через, скажем, пять лет?')

    if language == 1:
        with open('GameOct18/quiz_en.csv') as quiz_file:
            quiz_file_list = list(csv.DictReader(quiz_file))
    else:
        with open('GameOct18/quiz_ru.csv', encoding='utf-8') as quiz_file:
            quiz_file_list = list(csv.DictReader(quiz_file))

    quiz_correct_answers = [quiz_answer_1[1], quiz_answer_2[1], 0, 100, 0, quiz_answer_6[1], quiz_answer_7[1], 2,
                            quiz_answer_9[4], quiz_answer_10[0]]
    quiz_questions_count = len(quiz_file_list)
    quiz_questions_range = range(1, quiz_questions_count + 1, 1)
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
        print(Constants.quiz_file_list)
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
        min=0, max=Constants.endowment_RiskyProject1,
        label=Constants.question_RiskyProject1)
    survey2_RiskyProject1_earned = models.IntegerField()
    survey2_RiskyProject1_left = models.IntegerField()
    survey2_RiskyProject1_success = models.BooleanField()
    survey2_RiskyProject1_payoff = models.IntegerField()

    survey2_question_RiskyProject2 = models.IntegerField(
        min=0, max=Constants.endowment_RiskyProject2,
        label=Constants.question_RiskyProject2)
    survey2_RiskyProject2_earned = models.IntegerField()
    survey2_RiskyProject2_left = models.IntegerField()
    survey2_RiskyProject2_success = models.BooleanField()
    survey2_RiskyProject2_payoff = models.IntegerField()

    survey2_RiskyUrns1_0 = make_survey2_urn(0)
    survey2_RiskyUrns1_10 = make_survey2_urn(10)
    survey2_RiskyUrns1_20 = make_survey2_urn(20)
    survey2_RiskyUrns1_30 = make_survey2_urn(30)
    survey2_RiskyUrns1_40 = make_survey2_urn(40)
    survey2_RiskyUrns1_50 = make_survey2_urn(50)
    survey2_RiskyUrns1_60 = make_survey2_urn(60)
    survey2_RiskyUrns1_70 = make_survey2_urn(70)
    survey2_RiskyUrns1_80 = make_survey2_urn(80)
    survey2_RiskyUrns1_90 = make_survey2_urn(90)
    survey2_RiskyUrns1_100 = make_survey2_urn(100)
    survey2_RiskyUrns1_110 = make_survey2_urn(110)
    survey2_RiskyUrns1_120 = make_survey2_urn(120)
    survey2_RiskyUrns1_130 = make_survey2_urn(130)
    survey2_RiskyUrns1_140 = make_survey2_urn(140)
    survey2_RiskyUrns1_150 = make_survey2_urn(150)
    survey2_RiskyUrns1_sure = models.StringField()
    survey2_RiskyUrns1_choice = models.StringField()
    survey2_RiskyUrns1_choice_num = models.IntegerField()
    survey2_RiskyUrns1_payoff = models.IntegerField()

    survey2_RiskyUrns2_0 = make_survey2_urn(0)
    survey2_RiskyUrns2_10 = make_survey2_urn(10)
    survey2_RiskyUrns2_20 = make_survey2_urn(20)
    survey2_RiskyUrns2_30 = make_survey2_urn(30)
    survey2_RiskyUrns2_40 = make_survey2_urn(40)
    survey2_RiskyUrns2_50 = make_survey2_urn(50)
    survey2_RiskyUrns2_60 = make_survey2_urn(60)
    survey2_RiskyUrns2_70 = make_survey2_urn(70)
    survey2_RiskyUrns2_80 = make_survey2_urn(80)
    survey2_RiskyUrns2_90 = make_survey2_urn(90)
    survey2_RiskyUrns2_100 = make_survey2_urn(100)
    survey2_RiskyUrns2_sure = models.StringField()
    survey2_RiskyUrns2_choice = models.StringField()
    survey2_RiskyUrns2_choice_num = models.IntegerField()
    survey2_RiskyUrns2_payoff = models.IntegerField()

    survey2_total_payoff = models.IntegerField()

    def get_payoff_survey2(self):
        num = self.participant.vars['order_questions'][self.participant.vars['question_number']]
        if num == 1:
            self.survey2_RiskyProject1_left = \
                Constants.endowment_RiskyProject1 - self.survey2_question_RiskyProject1
            self.survey2_RiskyProject1_success = random.uniform(0, 100) < Constants.prob_success_RiskyProject1
            if self.survey2_RiskyProject1_success:
                self.survey2_RiskyProject1_earned = Constants.return_RiskyProject1 * self.survey2_question_RiskyProject1
            else:
                self.survey2_RiskyProject1_earned = 0
            self.survey2_RiskyProject1_payoff = self.survey2_RiskyProject1_left + self.survey2_RiskyProject1_earned
            self.survey2_total_payoff = self.survey2_total_payoff + self.survey2_RiskyProject1_payoff
        elif num == 2:
            self.survey2_RiskyProject2_left = \
                Constants.endowment_RiskyProject2 - self.survey2_question_RiskyProject2
            self.survey2_RiskyProject2_success = random.uniform(0, 100) < Constants.prob_success_RiskyProject2
            if self.survey2_RiskyProject2_success:
                self.survey2_RiskyProject2_earned = Constants.return_RiskyProject2 * self.survey2_question_RiskyProject2
            else:
                self.survey2_RiskyProject2_earned = 0
            self.survey2_RiskyProject2_payoff = self.survey2_RiskyProject2_left + self.survey2_RiskyProject2_earned
            self.survey2_total_payoff = self.survey2_total_payoff + self.survey2_RiskyProject2_payoff
        elif num == 3:
            sure = random.choice(Constants.Options_RiskyUrns1)
            self.survey2_RiskyUrns1_sure = str(Constants.choice2_RiskyUrns).format(sure)
            self.survey2_RiskyUrns1_choice_num = getattr(self, 'survey2_RiskyUrns1_{}'.format(sure))
            if self.survey2_RiskyUrns1_choice_num == 1:
                self.survey2_RiskyUrns1_choice = Constants.choice1_RiskyUrns
                ball = random.randint(1, Constants.LoseBalls_RiskyUrns1 + Constants.WinBalls_RiskyUrns1)
                if ball > Constants.LoseBalls_RiskyUrns1:
                    self.survey2_RiskyUrns1_payoff = Constants.WinPayoff_RiskyUrns1
                else:
                    self.survey2_RiskyUrns1_payoff = 0
            else:
                self.survey2_RiskyUrns1_choice = self.survey2_RiskyUrns1_sure
                self.survey2_RiskyUrns1_payoff = sure
            self.survey2_total_payoff = self.survey2_total_payoff + self.survey2_RiskyUrns1_payoff
        else:
            sure = random.choice(Constants.Options_RiskyUrns2)
            self.survey2_RiskyUrns2_sure = str(Constants.choice2_RiskyUrns).format(sure)
            self.survey2_RiskyUrns2_choice_num = getattr(self, 'survey2_RiskyUrns2_{}'.format(sure))
            if self.survey2_RiskyUrns2_choice_num == 1:
                self.survey2_RiskyUrns2_choice = Constants.choice1_RiskyUrns
                ball = random.randint(1, Constants.LoseBalls_RiskyUrns2 + Constants.WinBalls_RiskyUrns2)
                if ball > Constants.LoseBalls_RiskyUrns1:
                    self.survey2_RiskyUrns2_payoff = Constants.WinPayoff_RiskyUrns2
                else:
                    self.survey2_RiskyUrns2_payoff = 0
            else:
                self.survey2_RiskyUrns2_choice = self.survey2_RiskyUrns2_sure
                self.survey2_RiskyUrns2_payoff = sure
            self.survey2_total_payoff = self.survey2_total_payoff + self.survey2_RiskyUrns2_payoff

    Prisoner_decision = models.StringField(
        choices=[Constants.Prisoner_cooperate, Constants.Prisoner_defect],
        widget=widgets.RadioSelect
    )
    Prisoner_payoff = models.IntegerField()

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



