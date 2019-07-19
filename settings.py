from os import environ
import docutils.core

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

docutils.core.publish_file(
    source_path="README.rst",
    destination_path="README.html",
    writer_name="html")

SESSION_CONFIG_DEFAULTS = {
    'endowment': 100,
    'payoff_if_rejected': 0,
    'rate': 10,
    'rate_reversed': 10,
    'rate_UG': 10,
    'rate_UG_reversed': 10,
    'rate_CT': 10,
    'rate_Q': 1,
    'n_questions': 3,
    'total_questions': 2,  # number of parts where subjects have to answer paid questions
    'num_demo_participants': 4,
    'n_rounds': 8,
    'min_n_rounds': 2,
    'test_mode': True,
    'skip_test': True,
    'skip_CognitiveTest': False,
    'skip_ChoiceQuestions': False,
    'skip_survey': False,
    'doc': open('README.html').read()}
# 'doc': """
#     - Edit the 'language' and 'currency_used' parameter to change
#     the language ('en' or 'ru') and the currency (0=USD, 1=POUNDS, 2=RUBLES).\r\n
#
#     - Parameter 'n_rounds' corresponds to the number of rounds in the game.\n
#
#     Parameter 'skip_test' indicates whether the questionnaire should be skipped or not
#     (set OFF for the actual experiment)\n
#
#     Parameter 'skip_CognitiveTest' indicates whether the cognitive test should be skipped or not
#     (set OFF for the actual experiment)\n
#
#     Parameter 'skip_ChoiceQuestions' indicates whether the choice questions should be skipped or not
#     (set OFF for the actual experiment)\n
#
#     Parameter 'skip_survey' indicates whether the survey should be skipped or not
#     (set OFF for the actual experiment)\n
#
#     Parameter 'min_n_rounds' corresponds to the minimum number of rounds needed to test application\n
#
#     Parameter 'test_mode' indicates whether we want to run the experiment in a test regime
#     (set OFF for the actual experiment)
#     """}

SESSION_CONFIGS = [
    {
        'name': 'GameFeb19_en',
        'display_name': 'Experiment: February 2019 - English & USD',
        'app_sequence': ['GameFeb19_intro',
                         'GameFeb19_main', 'GameFeb19_role_reversed', 'GameFeb19_UG', 'GameFeb19_UG_role_reversed',
                         'GameFeb19_questions_cognitive', 'GameFeb19_questions_choice',
                         'GameFeb19_Payoffs',
                         'GameFeb19_survey_opinion', 'GameFeb19_survey_comment', 'GameFeb19_survey_personal',
                         'final_screen'],
        'use_browser_bots': True,
        'language': 'en',  # 'en' or 'ru'
        'currency_used': 0,  # 0=USD, 1=POUNDS, 2=RUBLES
        'real_world_currency_per_point': 0.05,
        'participation_fee': 5.00,
    },
    {
        'name': 'GameFeb19_en',
        'display_name': 'Experiment: February 2019 - English & Pounds',
        'app_sequence': ['GameFeb19_intro',
                         'GameFeb19_main', 'GameFeb19_role_reversed', 'GameFeb19_UG', 'GameFeb19_UG_role_reversed',
                         'GameFeb19_questions_cognitive', 'GameFeb19_questions_choice',
                         'GameFeb19_Payoffs',
                         'GameFeb19_survey_opinion', 'GameFeb19_survey_comment', 'GameFeb19_survey_personal',
                         'final_screen'],
        'use_browser_bots': True,
        'language': 'en',  # 'en' or 'ru'
        'currency_used': 1,  # 0=USD, 1=POUNDS, 2=RUBLES
        'real_world_currency_per_point': 0.02,
        'participation_fee': 3.00,
    },
    {
        'name': 'GameFeb19_ru',
        'display_name': 'Experiment: February 2019 - Russian',
        'app_sequence': ['GameFeb19_intro',
                         'GameFeb19_main', 'GameFeb19_role_reversed', 'GameFeb19_UG', 'GameFeb19_UG_role_reversed',
                         'GameFeb19_questions_cognitive', 'GameFeb19_questions_choice',
                         'GameFeb19_Payoffs',
                         'GameFeb19_survey_opinion', 'GameFeb19_survey_comment', 'GameFeb19_survey_personal',
                         'final_screen'],
        'use_browser_bots': True,
        'language': 'ru',  # 'en' or 'ru'
        'currency_used': 2,  # 0=USD, 1=POUNDS, 2=RUBLES
        'real_world_currency_per_point': 1.00,
        'participation_fee': 200,
    }
]

LANGUAGE_SESSION_KEY = '_language'

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'  # 'USD', 'RUB'
USE_POINTS = True

ROOMS = [
    {
        'name': 'room_100z',
        'display_name': 'Room for maximum 100 participants : room 1 (labels zi)',
        'participant_label_file': '_rooms/room_100z.txt'
    },
]

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """
Experiment for Ultimatum Game
"""

# don't share this with anybody.
SECRET_KEY = '-zix68refu)(#smaxr$n%3hz$4an1%=m_=8th@l7&2@*3-(xrd'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'otree_tools']
