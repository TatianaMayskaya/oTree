from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


import random

author = 'Tatiana Mayskaya'

doc = """
Survey. Personal questions
"""


class Constants(BaseConstants):
    name_in_url = 'GameJan19_survey_personal'
    players_per_group = None
    num_rounds = 12


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.random_questions()
            if self.session.config['language'] == 1:
                self.session.vars['age'] = 'Age'
                self.session.vars['gender'] = 'Gender'
                self.session.vars['male'] = 'Male'
                self.session.vars['female'] = 'Female'
                self.session.vars['other'] = 'Other'
                self.session.vars['field'] = 'Field of expertise'
                self.session.vars['field1'] = 'Economics, finance, management'
                self.session.vars['field2'] = 'Social sciences, psychology, political science'
                self.session.vars['field3'] = 'Law'
                self.session.vars['field4'] = 'International relations'
                self.session.vars['field5'] = 'Mathematics, physics, computer science'
                self.session.vars['field6'] = 'Biology, chemistry'
                self.session.vars['field7'] = 'Humanities'
                self.session.vars['field8'] = 'Media'
                self.session.vars['field9'] = 'Other'
                self.session.vars['native_language'] = 'What is(are) your native language(s)?'
                self.session.vars['income'] = \
                    'Which statement best describes the financial situation in your family?'
                self.session.vars['income1'] = 'Barely enough to survive.'
                self.session.vars['income2'] = \
                    'We have enough money for food and other daily essentials but we have no capacity to make savings.'
                self.session.vars['income3'] = \
                    '''
                    We can afford vacation every year.
                    '''
                    #  'Buying cloths requires making savings in advance.'
                self.session.vars['income4'] = \
                    '''
                    We can travel abroad every year.
                    '''
                    # '''
                    # We have enough savings to buy cloths but more expensive products
                    # (like washing machine, TV set, or plane tickets) require advance planning.
                    # '''
                self.session.vars['income5'] = 'We have no financial constraints.'
                    # 'We can buy quite expensive products without advance planning.'
                self.session.vars['riskat'] = \
                    'How do you see yourself: Are you generally a person who is fully prepared to take risks ' \
                    'or do you try to avoid taking risks? Please tick a box on the scale, ' \
                    'where the value 0 means: \'Not at all willing to take risks\' and ' \
                    'the value 10 means: \'Very willing to take risks\'.'
                self.session.vars['happy_now'] = \
                    'Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. ' \
                    'The top of the ladder represents the best possible life for you and the bottom of the ladder ' \
                    'represents the worst possible life for you. On which step of the ladder would you say ' \
                    'you personally feel you stand at this time?'
                self.session.vars['happy_future'] = \
                    'Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. ' \
                    'The top of the ladder represents the best possible life for you and the bottom of the ladder ' \
                    'represents the worst possible life for you. Just your best guess, on which step fo you think ' \
                    'you will stand in the future, say about five years from now?'
                self.session.vars['trust'] = \
                    'Do you think you could trust most people or they are generally not trustworthy? Please tick ' \
                    'a box on the scale, where the value 0 means: \'I never trust people\' and ' \
                    'the value 10 means: \'I always trust people\'.'
                self.session.vars['freedom'] = \
                    'Some people feel like they have complete freedom of choice and control of their lives, ' \
                    'whereas others believe their actions have no effect on their fate. What about you? ' \
                    'Please tick a box on the scale, where the value 0 means: \'I have no control of my fate\' and ' \
                    'the value 10 means: \'I have complete control of my life\'.'
                self.session.vars['democracy'] = \
                    'How important is it for you to live in a country that is governed based on democracy principals, ' \
                    'that is, where the citizens exercise power by voting? ' \
                    'Please tick a box on the scale, where the value 0 means: \'It does not matter\' and ' \
                    'the value 10 means: \'It is very important\'.'
                self.session.vars['democracy_live'] = \
                    'Do you think the country of your citizenship is democratic? ' \
                    'Please tick a box on the scale, where the value 0 means: \'It is not democratic at all\' and ' \
                    'the value 10 means: \'It is governed strictly based on democracy principals\'.'
            else:
                self.session.vars['age'] = 'Ваш возраст (полных лет)'
                self.session.vars['gender'] = 'Ваш пол'
                self.session.vars['male'] = 'Мужской'
                self.session.vars['female'] = 'Женский'
                self.session.vars['other'] = 'Другой'
                self.session.vars['field'] = 'Ваша специализация'
                self.session.vars['field1'] = 'Экономика, финансы, менеджмент'
                self.session.vars['field2'] = 'Социальные науки, психология, политология'
                self.session.vars['field3'] = 'Право'
                self.session.vars['field4'] = 'Международные отношения'
                self.session.vars['field5'] = 'Математика, физика, компьютерные науки'
                self.session.vars['field6'] = 'Биология, химия'
                self.session.vars['field7'] = 'Гуманитарные науки'
                self.session.vars['field8'] = 'Медиа'
                self.session.vars['field9'] = 'Другое'
                self.session.vars['native_language'] = 'Какой Ваш родной язык? (укажите все, если их больше одного)'
                self.session.vars['income'] = \
                    'Какое высказывание наиболее точно описывает финансовое положение вашей семьи?'
                self.session.vars['income1'] = 'Едва сводим концы с концами, денег не хватает на выживание.'
                self.session.vars['income2'] = \
                    'Живем от зарплаты до зарплаты, денег хватает только на неотложные нужды.'
                self.session.vars['income3'] = \
                    'На ежедневные расходы хватает денег, но уже покупка одежды требует накоплений.'
                self.session.vars['income4'] = \
                    'Вполне хватает денег, даже имеются некоторые накопления, ' \
                    'но крупные покупки требуется планировать заранее.'
                self.session.vars['income5'] = 'Можем позволить себе крупные траты при первой необходимости.'
                self.session.vars['riskat'] = \
                    'По шкале от 0 до 10, как сильно Вы любите риск / боитесь риска ' \
                    '(0 означает \'Очень боюсь рисковать\', 10 означает \'Очень люблю рисковать\')?'
                self.session.vars['happy_now'] = \
                    'Представьте себе лестницу, у которой 11 ступенек, пронумерованных от 0 (самая нижняя) ' \
                    'до 10. Самая верхняя ступенька символизирует самую лучшую жизнь, а самая нижняя - самую худшую. ' \
                    'На какой ступеньке Вы сейчас находитесь?'
                self.session.vars['happy_future'] = \
                    'Представьте себе лестницу, у которой 11 ступенек, пронумерованных от 0 (самая нижняя) ' \
                    'до 10. Самая верхняя ступенька символизирует самую лучшую жизнь, а самая нижняя - самую худшую. ' \
                    'Как Вы думаете, на какой ступеньке Вы будете находиться через, скажем, пять лет?'
                self.session.vars['trust'] = \
                    'Как Вы считаете, в целом большинству людей можно доверять, или же при общении с другими людьми ' \
                    'осторожность никогда не повредит? Пожалуйста, отметьте позицию на шкале, где 0 означает ' \
                    '\'Нужно быть очень осторожным с другими людьми\' и 10 означает \'Большинству людей можно ' \
                    'вполне доверять\'.'
                self.session.vars['freedom'] = \
                    'Некоторые люди чувствуют, что они обладают полной свободой выбора и контролируют свою жизнь, ' \
                    'в то время как другие люди чувствуют, что то, что они делают, не имеет реального влияния ' \
                    'на происходящее с ними. До какой степени эти характеристики применимы к Вам и Вашей жизни? ' \
                    'Пожалуйста, отметьте позицию на шкале, где 0 означает \'у меня нет свободы выбора\' ' \
                    'и 10 означает \'у меня полная свобода выбора\'.'
                self.session.vars['democracy'] = \
                    'Насколько важно для Вас жить в стране, которая управляется по принципам демократии, ' \
                    'т.е. в соответствии с волей народа? ' \
                    'Пожалуйста, отметьте позицию на шкале, где 0 означает \'Не важно\' ' \
                    'и 10 означает \'Очень важно\'.'
                self.session.vars['democracy_live'] = \
                    'Как Вы считаете, Вы являетесь гражданином демократической страны? ' \
                    'Пожалуйста, отметьте позицию на шкале, где 0 означает ' \
                    '\'Страна, гражданоном которой я являюсь, абсолютно не является демократией\' ' \
                    'и 10 означает \'Страна, гражданином которой я являюсь, ' \
                    'полностью управляется в соответствии с демократическими принципами\'.'


class Group(BaseGroup):
    pass


def make_question():
    return models.PositiveIntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal)


class Player(BasePlayer):
    def random_questions(self):
        randomized_questions = random.sample(range(1, Constants.num_rounds + 1, 1), Constants.num_rounds)
        self.participant.vars['questions'] = randomized_questions

    age = models.IntegerField(min=13, max=95, initial=None)
    gender = models.IntegerField(initial=None, widget=widgets.RadioSelect())
    field = models.PositiveIntegerField(widget=widgets.RadioSelect())
    native_language = models.StringField()
    income = models.PositiveIntegerField(widget=widgets.RadioSelect())
    riskat = make_question()
    happy_now = make_question()
    happy_future = make_question()
    trust = make_question()
    freedom = make_question()
    democracy = make_question()
    democracy_live = make_question()