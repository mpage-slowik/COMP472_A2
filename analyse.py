
from os import walk
import sys


def anal(algorithm, file_names):
    total_solution_length=0
    total_search_length=0
    total_no_solution=0
    total_cost=0
    total_execution_time=0
    optimality_solution_path = "not sure what this is"
    file_as_list = []
    route_costs = []
    for file_name in file_names:
        if algorithm in file_name:
            if "solution" in file_name:
                with open(f'./output/{file_name}', 'r') as reader:
                    file_as_list = list(reader)
                    if "no solution" == file_as_list[0]:
                        total_no_solution = total_no_solution + 1
                        route_costs.append(sys.maxsize)
                    else:
                        total_solution_length = total_solution_length + len(file_as_list) -1
                        total_cost = total_cost + int(file_as_list[-1].split(" ")[0])
                        route_costs.append(int(file_as_list[-1].split(" ")[0]))
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
        'average search length':f'{total_search_length/num_of_valid_sol}',
        'total cost': f'{total_cost}',
        'average cost':f'{total_cost/num_of_valid_sol}',
        'total execution time':f'{total_execution_time}',
        'average execution time':f'{total_execution_time/num_of_valid_sol}',
        'route_costs': route_costs
    }


if __name__ == "__main__":
    algos = ["ucs", "gbfs-h1", "gbfs-h2", "astar-h1", "astar-h2"]
    file_names = list()
    for (dirpath, dirnames, filenames) in walk("./output"):
        file_names.extend(filenames)
    analysis = list()
    output = ","
    for algo in algos:
        output = f'{output}{algo},'
        analysis.append(anal(algo, file_names))
    output = f'{output}\n'
    for key in analysis[0]:
        if key =='route_costs':
            continue
        output = f'{output}{key},'
        for analy in analysis:
            output = f'{output}{analy[key]},'
        output = f'{output}\n'
    
    best_algos = {}
    for i in range(len(analysis[0]['route_costs'])):
        best = analysis[0]['route_costs'][i]
        for index in range(len(algos)):
            if best > analysis[index]['route_costs'][i]:
                best = analysis[index]['route_costs'][i]
        for index in range(len(algos)):
            if  best == analysis[index]['route_costs'][i]:
                if best_algos.get(algos[index], None) == None:
                    best_algos[algos[index]] = 1
                else:
                    best_algos[algos[index]] = best_algos[algos[index]]+1
    
    output = f'{output}# of optimal paths,'
    for algo in algos:
        output = f'{output}{best_algos[algo]},'
    with open("./analysis.csv", 'w') as f:
        f.write(output)
    print("result can be found in analysis.csv open it in excel")