from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, add_currency, do_my_shuffle, set_payoffs

from GameFeb19_intro.pages import Page, WaitPage

import random

from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.session.vars['UG'] = False
        self.session.vars['reversed'] = False
        do_my_shuffle(self.subsession)


class Introduction(Page):
    def vars_for_template(self):
        return {'rate_text': add_currency(
            self.session.config['currency_used'],
            self.session.vars['rate'] * self.session.config['real_world_currency_per_point'])}

    def is_displayed(self):
        return self.round_number == 1


class RoleInGame(Page):
    template_name = 'global/RoleInGame.html'

    def vars_for_template(self):
        return {'role': self.player.role(),
                'round_number': self.round_number,
                'n_rounds': self.session.config['n_rounds']}


class Offer(Page):
    template_name = 'global/Offer.html'

    form_model = 'player'
    form_fields = ['offer']

    def offer_max(self):
        return self.session.vars['endowment']

    def is_displayed(self):
        return self.player.role() == '1A' or self.player.role() == '1B'

    def vars_for_template(self):
        return {'role': self.player.role(),
                'round_number': self.round_number,
                'n_rounds': self.session.config['n_rounds'],
                'offer_label': _('You have {} tokens. Choose how many tokens you want to offer to Player 2').format(
                    self.session.vars['endowment']),
                'submit': _('Submit'),
                'change': _('Change the choice'),
                'endowment': self.session.vars['endowment'],
                'payoff_if_rejected': self.session.vars['payoff_if_rejected']}


class OfferWaitPage(WaitPage):
    def after_all_players_arrive(self):
        if self.round_number < self.session.config['n_rounds']:
            self.group.computer_choice = random.choice(['C', 'D'])
        else:
            self.group.computer_choice = 'C'


class ComputerChoice(Page):
    template_name = 'global/ComputerChoice.html'

    def vars_for_template(self):
        return {'round_number': self.round_number,
                'n_rounds': self.session.config['n_rounds'],
                'computer_choice': self.group.computer_choice}


class PlayerChoice(Page):
    template_name = 'global/PlayerChoice.html'

    form_model = 'group'
    form_fields = ['player_choice']

    def is_displayed(self):
        if self.group.computer_choice == 'C':
            return self.player.role() == '2C'
        else:
            return self.player.role() == '2D'

    def vars_for_template(self):
        if self.group.computer_choice == 'C':
            computer_choice_opposite = 'D'
        else:
            computer_choice_opposite = 'C'
        return {'round_number': self.round_number,
                'n_rounds': self.session.config['n_rounds'],
                'role': self.player.role(),
                'computer_choice_opposite': computer_choice_opposite,
                'player_choice_label': _('Choose your partner'),
                'submit': _('Submit'),
                'change': _('Change the choice')}


class PlayerChoiceWaitPage(WaitPage):
    pass


class MatchAnnouncement(Page):
    template_name = 'global/MatchAnnouncement.html'

    def vars_for_template(self):
        if self.group.computer_choice == 'C':
            computer_choice_opposite = 'D'
        else:
            computer_choice_opposite = 'C'
        if self.group.player_choice == 'A':
            player_choice_opposite = 'B'
        else:
            player_choice_opposite = 'A'
        return {'round_number': self.round_number,
                'n_rounds': self.session.config['n_rounds'],
                'computer_choice': self.group.computer_choice,
                'computer_choice_opposite': computer_choice_opposite,
                'player_choice': self.group.player_choice,
                'player_choice_opposite': player_choice_opposite}


class PlayerChoiceAnnouncement(Page):
    template_name = 'global/PlayerChoiceAnnouncement.html'

    def is_displayed(self):
        if self.group.computer_choice == 'C':
            return not (self.player.role() == '2C')
        else:
            return not (self.player.role() == '2D')

    def vars_for_template(self):
        if self.group.computer_choice == 'C':
            computer_choice_opposite = 'D'
        else:
            computer_choice_opposite = 'C'
        if self.group.player_choice == 'A':
            player_choice_opposite = 'B'
        else:
            player_choice_opposite = 'A'
        return {'round_number': self.round_number,
                'n_rounds': self.session.config['n_rounds'],
                'computer_choice': self.group.computer_choice,
                'computer_choice_opposite': computer_choice_opposite,
                'player_choice': self.group.player_choice,
                'player_choice_opposite': player_choice_opposite}


class Accept(Page):
    template_name = 'global/Accept.html'
    form_model = 'player'
    form_fields = ['response']

    def is_displayed(self):
        return self.player.role() == '2C' or self.player.role() == '2D'

    def vars_for_template(self):
        if self.group.player_choice == 'A':
            player_choice_opposite = 'B'
        else:
            player_choice_opposite = 'A'
        if self.player.role() == '2C' and self.group.computer_choice == 'C':
            partner = self.group.player_choice
        elif self.player.role() == '2D' and self.group.computer_choice == 'D':
            partner = self.group.player_choice
        else:
            partner = player_choice_opposite
        return {'role': self.player.role(),
                'round_number': self.round_number,
                'n_rounds': self.session.config['n_rounds'],
                'response_label': _('Choose the minimum offer that you would accept'),
                'endowment': self.session.vars['endowment'],
                'payoff_if_rejected': self.session.vars['payoff_if_rejected'],
                'partner': partner,
                'submit': _('Submit'),
                'change': _('Change the choice')}


class ResponseWaitPage(WaitPage):
    def after_all_players_arrive(self):
        set_payoffs(self.group, 1)


class Results(Page):
    template_name = 'global/Results.html'

    def vars_for_template(self):
        if self.group.computer_choice == 'C':
            computer_choice_opposite = 'D'
        else:
            computer_choice_opposite = 'C'
        if self.group.player_choice == 'A':
            player_choice_opposite = 'B'
        else:
            player_choice_opposite = 'A'
        return {'round_number': self.round_number,
                'n_rounds': self.session.config['n_rounds'],
                'computer_choice': self.group.computer_choice,
                'computer_choice_opposite': computer_choice_opposite,
                'player_choice': self.group.player_choice,
                'player_choice_opposite': player_choice_opposite,
                'UG': self.session.vars['UG']}

    def app_after_this_page(self, upcoming_apps):
        if self.round_number == self.session.config['n_rounds']:
            return upcoming_apps[0]


# class Payoffs(Page):
#     template_name = 'global/Payoffs.html'
#
#     def vars_for_template(self):
#         return {'role': self.participant.vars['role'],
#                 'role_reversed': self.participant.vars['role_reversed'],
#                 'roleUG': self.participant.vars['roleUG'],
#                 'roleUG_reversed': self.participant.vars['roleUG_reversed'],
#                 'results_table': self.participant.vars['results_table'],
#                 'results_table_reversed': self.participant.vars['results_table_reversed'],
#                 'results_tableUG': self.participant.vars['results_tableUG'],
#                 'results_tableUG_reversed': self.participant.vars['results_tableUG_reversed'],
#                 'payment_round': self.participant.vars['payment_round'],
#                 'payment_round_reversed': self.participant.vars['payment_round_reversed'],
#                 'payment_roundUG': self.participant.vars['payment_roundUG'],
#                 'payment_roundUG_reversed': self.participant.vars['payment_roundUG_reversed'],
#                 'payment': self.participant.vars['payment_formula'] + ' = ' + self.participant.vars['payoff_text']}


page_sequence = [
    ShuffleWaitPage,
    Introduction,
    RoleInGame,
    Offer,
    OfferWaitPage,
    ComputerChoice,
    PlayerChoice,
    PlayerChoiceWaitPage,
    PlayerChoiceAnnouncement,
    Accept,
    ResponseWaitPage,
    Results
]
