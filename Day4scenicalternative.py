def finish_solution_set(stem, target_num_digits):
	stem = str(stem)
	solutions = []
	initial_digits_remaining = target_num_digits - len(stem)
	stem = low_as_possible(stem, target_num_digits)
	solutions += get_last_digit_solutions(stem)
	stem = stem[:-1]
	digits_remaining = 1
	while digits_remaining < initial_digits_remaining:
		if stem[-1] != "9":
			stem = str(int(stem)+1)
			stem = low_as_possible(stem, target_num_digits)
			solutions += get_last_digit_solutions(stem)
			stem = stem[:-1]
			digits_remaining = 1
		else:
			stem = stem[:-1]
			digits_remaining += 1
	return(solutions)

def low_as_possible(stem, target_num_digits):
	solutions = []
	digits_remaining = target_num_digits - len(stem)
	last_digit = int(stem[-1])
	while digits_remaining > 0:
		stem += str(last_digit)
		digits_remaining -= 1
	return stem

def get_last_digit_solutions(potential_solution):
	solutions = []
	if len(set(potential_solution)) < len(potential_solution):
		solutions.append(potential_solution)
	while potential_solution[-1] != "9":
		potential_solution = str(int(potential_solution)+1)
		if len(set(potential_solution)) < len(potential_solution):
			solutions.append(potential_solution)
	return solutions

def solutions_for_input_245182_790572():
# Puzzle input was 245182-790572
	solutions = []
	for stem in range(245,250):
		solutions += finish_solution_set(stem,6)
	for stem in range(25,30):
		solutions += finish_solution_set(stem,6)
	for stem in range(3,7):
		solutions += finish_solution_set(stem,6)
	for stem in range(77,79):
		solutions += finish_solution_set(stem,6)
	return solutions

print("Part 1: {}".format(len(solutions_for_input_245182_790572())))
