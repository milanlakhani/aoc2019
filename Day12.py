"""
Puzzle input:
<x=-10, y=-10, z=-13>
<x=5, y=5, z=-9>
<x=3, y=8, z=-16>
<x=1, y=3, z=-3>
"""

Io = {"position":[-10,-10,-13], "velocity":[0,0,0]}
Europa = {"position":[5,5,-9], "velocity":[0,0,0]}
Ganymede = {"position":[3,8,-16], "velocity":[0,0,0]}
Callisto = {"position":[1,3,-3], "velocity":[0,0,0]}

moons = [Io, Europa, Ganymede, Callisto]

def apply_gravity(moons):
	for index_1 in range(len(moons)):
		for index_2 in range(index_1+1, len(moons)):
			for dimension in range(3):
				if moons[index_1]["position"][dimension] > moons[index_2]["position"][dimension]:
					moons[index_1]["velocity"][dimension] -= 1
					moons[index_2]["velocity"][dimension] += 1
				elif moons[index_1]["position"][dimension] < moons[index_2]["position"][dimension]:
					moons[index_1]["velocity"][dimension] += 1
					moons[index_2]["velocity"][dimension] -= 1
	return moons

def apply_velocity(moons):
	for moon in moons:
		for dimension in range(3):
			moon["position"][dimension] += moon["velocity"][dimension]
	return moons

def get_energy(moons):
	total_energy = 0
	for moon in moons:
		absolute_position = [abs(dimension) for dimension in moon["position"]]
		potential_energy = sum(absolute_position)
		absolute_velocity = [abs(dimension) for dimension in moon["velocity"]]
		kenetic_energy = sum(absolute_velocity)
		total_energy += potential_energy*kenetic_energy
	return total_energy

def make_steps_get_energy(moons, steps):
	for step in range(steps):
		moons = apply_gravity(moons)
		moons = apply_velocity(moons)
	energy = get_energy(moons)
	print("Step {} energy: {}".format(step+1,energy))
	return energy

def get_one_d_state(moons, dimension):
	state = []
	for moon in moons:
		state.append(moon["position"][dimension])
		state.append(moon["velocity"][dimension])
	return state

def one_d_repeat_history(moons, dimension):
	history = []
	state = get_one_d_state(moons, dimension)
	steps = 0
	while state not in history:
		history.append(state)
		for index_1 in range(len(moons)):
			for index_2 in range(index_1+1, len(moons)):
				if moons[index_1]["position"][dimension] > moons[index_2]["position"][dimension]:
					moons[index_1]["velocity"][dimension] -= 1
					moons[index_2]["velocity"][dimension] += 1
				elif moons[index_1]["position"][dimension] < moons[index_2]["position"][dimension]:
					moons[index_1]["velocity"][dimension] += 1
					moons[index_2]["velocity"][dimension] -= 1
		for moon in moons:
			moon["position"][dimension] += moon["velocity"][dimension]
		steps += 1
		state = get_one_d_state(moons, dimension)
		if steps % 1000 == 0:
			print(steps, dimension)
	print("Step {}:{}".format(steps,moons))
	return steps

def is_prime(n):
	for fact in range(2,n):
		if n % fact == 0:
			return False
		elif fact**2 > n:
			return True
	return True

def repeat_history(moons):
	a = one_d_repeat_history(moons, 0)
	b = one_d_repeat_history(moons, 1)
	c = one_d_repeat_history(moons, 2)
	cycles = [a,b,c]
	print("Individual cycle lengths: {}".format(cycles))
	lcm = 1
	n = 2
	while n <= max(cycles):
		if is_prime(n):
			max_power = 0
			for cycle in cycles:
				power = 0
				while cycle/n % 1 == 0:
					cycle = cycle/n
					power += 1
				if power > max_power:
					max_power = power
			lcm *= (n ** max_power)
		n += 1
	print("Steps to repeat history: {}".format(lcm))
	return lcm

make_steps_get_energy(moons, 1000)
repeat_history(moons)
