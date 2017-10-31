from knapsack import knapsack
from utils import c_fair_input, fair_pair_input, c_fixed_input

def c_fair(c, payoffs):
	# TODO
	return True

def fair_pair(task_pairs):
	# TODO
	return True

def c_fixed(c, commands):
	# TODO
	return True

if __name__ == "__main__":
	problem = input()
	
	input_fn, solver =	(c_fair_input, c_fair) if problem == "c-fair" else \
						(fair_pair_input, fair_pair) if problem == "fair-pair" else \
						(c_fixed_input, c_fixed)

	problem_input = input_fn()
	print(int(solver(**problem_input)))
