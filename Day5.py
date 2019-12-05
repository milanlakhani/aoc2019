def get_opcodes(puzzle_input):
	input_list = puzzle_input.split(",")
	opcodes = [int(num) for num in input_list]
	return(opcodes)

def modesgetter(number):
	modes = (number - (number % 100))/100
	return [modes%10,(modes%100-modes%10)/10,(modes-(modes%100))/100]

def process_opcodes_a(opcodes, input):
	position = 0
	while True:
		opcode_length = 4
		if opcodes[position] % 100 == 1:
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
			opcodes[(opcodes[position+1])] = input
			opcode_length = 2
		elif opcodes[position] == 4:
			print(opcodes[(opcodes[position+1])])
			opcode_length = 2
		elif opcodes[position] == 99:
			print("Halt")
			return("Halt")
		elif opcodes[position] == 103:
			opcodes[position+1] = input
			opcode_length = 2
		elif opcodes[position] == 104:
			print(opcodes[position+1])
			opcode_length = 2
		else:
			print("Fault")
			return("Fault")
		position += opcode_length
	print("Somehow finished")
	return("Somehow finished")

def process_opcodes_b(opcodes, input):
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
			opcodes[(opcodes[position+1])] = input
			opcode_length = 2
		elif opcodes[position] == 4:
			print(opcodes[(opcodes[position+1])])
			opcode_length = 2
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
			return("Halt")
		elif opcodes[position] == 103:
			opcodes[position+1] = input
			opcode_length = 2
		elif opcodes[position] == 104:
			print(opcodes[position+1])
			opcode_length = 2
		else:
			print("Fault")
			return("Fault")
		position += opcode_length
	print("Somehow finished")
	return("Somehow finished")

puzzle_input = """3,225,1,225,6,6,1100,1,238,225,104,0,1101,90,64,225,1101,15,56,225,1,14,153,224,101,-147,224,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,2,162,188,224,101,-2014,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1001,18,81,224,1001,224,-137,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,16,16,224,101,-256,224,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,101,48,217,224,1001,224,-125,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1002,158,22,224,1001,224,-1540,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,83,31,225,1101,56,70,225,1101,13,38,225,102,36,192,224,1001,224,-3312,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1102,75,53,225,1101,14,92,225,1101,7,66,224,101,-73,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,77,60,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,374,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,389,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,404,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,449,1001,223,1,223,1107,226,226,224,1002,223,2,223,1005,224,464,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,479,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,509,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,524,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,584,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,614,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,629,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226"""

process_opcodes_a(get_opcodes(puzzle_input), 1)
process_opcodes_b(get_opcodes(puzzle_input), 5)