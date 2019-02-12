import numpy as np

# Score categories
# Change the values as you see fit
YACHT = 'YACHT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
	max_val = max(dice)
	min_val = min(dice)
	occur_max_val = dice.count(max_val)
	occur_min_val = dice.count(min_val)
	sequences = set(dice) #Distinct values
	
	if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
		result = category * (dice.count(category))
		return result
		
	elif category == FULL_HOUSE and sum_occur_min_max(occur_min_val, occur_max_val) == 5:
		return sum(dice)
		
	elif category == FOUR_OF_A_KIND:
		return common_value(dice)
		
	elif category == CHOICE:
		return sum(dice)

	elif category == YACHT:
		if occur_max_val == 5:
			return 50
		else:
			return 0
	
	elif category == BIG_STRAIGHT and sequences == set([2,3,4,5,6]):
		return 30

	elif category == LITTLE_STRAIGHT and sequences == set([1,2,3,4,5]):
		return 30
			
	else:
		return 0


def sum_occur_min_max (occur_min_val, occur_max_val):
	if occur_min_val in (2,3) and occur_max_val in (2,3) and (occur_min_val + occur_max_val) == 5:
		return occur_min_val + occur_max_val
	else:
		return 0


def common_value (dice):
	if dice.count(np.bincount(dice).argmax()) >= 4:  #np.bincount Count number of occurences of each value in array. argmax returns index of first (maximum) value in array.
		return np.bincount(dice).argmax() * 4
	else:
		return 0