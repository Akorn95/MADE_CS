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

