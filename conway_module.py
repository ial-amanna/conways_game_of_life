import numpy as np
import time


def initialize(size):
	state = np.random.randint(2, size = size)
	return state

def find_current_state(state):
	n = (state[0:-2,0:-2] + state[0:-2,1:-1] + state[0:-2,2:] +
          state[1:-1,0:-2] + state[1:-1,2:] + state[2:,0:-2] +
          state[2:,1:-1] + state[2:,2:])
	return n

def apply_rules(state, n):
	birth = (n == 3) & (state[1:-1,1:-1] == 0)
	survive = ((n == 2) | (n == 3)) & (state[1:-1,1:-1] == 1)
	state[...] = 0
	state[1:-1,1:-1][birth | survive] = 1
	born = np.sum(birth)
	survived = np.sum(survive)
	return born, survived

def conway_game(i, size, state):
	state = initialize(size)
	number = find_current_state(state)
	born, survived = apply_rules(state, number)
	print('Life Cycle: {} Birth: {} Survive: {}'.format(i, born, survived))
	return state
	
	
