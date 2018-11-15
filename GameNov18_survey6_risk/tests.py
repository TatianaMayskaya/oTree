from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        num = self.participant.vars['questions_order'][self.round_number - 1]
        if num == 1:
            yield (pages.RiskyProject, {'question_RiskyProject1': 30})
            yield (pages.RiskyProjectResults)
        elif num == 2:
            yield (pages.RiskyProject, {'question_RiskyProject2': 10})
            yield (pages.RiskyProjectResults)
        elif num == 3:
            yield (pages.RiskyUrns, {'RiskyUrns1_0': 1,
                                     'RiskyUrns1_10': 1,
                                     'RiskyUrns1_20': 1,
                                     'RiskyUrns1_30': 1,
                                     'RiskyUrns1_40': 1,
                                     'RiskyUrns1_50': 1,
                                     'RiskyUrns1_60': 1,
                                     'RiskyUrns1_70': 1,
                                     'RiskyUrns1_80': 1,
                                     'RiskyUrns1_90': 1,
                                     'RiskyUrns1_100': 1,
                                     'RiskyUrns1_110': 1,
                                     'RiskyUrns1_120': 1,
                                     'RiskyUrns1_130': 1,
                                     'RiskyUrns1_140': 1,
                                     'RiskyUrns1_150': 1})
            yield (pages.RiskyUrnsResults)
        else:
            yield (pages.RiskyUrns, {'RiskyUrns2_0': 1,
                                     'RiskyUrns2_10': 1,
                                     'RiskyUrns2_20': 1,
                                     'RiskyUrns2_30': 1,
                                     'RiskyUrns2_40': 1,
                                     'RiskyUrns2_50': 1,
                                     'RiskyUrns2_60': 1,
                                     'RiskyUrns2_70': 2,
                                     'RiskyUrns2_80': 2,
                                     'RiskyUrns2_90': 2,
                                     'RiskyUrns2_100': 2})
            yield (pages.RiskyUrnsResults)
        if self.round_number == 4:
            yield (pages.Results)
