def read_input(filename):
    with(open(filename)) as file:
        for line in file:
            print(line)

def output_solution(solution_arr,filename,time_diff):
    total_cost = 0
    with(open(filename, 'w')) as file:
        for line in solution_arr:
            total_cost = total_cost + line.cost
            file.write(str(line.moved_value) + " " + str(line.depth) + " " +str(line.instance) + "\n")
        file.write(str(total_cost) + " " + str(time_diff))

def output_search(search_arr,filename):
    with(open(filename )) as file:
        for line in search_arr:
            file.write(line)

def output_nosolution(filename):
    with(open(filename, 'w')) as file:
        file.write("no solution")