from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


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

    def gender_choices(self):
        return [[0, self.session.vars['female']],
                [1, self.session.vars['male']],
                [-1, self.session.vars['other']]]

    def field_choices(self):
        return [[1, self.session.vars['field1']],
                [2, self.session.vars['field2']],
                [3, self.session.vars['field3']],
                [4, self.session.vars['field4']],
                [5, self.session.vars['field5']],
                [6, self.session.vars['field6']],
                [7, self.session.vars['field7']],
                [8, self.session.vars['field8']],
                [9, self.session.vars['field9']]]

    def income_choices(self):
        return [[1, self.session.vars['income1']],
                [2, self.session.vars['income2']],
                [3, self.session.vars['income3']],
                [4, self.session.vars['income4']],
                [5, self.session.vars['income5']]]

    def vars_for_template(self):
        num = self.participant.vars['questions'][self.round_number - 1]
        if num == 1:
            question_label = self.session.vars['age']
        elif num == 2:
            question_label = self.session.vars['gender']
        elif num == 3:
            question_label = self.session.vars['field']
        elif num == 4:
            question_label = self.session.vars['native_language']
        elif num == 5:
            question_label = self.session.vars['income']
        elif num == 6:
            question_label = self.session.vars['riskat']
        elif num == 7:
            question_label = self.session.vars['happy_now']
        elif num == 8:
            question_label = self.session.vars['happy_future']
        elif num == 9:
            question_label = self.session.vars['trust']
        elif num == 10:
            question_label = self.session.vars['freedom']
        elif num == 11:
            question_label = self.session.vars['democracy']
        elif num == 12:
            question_label = self.session.vars['democracy_live']
        else:
            question_label = []

        return {'language': self.session.config['language'],
                'question_label': question_label,
                'part_num': self.participant.vars['survey_part']}

    def before_next_page(self):
        if self.round_number == Constants.num_rounds:
            self.participant.vars['survey_part'] = self.participant.vars['survey_part'] + 1


page_sequence = [
    Question
]
