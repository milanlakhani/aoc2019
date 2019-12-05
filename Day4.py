def aoc4a(lower, upper):
	solutions = []
	for numb in range(lower, upper+1):
		valid = True
		numb = str(numb)
		for pos in range(len(numb)-1):
			for compare in range(pos+1,len(numb)):
				if numb[pos] > numb[compare]:
					valid = False
					break
			if not valid:
				break
		if valid and len(set(numb)) < len(numb):
			solutions.append(numb)
	return(solutions)

def onlyDoubles(solutions):
	doubles = []
	for solution in solutions:
		present = False
		if solution[0] == solution[1] and solution[1] != solution[2]:
			present = True
		elif solution[len(solution)-3] != solution[len(solution)-2] and solution[len(solution)-2] == solution[len(solution)-1]:
			present = True
		else:
			for i in range(1,len(solution)-2):
				if solution[i-1] != solution[i] == solution[i+1] != solution[i+2]:
					present = True
		if present:
			doubles.append(solution)
	return(doubles)

print("Part 1: {}".format(len(aoc4a(245182,790572))))
print("Part 2: {}".format(len(onlyDoubles(aoc4a(245182,790572)))))
