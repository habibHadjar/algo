import random
# ----------------------< Game rules constants  >-----------------------------------------------------------------------

# Number of dices by default in the set
DEFAULT_DICES_NB = 12
# Target total score to win by default
DEFAULT_TARGET_SCORE = 2000
# Number of side of the dices used in the game
NB_DICE_SIDE = 6

# List of dice value scoring
LIST_SCORING_DICE_VALUE = [1, 5]
# List of associated score for scoring dice values
LIST_SCORING_MULTIPLIER = [100, 50]

# Trigger for multiple bonus
TRIGGER_OCCURRENCE_FOR_BONUS = 3
# Special bonus multiplier for multiple ace bonus
BONUS_VALUE_FOR_ACE_BONUS = 1000
# Standard multiplier for multiple dices value bonus
BONUS_VALUE_FOR_NORMAL_BONUS = 100

def roll_dice_set(nb_dice_to_roll):
    dice_set = [0] * NB_DICE_SIDE
    rolls = 0
    while rolls < nb_dice_to_roll:
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_set[dice_value - 1] += 1
        rolls += 1
    return dice_set

my_dice_set = roll_dice_set(DEFAULT_DICES_NB)
print(my_dice_set)

def analyse_bonus_score(dice_value_occurrence):
    score = 0
    scoring_dices = [0] * len(dice_value_occurrence)
    dice_index = 0
    
    while dice_index < len(dice_value_occurrence):
        if dice_value_occurrence[dice_index] >= TRIGGER_OCCURRENCE_FOR_BONUS:
            if dice_index == 0:
                score += BONUS_VALUE_FOR_ACE_BONUS * ( dice_value_occurrence[dice_index] // TRIGGER_OCCURRENCE_FOR_BONUS )
            else:
                score += BONUS_VALUE_FOR_NORMAL_BONUS * ( dice_index + 1 ) * ( dice_value_occurrence[dice_index] // TRIGGER_OCCURRENCE_FOR_BONUS )
                
            scoring_dices[dice_index] = dice_value_occurrence[dice_index] // TRIGGER_OCCURRENCE_FOR_BONUS
            dice_value_occurrence[dice_index] -= dice_value_occurrence[dice_index] // TRIGGER_OCCURRENCE_FOR_BONUS * TRIGGER_OCCURRENCE_FOR_BONUS
            
        dice_index += 1
        
    return {'score' : score, 'bonus_scoring_dices' : scoring_dices, 'non_scoring_dices' : dice_value_occurrence}

my_dice_set_analyzed = analyse_bonus_score(my_dice_set)
print(my_dice_set_analyzed)

def analyse_standard_score(dice_value_occurences):
    score = 0
    scoring_dices = [0] * len(dice_value_occurences)
    non_scoring_dices = [0] * len(dice_value_occurences)
    dice_index = 0
    
    while dice_index < len(dice_value_occurences):
        if dice_value_occurences[dice_index] > 0:
            if dice_index == 0:
                score += LIST_SCORING_MULTIPLIER[0] * dice_value_occurences[dice_index]
                scoring_dices[dice_index] = dice_value_occurences[dice_index]
            elif dice_index == 4:
                score += LIST_SCORING_MULTIPLIER[1] * dice_value_occurences[dice_index]
                scoring_dices[dice_index] = dice_value_occurences[dice_index]
        else :
            non_scoring_dices[dice_index] = dice_value_occurences[dice_index]
            
        dice_index += 1
        
    return {'score' : score, 'std_scoring_dices' : scoring_dices, 'non_scoring_dices' : non_scoring_dices}

my_dice_set_analyzed_std = analyse_standard_score(my_dice_set_analyzed["non_scoring_dices"])
print(my_dice_set_analyzed_std)
