from threading import current_thread
from x_puzzle import X_Puzzle


def output_search(search_arr, filename):
    with(open(filename, 'w')) as file:
        for line in search_arr:
            if line.h == 0:
                f = 0
            else:
                f = line.h+line.g
            file.write(str(f) + ' ' + str(line.g) + ' ' +str(line.h) + ' ' + str(line.instance) + "\n")



def output_solution(solution_arr,filename,time_diff):
    total_cost = 0
    with(open(filename, 'w')) as file:
        for line in solution_arr:
            total_cost = total_cost + line.cost
            file.write(str(line.moved_value) + " " + str(line.cost) + " " +str(line.instance) + "\n")
        file.write(str(total_cost) + " " + str(time_diff))



def output_nosolution(filename):
    with(open(filename, 'w')) as file:
        file.write("no solution")