def process_opcodes(opcodes):
	position = 0
	while True:
		if opcodes[position] == 1:
			opcodes[(opcodes[position+3])] = opcodes[
			(opcodes[position+1])] + opcodes[(opcodes[position+2])]
		elif opcodes[position] == 2:
			opcodes[(opcodes[position+3])] = opcodes[
			(opcodes[position+1])] * opcodes[(opcodes[position+2])]
		elif opcodes[position] == 99:
			return(1)
		else:
			return(0)
		position += 4
	return opcodes

def restore_alarm_state(opcodes, noun, verb):
	opcodes[1] = noun
	opcodes[2] = verb
	process_opcodes(opcodes)
	return(opcodes[0])

def find_noun_and_verb(output, puzzle_input):
	opcodes = get_opcodes(puzzle_input)
	for noun in range(100):
		for verb in range(100):
			state = restore_alarm_state(opcodes, noun, verb)
			if state == output:
				print("Part 2: {}".format(100*noun+verb))
				return([noun, verb])
			else:
				opcodes = get_opcodes(puzzle_input)
	print("finished")
	return([noun, verb])

def get_opcodes(puzzle_input):
	input_list = puzzle_input.split(",")
	opcodes = [int(num) for num in input_list]
	return(opcodes)

puzzle_input = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,5,19,23,1,23,6,27,1,5,27,31,1,31,6,35,1,9,35,39,2,10,39,43,1,43,6,47,2,6,47,51,1,5,51,55,1,55,13,59,1,59,10,63,2,10,63,67,1,9,67,71,2,6,71,75,1,5,75,79,2,79,13,83,1,83,5,87,1,87,9,91,1,5,91,95,1,5,95,99,1,99,13,103,1,10,103,107,1,107,9,111,1,6,111,115,2,115,13,119,1,10,119,123,2,123,6,127,1,5,127,131,1,5,131,135,1,135,6,139,2,139,10,143,2,143,9,147,1,147,6,151,1,151,13,155,2,155,9,159,1,6,159,163,1,5,163,167,1,5,167,171,1,10,171,175,1,13,175,179,1,179,2,183,1,9,183,0,99,2,14,0,0"""

print("Part 1: {}".format(restore_alarm_state(get_opcodes(puzzle_input), 12, 2)))
find_noun_and_verb(19690720, puzzle_input)
