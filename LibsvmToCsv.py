import sys
import csv
import numpy as np


def empty_table(input_file):
    max_feature = 0
    count = 0
    with open(input_file, 'r', newline='\n') as f:
        reader = csv.reader(f, delimiter=" ")
        for line in reader:
            count += 1
            for i in line:
                try:
                    num = int(i.split(":")[0])
                    if num > max_feature:
                        max_feature = num
                except:
                    pass
    
    return np.zeros((count, max_feature + 1))


def write(input_file, output_file, table):
    with open(input_file, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=" ")
        for c, line in enumerate(reader):
            label = line.pop(0)
            table[c, -1] = label
            if line[-1].strip() == '':
                line.pop(-1)

            line = map(lambda x : tuple(x.split(":")), line)
            for i, v in line:
                i = int(i)
                table[c, i-1] = v
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list(range(1, table.shape[1])) + ["target"])
        for line in table:
            writer.writerow(line)




if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    table = empty_table(input_file)
    write(input_file, output_file, table)