import numpy as np
import pandas as pd
import random
import matplotlib.plt as plt
import seaborn as sns
import sklearn.metrics as metrics
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten, Dropout

# list all permutations of ace values
def get_ace_values(temp_list):
    sum_array = np.zeros((2 ** len(temp_list), len(temp_list)))

    for i in range(len(temp_list)):
        n = len(temp_list) - i
        half_len = int(2 ** n * 0.5)
        for rep in range((int(sum_array.shape[0]) / half_len / 2)):
            sum_array[rep * 2 ** n : rep * 2 ** n + half_len, i]
            sum_array[rep * 2 ** n + half_len : rep * 2 ** n + half_len * 2, i] = 11

    return [int(s) for s in np.sum(sum_array, axis = 1)]

# convert num_aces into list of lists
def ace_values(num_aces): 
    temp_list = []
    for i in range(num_aces): 
        temp_list.append([1, 11])
    return get_ace_values(temp_list)

# make deck
def make_decks(num_decks, card_types):
    new_deck = []
    for i in range(num_decks):
        for j in range(4):
            new_deck.extend(card_types)
    random.shuffle(new_deck)
    return new_deck 

# sum value of hand
def sum_up(hand):
    aces = 0
    total = 0

    for card in hand:
        if card != 'A':
            total += card
        else:
            aces += 1

    ace_value_list = ace_values(aces)
    final_totals = [i + total for i in ace_value_list if i + total <= 21]

    if final_totals == []:
        return min(ace_value_list) + total
    else:
        return max(final_totals)



    

