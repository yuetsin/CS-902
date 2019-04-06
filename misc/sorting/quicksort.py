import time
from random import shuffle

ARRAY_SIZE = 1000000

sample = list(range(ARRAY_SIZE))
shuffle(sample)

# print(sample)

# Quick sort

def split(array, low, high):
    i = low
    x = array[low]
    for j in range(low + 1, high + 1):
        if array[j] <= x:
            i += 1
            if i != j:
                array[i], array[j] = array[j], array[i]
    array[low], array[i] = array[i], array[low]
    return i

def quick_sort(array, low, high):
    if low < high:
        w = split(array, low, high)
        quick_sort(array, low, w - 1)
        quick_sort(array, w + 1, high)


start = time.process_time()


quick_sort(sample, 0, ARRAY_SIZE - 1)
# print(sample)

finish = time.process_time()

time = (finish - start)
speed = time / ARRAY_SIZE
print("time spend: %fs\nspeed index: %f" % (time, speed))
