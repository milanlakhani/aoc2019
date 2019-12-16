import math

def make_fuel(puzzle_input):
	reactions = puzzle_input.split("\n")
	fuel_chemicals = {"spare":{}, "ORE":0}
	for line in reactions:
		if line[-4:] == "FUEL":
			reaction = line.split(" => ")
			reaction_input = [[int(element.split(" ")[0]), element.split(" "
				)[1]] for element in reaction[0].split(", ")]
			for element in reaction_input:
				fuel_chemicals[element[1]] = element[0]
			break
	while len(fuel_chemicals) > 2:
		keys = list(fuel_chemicals.keys())
		for key in keys:
			for line in reactions:
				if line[len(key)*-1:] == key:
					reaction = line.split(" => ")
					reaction_multiple = int(reaction[1].split(" ")[0])
					reaction_multiplier = int(math.ceil(fuel_chemicals[key]/reaction_multiple))
					reaction_input = [[int(element.split(" ")[0])*reaction_multiplier, element.split(" "
						)[1]] for element in reaction[0].split(", ")]
					for chemical in reaction_input:
						if chemical[1] in fuel_chemicals:
							fuel_chemicals[chemical[1]] += chemical[0]
						else:
							fuel_chemicals[chemical[1]] = chemical[0]
					if fuel_chemicals[key] < reaction_multiple*reaction_multiplier:
						fuel_chemicals["spare"][key] = reaction_multiple*reaction_multiplier - fuel_chemicals[key]
					del fuel_chemicals[key]
					break
		no_longer_spare = []
		for chemical in fuel_chemicals["spare"]:
			if chemical in fuel_chemicals:
				if fuel_chemicals[chemical] == fuel_chemicals["spare"][chemical]:
					del fuel_chemicals[chemical]
					no_longer_spare.append(chemical)
				elif fuel_chemicals[chemical] > fuel_chemicals["spare"][chemical]:
					fuel_chemicals[chemical] -= fuel_chemicals["spare"][chemical]
					no_longer_spare.append(chemical)
				elif fuel_chemicals[chemical] < fuel_chemicals["spare"][chemical]:
					fuel_chemicals["spare"][chemical] -= fuel_chemicals[chemical]
					del fuel_chemicals[chemical]
		for chemical in no_longer_spare:
			del fuel_chemicals["spare"][chemical]
	return fuel_chemicals

def make_lots_of_fuel(puzzle_input, cargo_hold):
	reactions = puzzle_input.split("\n")
	fuel_chemicals = {"ORE":0, "spare":{}}
	fuel = 0
	while cargo_hold >= 0:
		for line in reactions:
			if line[-4:] == "FUEL":
				reaction = line.split(" => ")
				reaction_input = [[int(element.split(" ")[0]), element.split(" "
					)[1]] for element in reaction[0].split(", ")]
				for element in reaction_input:
					fuel_chemicals[element[1]] = element[0]
				break
		no_longer_spare = []
		for chemical in fuel_chemicals["spare"]:
			if chemical in fuel_chemicals:
				if fuel_chemicals[chemical] == fuel_chemicals["spare"][chemical]:
					del fuel_chemicals[chemical]
					no_longer_spare.append(chemical)
				elif fuel_chemicals[chemical] > fuel_chemicals["spare"][chemical]:
					fuel_chemicals[chemical] -= fuel_chemicals["spare"][chemical]
					no_longer_spare.append(chemical)
				elif fuel_chemicals[chemical] < fuel_chemicals["spare"][chemical]:
					fuel_chemicals["spare"][chemical] -= fuel_chemicals[chemical]
					del fuel_chemicals[chemical]
		for chemical in no_longer_spare:
			del fuel_chemicals["spare"][chemical]
		while len(fuel_chemicals) > 2:
			keys = list(fuel_chemicals.keys())
			for key in keys:
				for line in reactions:
					if line[len(key)*-1:] == key:
						reaction = line.split(" => ")
						reaction_multiple = int(reaction[1].split(" ")[0])
						reaction_multiplier = int(math.ceil(fuel_chemicals[key]/reaction_multiple))
						reaction_input = [[int(element.split(" ")[0])*reaction_multiplier, element.split(" "
							)[1]] for element in reaction[0].split(", ")]
						for chemical in reaction_input:
							if chemical[1] in fuel_chemicals:
								fuel_chemicals[chemical[1]] += chemical[0]
							else:
								fuel_chemicals[chemical[1]] = chemical[0]
						if fuel_chemicals[key] < reaction_multiple*reaction_multiplier:
							fuel_chemicals["spare"][key] = reaction_multiple*reaction_multiplier - fuel_chemicals[key]
						del fuel_chemicals[key]
						break
			no_longer_spare = []
			for chemical in fuel_chemicals["spare"]:
				if chemical in fuel_chemicals:
					if fuel_chemicals[chemical] == fuel_chemicals["spare"][chemical]:
						del fuel_chemicals[chemical]
						no_longer_spare.append(chemical)
					elif fuel_chemicals[chemical] > fuel_chemicals["spare"][chemical]:
						fuel_chemicals[chemical] -= fuel_chemicals["spare"][chemical]
						no_longer_spare.append(chemical)
					elif fuel_chemicals[chemical] < fuel_chemicals["spare"][chemical]:
						fuel_chemicals["spare"][chemical] -= fuel_chemicals[chemical]
						del fuel_chemicals[chemical]
			for chemical in no_longer_spare:
				del fuel_chemicals["spare"][chemical]
		cargo_hold -= fuel_chemicals["ORE"]
		fuel_chemicals["ORE"] = 0
		if cargo_hold >= 0:
			fuel += 1
		if cargo_hold % 1000 == 999:
			print("Ore left in cargo hold: {}, fuel produced: {}".format(cargo_hold, fuel))
	print("Fuel produced from {} ores: {}".format(cargo_hold, fuel))

puzzle_input = """6 GTGRP, 1 VPGRV, 1 KGQR => 6 HSHQR
1 RZXL => 1 MJTV
2 MJTV, 1 NZFM => 6 MGVLC
6 PFWG, 2 NVQG => 5 DCQP
6 MQDF, 1 NTHXM, 10 NZFM => 3 JRKQ
13 KFZXS => 8 MQDF
2 CMBFH => 9 KCXVQ
13 QVTVR, 4 HXTVZ, 2 TGFZK => 9 FCLQJ
2 ZBXVW => 5 WQVSD
20 DXKGN, 10 LWNB, 1 KCGRN, 1 QLZWT, 2 CTKD => 3 LSWQ
10 TGFZK => 8 CMBFH
149 ORE => 4 NTHXM
145 ORE => 5 ZVCW
1 LSFHG => 4 PFWG
1 NTHXM, 1 THSD => 6 LSFHG
1 KFZXS, 4 VTMK => 4 LWNB
20 HXTVZ, 1 LWNB => 7 QNDT
3 FHVXH, 6 NBGZ => 8 MLBKD
9 MQDF, 1 VJLNZ => 9 FHVXH
2 CWLD => 3 HLXNV
7 PFWG, 1 NCRG => 6 JLPG
2 XCTGC, 10 VZDF, 5 JRKQ => 8 NVQG
2 MJCR => 7 VPGRV
18 XTNK, 1 THSD => 3 VJLNZ
3 CWLD => 3 NMKZN
3 LSFHG, 1 PFWG, 6 DXKGN => 1 WVLN
12 NMKZN => 8 VZDF
1 MJTV => 5 NZFM
31 MGVLC => 5 THSD
11 PFWG => 8 JTHQ
2 KGQR, 1 TGFZK, 2 FPZHG => 4 XTXKL
30 GTGRP => 3 NBGZ
17 NVQG => 8 HDWSV
1 THSD, 18 XTNK => 2 FPZHG
5 QNDT, 13 WDGM, 13 NTHXM, 10 NBGZ, 14 GTGRP, 14 KFWM, 3 HDWSV, 5 LSWQ => 1 FUEL
3 VJLNZ, 5 VTMK => 9 DXKGN
1 LWNB, 2 HSHQR, 10 WQVSD => 9 QLZWT
42 VZDF, 3 RZXL, 1 NTHXM => 7 XTNK
3 WVLN => 7 NCRG
14 NZFM => 8 XCTGC
4 NVQG, 2 LSFHG => 7 KGQR
26 HSHQR, 3 BVMKL => 2 QVTVR
1 VJLNZ, 7 XTNK => 1 KCGRN
167 ORE => 3 KCLR
2 ZVCW, 3 RZXL, 1 KCLR => 9 CWLD
5 FCLQJ, 19 MLBKD, 4 SRPRL, 5 RMQRL, 11 WQVSD, 3 QLZWT => 6 KFWM
3 KCLR, 1 VZDF => 5 TGFZK
17 NVQG, 1 VPGRV => 5 BVMKL
4 WQVSD => 4 RMQRL
4 KCGRN, 4 DCQP => 4 SRPRL
2 KCGRN => 4 CTKD
1 HLXNV, 1 KFZXS => 7 MJCR
116 ORE => 6 RZXL
181 ORE => 7 KFZXS
1 FHVXH, 1 NVQG => 5 GTGRP
5 JTHQ, 8 FCLQJ, 1 XTXKL, 1 QVTVR, 1 WQVSD, 10 JLPG => 3 WDGM
1 NZFM, 1 RZXL, 17 MGVLC => 4 VTMK
1 KFZXS => 7 ZBXVW
7 KCXVQ, 29 BVMKL => 6 HXTVZ"""

print("Ore required for 1 FUEL: {}".format(make_fuel(puzzle_input)["ORE"]))
make_lots_of_fuel(puzzle_input, 1000000000000)