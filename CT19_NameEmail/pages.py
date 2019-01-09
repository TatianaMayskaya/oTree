from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ContactInfo(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.participant.label[0] == '_' and self.session.config['Email'] == 1:
            return ['name', 'email']
        elif self.participant.label[0] == '_':
            return ['name']
        elif self.session.config['Email'] == 1:
            return ['email']
        else:
            return []

    def is_displayed(self):
        return self.session.config['Email'] == 1 or self.participant.label[0] == '_'


page_sequence = [ContactInfo]
