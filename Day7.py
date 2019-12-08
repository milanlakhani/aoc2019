import itertools

def get_opcodes(puzzle_input):
	input_list = puzzle_input.split(",")
	opcodes = [int(num) for num in input_list]
	return(opcodes)

def modesgetter(number):
	modes = (number - (number % 100))/100
	return [modes%10,(modes%100-modes%10)/10,(modes-(modes%100))/100]

def opcode_3_input(options):
	for number in options:
		yield number

def amp_process(opcodes, input1, input2):
	opcode_3_func = opcode_3_input([input1,input2])
	position = 0
	while True:
		if opcodes[position] % 100 == 1:
			opcode_length = 4
			mode = modesgetter(opcodes[position])
			if mode[0] == 0:
				first_param = opcodes[(opcodes[position+1])]
			elif mode[0] == 1:
				first_param = opcodes[position+1]
			if mode[1] == 0:
				second_param = opcodes[(opcodes[position+2])]
			elif mode[1] == 1:
				second_param = opcodes[position+2]
			if mode[2] == 0:
				opcodes[(opcodes[position+3])] = first_param + second_param
			elif mode[2] == 1:
				opcodes[position+3] = first_param + second_param
		elif opcodes[position] % 100 == 2:
			opcode_length = 4
			mode = modesgetter(opcodes[position])
			if mode[0] == 0:
				first_param = opcodes[(opcodes[position+1])]
			elif mode[0] == 1:
				first_param = opcodes[position+1]
			if mode[1] == 0:
				second_param = opcodes[(opcodes[position+2])]
			elif mode[1] == 1:
				second_param = opcodes[position+2]
			if mode[2] == 0:
				opcodes[(opcodes[position+3])] = first_param * second_param
			elif mode[2] == 1:
				opcodes[position+3] = first_param * second_param
		elif opcodes[position] == 3:
			opcodes[(opcodes[position+1])] = opcode_3_func.__next__()
			opcode_length = 2
		elif opcodes[position] == 4:
			opcode_length = 2
			print(opcodes[(opcodes[position+1])])
			output = opcodes[(opcodes[position+1])]
			return opcodes[(opcodes[position+1])]
		elif opcodes[position] % 100 == 5:
			opcode_length = 3
			mode = modesgetter(opcodes[position])
			if mode[0] == 0 and opcodes[(opcodes[position+1])] != 0:
				opcode_length = 0
				if mode[1] == 0:
					position = opcodes[(opcodes[position+2])]
				elif mode[1] == 1:
					position = opcodes[position+2]
			elif mode[0] == 1 and opcodes[position+1] != 0:
				opcode_length = 0
				if mode[1] == 0:
					position = opcodes[(opcodes[position+2])]
				elif mode[1] == 1:
					position = opcodes[position+2]
		elif opcodes[position] % 100 == 6:
			opcode_length = 3
			mode = modesgetter(opcodes[position])
			if mode[0] == 0 and opcodes[(opcodes[position+1])] == 0:
				opcode_length = 0
				if mode[1] == 0:
					position = opcodes[(opcodes[position+2])]
				elif mode[1] == 1:
					position = opcodes[position+2]
			elif mode[0] == 1 and opcodes[position+1] == 0:
				opcode_length = 0
				if mode[1] == 0:
					position = opcodes[(opcodes[position+2])]
				elif mode[1] == 1:
					position = opcodes[position+2]
		elif opcodes[position] % 100 == 7:
			opcode_length = 4
			mode = modesgetter(opcodes[position])
			if mode[0] == 0:
				first_param = opcodes[(opcodes[position+1])]
			elif mode[0] == 1:
				first_param = opcodes[position+1]
			if mode[1] == 0:
				second_param = opcodes[(opcodes[position+2])]
			elif mode[1] == 1:
				second_param = opcodes[position+2]
			if mode[2] == 0:
				if first_param < second_param:
					opcodes[(opcodes[position+3])] = 1
				else:
					opcodes[(opcodes[position+3])] = 0
			elif mode[2] == 1:
				if first_param < second_param:
					opcodes[position+3] = 1
				else:
					opcodes[position+3] = 0
		elif opcodes[position] % 100 == 8:
			opcode_length = 4
			mode = modesgetter(opcodes[position])
			if mode[0] == 0:
				first_param = opcodes[(opcodes[position+1])]
			elif mode[0] == 1:
				first_param = opcodes[position+1]
			if mode[1] == 0:
				second_param = opcodes[(opcodes[position+2])]
			elif mode[1] == 1:
				second_param = opcodes[position+2]
			if mode[2] == 0:
				if first_param == second_param:
					opcodes[(opcodes[position+3])] = 1
				else:
					opcodes[(opcodes[position+3])] = 0
			elif mode[2] == 1:
				if first_param == second_param:
					opcodes[position+3] = 1
				else:
					opcodes[position+3] = 0
		elif opcodes[position] == 99:
			print("Halt")
			# return("Halt")
			return output
		elif opcodes[position] == 103:
			opcodes[position+1] = opcode_3_func.__next__()
			opcode_length = 2
		elif opcodes[position] == 104:
			opcode_length = 2
			print(opcodes[position+1])
			output = opcodes[(opcodes[position+1])]
			return opcodes[(opcodes[position+1])]
		else:
			print("Fault")
			return("Fault")
		position += opcode_length
	print("Somehow finished")
	return("Somehow finished")

def max_amps_output_1(puzzle_input, phase_sequence_list):
	highest_signal = 0
	opcodes = get_opcodes(puzzle_input)
	for phase_sequence in phase_sequence_list:
		input2 = 0
		for phase in phase_sequence:
			input2 = amp_process(opcodes, phase, input2)
		if input2 > highest_signal:
			highest_signal = input2
	print("HS: {}".format(highest_signal))
	return(highest_signal)

def max_amps_output_2(puzzle_input, phase_sequence_list):
	highest_signal = 0
	opcodes = get_opcodes(puzzle_input)
	for phase_sequence in phase_sequence_list:
		input2 = 0
		while True:
			for phase in phase_sequence:
				input2 = amp_process(opcodes, phase, input2)
		if input2 > highest_signal:
			highest_signal = input2
	print("HS: {}".format(highest_signal))
	return(highest_signal)

puzzle_input = """3,8,1001,8,10,8,105,1,0,0,21,30,55,80,101,118,199,280,361,442,99999,3,9,101,4,9,9,4,9,99,3,9,101,4,9,9,1002,9,4,9,101,4,9,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,101,5,9,9,1002,9,2,9,101,3,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99"""

max_amps_output_1(puzzle_input, list(itertools.permutations([0,1,2,3,4])))
# max_amps_output_2(puzzle_input, list(itertools.permutations([5,6,7,8,9])))