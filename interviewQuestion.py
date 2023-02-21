# Check if the array of integers has duplicates

import time, random
import numpy as np



def has_repeated(integers):
    for number in integers:
        if integers.count(number) > 1:
            return True
    return False

def has_repeated_optimised(integers):
    integers.sort()
    for i in range(len(integers) - 1):
        if integers[i] == integers[i + 1]:
            return True
    return False

def has_repeated_best(integers):
    return len(integers) != len(set(integers))

def has_repeated_numpy(integers):
    return len(np.unique(integers)) < len(integers)





integers = [random.randint(0, 1000000) for num in range(1000000)]


# start = time.time()
# print(has_repeated(integers))
# print('%s seconds' %(time.time() - start))


# start = time.time()
# print(has_repeated_optimised(integers))
# print('%s seconds' %(time.time() - start))

# start = time.time()
# print(has_repeated_best(integers))
# print('%s seconds' %(time.time() - start))

# start = time.time()
# print(has_repeated_numpy(np.array(integers)))
# print('%s seconds' %(time.time() - start))
