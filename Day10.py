import numpy
import math
import operator

def get_astroid_map(astroid_string):
    astroid_list = astroid_string.split("\n")
    astroid_map = numpy.zeros((len(astroid_list[0]),len(astroid_list)))
    for row in range(len(astroid_list)):
        for position in range(len(astroid_list[0])):
            if astroid_list[row][position] == "#":
                astroid_map[position][row] = 1
    return astroid_map

def get_ratio(row, check_row, column, check_column):
    hcf = 1
    x = column - check_column
    y = row - check_row
    if y == 0:
        hcf = abs(x)
    elif x == 0:
        hcf = abs(y)
    else:
        for i in range(2,min(abs(x),abs(y))+1):
            if x % i == 0 and y % i == 0:
                hcf = i
    ratio = [int(x/hcf),int(y/hcf)]
    return ratio

def get_angle_and_dist(monitoring_station, astroidrow, astroidcolumn):
    x = astroidcolumn - monitoring_station[1]
    y = monitoring_station[0] - astroidrow
    if x == 0:
        if y > 0:
            angle = 0
        elif y < 0:
            angle = math.pi
    elif y == 0:
        if x > 0:
            angle = 0.5*math.pi
        elif x < 0:
            angle = 1.5*math.pi
    elif x > 0:
        if y > 0:
            angle = math.atan(x/y)
        elif y < 0:
            angle = 0.5*math.pi + math.atan(abs(y/x))
    elif x < 0:
        if y < 0:
            angle = math.pi + math.atan(abs(x/y))
        elif y > 0:
            angle = 1.5*math.pi + math.atan(abs(y/x))
    return([angle, 1/(abs(x)+abs(y)), astroidrow, astroidcolumn])

def max_astroid_detection(astroid_string):
    astroid_map = get_astroid_map(astroid_string)
    max_viewcount = 0
    monitoring_station = []
    for row in range(astroid_map.shape[0]):
        for column in range(astroid_map.shape[1]):
            if astroid_map[row][column] == 1:
                viewcount = 0
                ratios_blocked = []
                for check_row in range(astroid_map.shape[0]):
                    for check_column in range(astroid_map.shape[1]):
                        if astroid_map[check_row][check_column] == 0 or (
                            check_row == row and check_column == column):
                            continue
                        ratio = get_ratio(row,check_row,column,check_column)
                        if ratio in ratios_blocked:
                            continue
                        else:
                            viewcount += 1
                            ratios_blocked.append(ratio)
                if viewcount > max_viewcount:
                    max_viewcount = viewcount
                    monitoring_station = [row,column]
    print("Max astroids visible: {} at {}".format(max_viewcount, monitoring_station))
    return monitoring_station

def terrible_hacky_laser(astroid_string, laser_row, laser_column, gamblee):
    astroid_map = get_astroid_map(astroid_string)
    astroid_map[laser_row,laser_column] = 4

    ratios_blocked = []
    for check_row in range(astroid_map.shape[0]):
        for check_column in range(astroid_map.shape[1]):
            if astroid_map[check_row][check_column] == 0 or (
                check_row == laser_row and check_column == laser_column):
                continue
            ratio = get_ratio(laser_row,check_row,laser_column,check_column)
            if ratio in ratios_blocked:
                continue
            else:
                ratios_blocked.append(ratio)

    visible_astroids = []
    for ratio in ratios_blocked:
        blocked = False
        multiplier = 1
        while not blocked:
            search_astroid_row = int(laser_row-(multiplier*ratio[0]))
            search_astroid_column = int(laser_column-(multiplier*ratio[1]))
            if astroid_map[search_astroid_column][search_astroid_row] == 1:
                visible_astroids.append([search_astroid_row,search_astroid_column])
                blocked = True
            else:
                multiplier += 1

    visible = [get_angle_and_dist([laser_row,laser_column], astroid[0], astroid[1]) for astroid in visible_astroids]
    sorted_visible = sorted(visible, key=operator.itemgetter(0))

    for i in sorted_visible:
        astroid_map[int(i[2])][int(i[3])] = 9
        print(astroid_map)
        astroid_map[int(i[2])][int(i[3])] = 0
        print(astroid_map)
    print("Astroid {} - Row: {} Column: {}".format(gamblee,sorted_visible[gamblee-1][3], sorted_visible[gamblee-1][2]))
    return("Oh gosh")

astroid_string = """###..#########.#####.
.####.#####..####.#.#
.###.#.#.#####.##..##
##.####.#.###########
###...#.####.#.#.####
#.##..###.########...
#.#######.##.#######.
.#..#.#..###...####.#
#######.##.##.###..##
#.#......#....#.#.#..
######.###.#.#.##...#
####.#...#.#######.#.
.######.#####.#######
##.##.##.#####.##.#.#
###.#######..##.#....
###.##.##..##.#####.#
##.########.#.#.#####
.##....##..###.#...#.
#..#.####.######..###
..#.####.############
..##...###..#########"""

monitoring_station = max_astroid_detection(astroid_string)
terrible_hacky_laser(astroid_string, monitoring_station[0], monitoring_station[1], 200)