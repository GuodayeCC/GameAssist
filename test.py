import numpy as np

l = [['1', 'dog', 'dog', 'cat'],
 ['2', '2', 'dog', 'cat'],
 ['3', 'dog', 'dog', 'cat']]
arr = np.array(l)
names = [['']*4 for i in range(3)]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        names[i][j] = arr[i][j]

names[0][1] = "hhhhh"

print(names)