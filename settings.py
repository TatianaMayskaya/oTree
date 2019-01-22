from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
     {
        'name': 'GameJan19',
        'display_name': 'Experiment: January 2019',
        'num_demo_participants': 4,
        'app_sequence': ['GameJan19_intro', 'GameJan19_main'],
        # 'app_sequence': ['GameJan19_main'],
        'use_browser_bots': True,
        'language': 1,  # 1=EN, 2=RU
        'currency_used': 0,  # 0=USD, 1=POUNDS, 2=RUBLES
        'n_rounds': 4,  # make sure it coincides with the number of rounds in GameJan19_main
        'doc': """
        Edit the 'language' and 'currency_used' parameter to change
        the language (1=EN, 2=RU) and the currency (0=USD, 1=POUNDS, 2=RUBLES).
        Parameter 'n_rounds' corresponds to the number of rounds in the game (do not change).
        """
     },
     {
         'name': 'ContractTheoryICEF2019_Class1',
         'display_name': "Contract Theory ICEF year 2019. Class 1",
         'num_demo_participants': 2,
         'app_sequence': ['CT19_NameEmail', 'CT19_SellerBuyer'],
         'use_browser_bots': True,
         'Email': 1,
         'file': 'CT19_SellerBuyer/parameters1.csv',
         'doc': """
         Edit 'Email' to control whether emails should be collected for 
         participants in the database (0=no,1=yes)
         
         Edit 'file' for the file containing parameters (in csv format)
         """
     },
     {
         'name': 'ContractTheoryICEF2019_Class2',
         'display_name': "Contract Theory ICEF year 2019. Class 2",
         'num_demo_participants': 2,
         'app_sequence': ['CT19_NameEmail', 'CT19_SellerBuyer'],
         'use_browser_bots': True,
         'Email': 1,
         'file': 'CT19_SellerBuyer/parameters2.csv',
         'doc': """
         Edit 'Email' to control whether emails should be collected for 
         participants in the database (0=no,1=yes)
         
         Edit 'file' for the file containing parameters (in csv format)
         """
     },
     {
        'name': 'ResearchSeminar_11Jan19',
        'display_name': "Research Seminar - order assignment (11 January 2019)",
        'num_demo_participants': 4,
        'app_sequence': ['CT19_NameEmail', 'RS19_SchedulingGame'],
        'use_browser_bots': True,
        'Email': 1,
        'doc': """
         Edit 'Email' to control whether emails should be collected for 
         participants in the database (0=no,1=yes)
         """
     }
    # {
    #     'name': 'my_game',
    #     'display_name': 'My Game',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['my_game'],
    # },
    # {
    #     'name': 'GameOct18_ru',
    #     'display_name': 'GameOct18_ru',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['GameOct18'],
    #     'use_browser_bots': False
    # },
    # {
    #     'name': 'GameOct18_en',
    #     'display_name': 'GameOct18_en',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['GameOct18_en'],
    # },
    # {
    #     'name': 'GameNov18',
    #     'display_name': 'GameNov18',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['GameNov18_intro',
    #                      'GameNov18_main',
    #                      'GameNov18_survey_text_logic',
    #                      'GameNov18_survey_roles_reversed',
    #                      'GameNov18_survey_opinion',
    #                      # 'GameNov18_survey_text_modifications',
    #                      'GameNov18_survey_comments',
    #                      'GameNov18_survey_risk',
    #                      'GameNov18_survey_prisoner',
    #                      'GameNov18_survey_trust',
    #                      'GameNov18_survey_personal',
    #                      'final_screen'
    #                      ],
    #     'use_browser_bots': True,
    #     'language': 1,  # 1=EN, 2=RU
    #     'currency_used': 0,  # 0=USD, 1=POUNDS, 2=RUBLES
    #     'doc': """
    #     Edit the 'language' and 'currency_used' parameter to change
    #     the language (1=EN, 2=RU) and the currency (0=USD, 1=POUNDS, 2=RUBLES)
    #     """
    # },
    # {
    #     'name': 'public_goods',
    #     'display_name': "Public Goods",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['public_goods', 'payment_info'],
    # },
    # {
    #     'name': 'guess_two_thirds',
    #     'display_name': "Guess 2/3 of the Average",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['guess_two_thirds', 'payment_info'],
    # },
    # {
    #     'name': 'survey',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['survey', 'payment_info'],
    # },
    # {
    #     'name': 'quiz',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['quiz'],
    # },
    # {
    #     'name': 'prisoner',
    #     'display_name': "Prisoner's Dilemma",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['prisoner', 'payment_info'],
    # },
    # {
    #     'name': 'ultimatum',
    #     'display_name': "Ultimatum (randomized: strategy vs. direct response)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['ultimatum', 'payment_info'],
    # },
    # {
    #     'name': 'ultimatum_strategy',
    #     'display_name': "Ultimatum (strategy method treatment)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['ultimatum', 'payment_info'],
    #     'use_strategy_method': True,
    # },
    # {
    #     'name': 'ultimatum_non_strategy',
    #     'display_name': "Ultimatum (direct response treatment)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['ultimatum', 'payment_info'],
    #     'use_strategy_method': False,
    # },
]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'  # 'USD', 'RUB'
USE_POINTS = True

ROOMS = [
    {
        'name': 'ContractTheoryICEF2019',
        'display_name': 'Contract Theory ICEF year 2019',
        'participant_label_file': '_rooms/ContractTheoryICEF2019.txt',
    },
    {
        'name': 'ResearchSeminar3year2019',
        'display_name': 'Research Seminar 3 year 2019',
        'participant_label_file': '_rooms/ResearchSeminar3year2019.txt'
    },
    {
        'name': 'room_100z',
        'display_name': 'Room for maximum 100 participants : room 1 (labels zi)',
        'participant_label_file': '_rooms/room_100z.txt'
    },
    # {
    #     'name': 'econ101',
    #     'display_name': 'Econ 101 class',
    #     'participant_label_file': '_rooms/econ101.txt',
    # },
    # {
    #     'name': 'live_demo',
    #     'display_name': 'Room for live demo (no participant labels)',
    # },
    # {
    #     'name': 'game_for_two_players',
    #     'display_name': 'Game for two players',
    #     'participant_label_file': '_rooms/game_for_two_players.txt'
    # },
    # {
    #     'name': 'GameOct18_en_AM',
    #     'display_name': 'GameOct18 - test for English version : Alexander Matros',
    #     'participant_label_file': '_rooms/GameOct18_4.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_AM',
    #     'display_name': 'GameOct18 - test for Russian version : Alexander Matros',
    #     'participant_label_file': '_rooms/GameOct18_4.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_16',
    #     'display_name': 'GameOct18 - for maximum 16 participants',
    #     'participant_label_file': '_rooms/GameOct18_16.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_20_room1',
    #     'display_name': 'GameOct18 - for maximum 20 participants : room 1 (labels: Pi)',
    #     'participant_label_file': '_rooms/GameOct18_20.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_20_room2',
    #     'display_name': 'GameOct18 - for maximum 20 participants : room 2 (labels: Pi)',
    #     'participant_label_file': '_rooms/GameOct18_20.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_20_room3',
    #     'display_name': 'GameOct18 - for maximum 20 participants : room 3 (labels: Pi)',
    #     'participant_label_file': '_rooms/GameOct18_20.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_20_room4',
    #     'display_name': 'GameOct18 - for maximum 20 participants : room 4 (labels: Pi)',
    #     'participant_label_file': '_rooms/GameOct18_20.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_20_room5',
    #     'display_name': 'GameOct18 - for maximum 20 participants : room 5 (labels: Pi)',
    #     'participant_label_file': '_rooms/GameOct18_20.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_20_room6',
    #     'display_name': 'GameOct18 - for maximum 20 participants : room 6 (labels: Pi)',
    #     'participant_label_file': '_rooms/GameOct18_20.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_30z_room1',
    #     'display_name': 'GameOct18 - for maximum 30 participants : room 1 (labels: zi)',
    #     'participant_label_file': '_rooms/GameOct18_30z.txt'
    # },
    # {
    #     'name': 'GameOct18_ru_30z_room2',
    #     'display_name': 'GameOct18 - for maximum 30 participants : room 2 (labels: zi)',
    #     'participant_label_file': '_rooms/GameOct18_30z.txt'
    # },
    # {
    #     'name': 'GameNov18_room1',
    #     'display_name': 'GameNov18 - for maximum 100 participants : room 1 (labels zi)',
    #     'participant_label_file': '_rooms/room_100z.txt'
    # },
    # {
    #     'name': 'GameNov18_room2',
    #     'display_name': 'GameNov18 - for maximum 100 participants : room 2 (labels zi)',
    #     'participant_label_file': '_rooms/room_100z.txt'
    # }
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
Here are various games implemented with 
oTree. These games are open
source, and you can modify them as you wish.
"""

# don't share this with anybody.
SECRET_KEY = '-zix68refu)(#smaxr$n%3hz$4an1%=m_=8th@l7&2@*3-(xrd'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'otree_tools']

# inactive session configs
### {
###     'name': 'trust',
###     'display_name': "Trust Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust', 'payment_info'],
### },
### {
###     'name': 'prisoner',
###     'display_name': "Prisoner's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['prisoner', 'payment_info'],
### },
### {
###     'name': 'ultimatum',
###     'display_name': "Ultimatum (randomized: strategy vs. direct response)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
### },
### {
###     'name': 'ultimatum_strategy',
###     'display_name': "Ultimatum (strategy method treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': True,
### },
### {
###     'name': 'ultimatum_non_strategy',
###     'display_name': "Ultimatum (direct response treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': False,
### },
### {
###     'name': 'vickrey_auction',
###     'display_name': "Vickrey Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['vickrey_auction', 'payment_info'],
### },
### {
###     'name': 'volunteer_dilemma',
###     'display_name': "Volunteer's Dilemma",
###     'num_demo_participants': 3,
###     'app_sequence': ['volunteer_dilemma', 'payment_info'],
### },
### {
###     'name': 'cournot',
###     'display_name': "Cournot Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'cournot', 'payment_info'
###     ],
### },
### {
###     'name': 'principal_agent',
###     'display_name': "Principal Agent",
###     'num_demo_participants': 2,
###     'app_sequence': ['principal_agent', 'payment_info'],
### },
### {
###     'name': 'dictator',
###     'display_name': "Dictator Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['dictator', 'payment_info'],
### },
### {
###     'name': 'matching_pennies',
###     'display_name': "Matching Pennies",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'matching_pennies',
###     ],
### },
### {
###     'name': 'traveler_dilemma',
###     'display_name': "Traveler's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['traveler_dilemma', 'payment_info'],
### },
### {
###     'name': 'bargaining',
###     'display_name': "Bargaining Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['bargaining', 'payment_info'],
### },
### {
###     'name': 'common_value_auction',
###     'display_name': "Common Value Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['common_value_auction', 'payment_info'],
### },
### {
###     'name': 'bertrand',
###     'display_name': "Bertrand Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'bertrand', 'payment_info'
###     ],
### },
### {
###     'name': 'real_effort',
###     'display_name': "Real-effort transcription task",
###     'num_demo_participants': 1,
###     'app_sequence': [
###         'real_effort',
###     ],
### },
### {
###     'name': 'lemon_market',
###     'display_name': "Lemon Market Game",
###     'num_demo_participants': 3,
###     'app_sequence': [
###         'lemon_market', 'payment_info'
###     ],
### },
### {
###     'name': 'public_goods_simple',
###     'display_name': "Public Goods (simple version from tutorial)",
###     'num_demo_participants': 3,
###     'app_sequence': ['public_goods_simple', 'payment_info'],
### },
### {
###     'name': 'trust_simple',
###     'display_name': "Trust Game (simple version from tutorial)",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust_simple'],
### },
