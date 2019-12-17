def get_first_list(puzzle_input):
	initial = [int(digit) for digit in puzzle_input]
	return initial

def one_phase(signal):
	output = []
	for digit in range(len(signal)):
		to_append = 0
		increment = digit+1
		if increment % 100 == 0:
			print(increment)
		indice = increment-1
		sign = 1
		while indice <= len(signal):
			to_append += sum(signal[indice:indice+increment])*sign
			indice += 2*increment
			sign *= -1
		output.append(abs(to_append)%10)
	return output

def multiple_phases(phases, signal):
	for phase in range(phases):
		signal = one_phase(signal)
		print("Phase {}".format(phase))
	return signal

def offset_multiple_phases(phases, signal):
	initial_signal = signal
	signal = multiple_phases(phases, signal)
	message_position_list = [str(numb) for numb in initial_signal[:7]]
	message_position = int("".join(message_position_list))
	print(signal[message_position:message_position+8])

puzzle_input = "59780176309114213563411626026169666104817684921893071067383638084250265421019328368225128428386936441394524895942728601425760032014955705443784868243628812602566362770025248002047665862182359972049066337062474501456044845186075662674133860649155136761608960499705430799727618774927266451344390608561172248303976122250556049804603801229800955311861516221350410859443914220073199362772401326473021912965036313026340226279842955200981164839607677446008052286512958337184508094828519352406975784409736797004839330203116319228217356639104735058156971535587602857072841795273789293961554043997424706355960679467792876567163751777958148340336385972649515437"

# print(len(puzzle_input))
print(multiple_phases(100, get_first_list(puzzle_input)))
print(offset_multiple_phases(100, get_first_list(puzzle_input)*10000))
