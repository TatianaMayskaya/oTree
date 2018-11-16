from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Tatiana Mayskaya'

doc = """
Endogenous Choice Between ultimatum and Dictator Games: Experimental Evidence
Survey. Experiment with reversed roles
"""


class Constants(BaseConstants):
    name_in_url = 'GameNov18_survey_roles_reversed'
    players_per_group = 2
    num_rounds = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    amount_offered = models.IntegerField(min=0)
    amount_offered_1 = models.IntegerField(min=0)
    amount_offered_2 = models.IntegerField(min=0)
    response = models.IntegerField(min=0)
    game_played = models.IntegerField(widget=widgets.RadioSelectHorizontal)


class Player(BasePlayer):
    pass
