with open("statuses.txt") as file_handler:
    indexes = []
    for line in file_handler:
        if line.find('const ') > -1:
            indexes.append(line.split('const ')[1].split(' ')[0])
indexes_set = set(indexes)
results_const = {}
results_without = {}
with open("statuses.txt") as file_handler:
    for line in file_handler:
        line = line.replace('::', ' ').replace('\n','')
        line_set = set(line.split(' '))
        if len(line_set & indexes_set):
            index = list(line_set & indexes_set)[0]
            if line.find('const') > -1:
                results_const[index] = line
            else:
                results_without[index] = line
for result in results_without:
    print(result, results_const[result], results_without[result])


