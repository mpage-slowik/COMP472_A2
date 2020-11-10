
from os import walk


def anal(algorithm):
    total_solution_length=0
    total_search_length=0
    total_no_solution=0
    total_cost=0
    total_execution_time=0
    optimality_solution_path = "not sure what this is"
    file_names = list()
    for (dirpath, dirnames, filenames) in walk("./output"):
        file_names.extend(filenames)
    file_as_list = []
    for file_name in file_names:
        if algorithm in file_name:
            if "solution" in file_name:
                with open(f'./output/{file_name}', 'r') as reader:
                    file_as_list = list(reader)
                    if "no solution" == file_as_list[0]:
                        total_no_solution = total_no_solution + 1
                    else:
                        total_solution_length = total_solution_length + len(file_as_list) -1
                        total_cost = total_cost + int(file_as_list[-1].split(" ")[0])
                        total_execution_time = total_execution_time + float(file_as_list[-1].split(" ")[1])
            if "search" in file_name:
                with open(f'./output/{file_name}', 'r') as reader:
                    file_as_list = list(reader)
                    if "no solution" != file_as_list[0]:
                        total_search_length = total_search_length + len(file_as_list) -1
    num_of_valid_sol = 50 - total_no_solution
    return {
        'total no solution':f'{total_no_solution}',
        'percent no solution':f'{total_no_solution/50 * 100}%',
        'total solution length':f'{total_solution_length}',
        'average solution length':f'{total_solution_length/num_of_valid_sol}',
        'total search length':f'{total_search_length}',
        'avarage search length':f'{total_search_length/num_of_valid_sol}',
        'total cost': f'{total_cost}',
        'average cost':f'{total_cost/num_of_valid_sol}',
        'total execution time':f'{total_execution_time}',
        'average execution time':f'{total_execution_time/num_of_valid_sol}',
    }


if __name__ == "__main__":
    algos = ["ucs", "gbfs-h1", "gbfs-h2", "astar-h1", "astar-h2"]
    analysis = list()
    col_width = 23
    col_1_width = 30
    print("".join(" ".ljust(col_1_width)), end="")
    for algo in algos:
        print("".join(algo.ljust(col_width)), end="")
        analysis.append(anal(algo))
    print('')
    for key in analysis[0]:
        print("".join(key.ljust(col_1_width)), end="")
        for analy in analysis:
            print("".join(analy[key].ljust(col_width)), end="")
        print('')
    