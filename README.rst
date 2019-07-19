oTree - Ultimatum Game
=======================================================

**PARAMETERS**

-------------------------------------------------------

language
    change the language (*en* or *ru*)

currency_used
    change the currency (0=USD, 1=POUNDS, 2=RUBLES)

real_world_currency_per_point
    This parameter allows to control the conversion rate between real world currencies

    Suggested formula: (for example, USD vs RUB)
        USD/point = RUB/point * (hourly payment in US in USD)/(hourly payment in Russia in RUB)

    Google says:
        - hourly payment in US = 25.5 USD
        - hourly payment in Moscow = 432 RUB
        - hourly payment in UK = 7 Pounds

    Suggested values:
        - 0.05 for USD
        - 0.02 for Pounds
        - 1.00 for Rubles

participation_fee
    fixed payment at the beginning of the experiment (in currency_used)

    Suggested values:
        - 5 for USD
        - 3 for Pounds
        - 200 for Rubles

rate
    conversion rate for **UG4-1** (positive integer)

    Default value: 10

rate_reversed
    conversion rate for **UG4-2** (positive integer)

    Default value: 10

rate_UG
    conversion rate for **UG2-1** (positive integer)

    Default value: 10

rate_UG_reversed
    conversion rate for **UG2-2** (positive integer)

    Default value: 10

rate_CT
    conversion rate for **Q-CT** (positive integer)

    Default value: 10

rate_Q
    conversion rate for **Q-Q** (positive integer)

    Default value: 1

n_questions
    the number of paid questions in **Q-Q**

    Default value: 3

endowment
    how many points Player 1 and Player 2 divide between each other in **UG4-1**, **UG4-2**, **UG2-1**, **UG2-2**

    Default value: 100

payoff_if_rejected
    how many points Players 1 and 2 each get when the offer is rejected in **UG4-1**, **UG4-2**, **UG2-1**, **UG2-2**

    Default value: 0

n_rounds
    the number of rounds in the game

    Default value: 8

min_n_rounds
    the minimum number of rounds needed to test application

    Default value: 2

skip_test
    whether the questionnaire should be skipped or not (set OFF for the actual experiment)

test_mode
    whether we want to run the experiment in a test regime (set OFF for the actual experiment)

skip_CognitiveTest
    whether the cognitive test should be skipped or not (set OFF for the actual experiment)

skip_ChoiceQuestions
    whether the choice questions should be skipped or not (set OFF for the actual experiment)

skip_survey
    whether the survey should be skipped or not (set OFF for the actual experiment)

total_questions = 2
    DO NOT CHANGE

    the number of parts where subjects have to answer paid questions = **Q-CT** and **Q-Q**

num_demo_participants = 4
    DO NOT CHANGE


-------------------------------------------------------

**FINAL PAYMENT**

-------------------------------------------------------

1. Participation fee
2. One round from **UG4-1** (on average = (*endowment*/2) * *rate* * *real_world_currency_per_point*)
3. One round from **UG4-2** (on average = (*endowment*/2) * *rate_reversed* * *real_world_currency_per_point*)
4. One round from **UG2-1** (on average = (*endowment*/2) * *rate_UG* * *real_world_currency_per_point*)
5. One round from **UG2-2** (on average = (*endowment*/2) * *rate_UG_reversed* * *real_world_currency_per_point*)
6. All questions in **Q-CT** (number of questions answered correctly * *rate_CT* * *real_world_currency_per_point*)
7. Points in *n_questions* questions in **Q-Q** * *rate_Q* * *real_world_currency_per_point*

-------------------------------------------------------

**DESCRIPTION**

-------------------------------------------------------

1. Instruction is shown
2. Quiz is played (if *skip_test* is OFF)
3. **UG4-1** Ultimatum Game with 4 players in a group and endogenous pairing is played (*n_rounds* rounds, unless *test_mode* is ON in which case *min_n_rounds* is played)
4. **UG4-2** Participants change roles (Player 1 <-> Player 2) and the previous game is repeated (with the same number of rounds)
5. **UG2-1** Participants are randomly assigned the roles. Ultimatum Game with 2 players in a group is played (*n_rounds* rounds, unless *test_mode* is ON in which case *min_n_rounds* is played)
6. **UG2-2** Participants change roles (Player 1 <-> Player 2) and the previous game is repeated (with the same number of rounds)
7. **Q-CT** Cognitive Test - questions with correct answers (questions are in the file *cognitive_en.csv* or *cognitive_ru.csv*)
8. **Q-Q** Questions with no correct answers (questions are in the file *choice_en.csv* or *choice_ru.csv*)
9. Total payoff in the experiment is displayed
10. Survey - opinion (agree / disagree) questions (file *survey_opinion_en.csv* or *survey_opinion_ru.csv*)
11. Survey - comments: not obligatory questions in text format (file *survey_comment_en.csv* or *survey_comment_ru.csv*)
12. Survey - personal questions (age, gender, etc)