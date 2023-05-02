def unpak(name_file, list):
    list.append(name_file)
    with open(name_file) as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            list.append(line)
    f.close()
    return list


line_list = []
liner = []

for i in range(4):
    file_name = str(i + 1) + '.txt'
    line_list = unpak(file_name, line_list)
    liner.append(line_list)
    line_list = []

for i in range(4):
    liner[i].insert(1, len(liner[i]) - 1)

list_sorted = []
tuppl = tuple()

for i in range(4):
    tuppl = (len(liner[i]) - 2, liner[i])
    list_sorted.append(tuppl)

list_sorted.sort()

with open(r'out.txt', 'w') as f:
    for i in range(4):
        for line in list_sorted[i][1]:
            f.write(str(line) + '\n')

f.close()