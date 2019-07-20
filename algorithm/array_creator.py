import numpy as np 
import copy

def shuffle_list(original):
    shuffled=copy.copy(original)
    np.random.shuffle(shuffled)
    return shuffled

def create_test_set(size,trial):
    original=list(range(size))
    return [(np.random.choice(original),shuffle_list(original)) for _ in range(trial)]
