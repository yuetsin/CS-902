import time
from random import shuffle

ARRAY_SIZE = 1000000

sample = list(range(ARRAY_SIZE))
shuffle(sample)

# print(sample)

def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = int(len(lists) / 2)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)




start = time.process_time()


merge_sort(sample)


finish = time.process_time()

time = (finish - start)
speed = time / ARRAY_SIZE
print("time spend: %fs\nspeed index: %f" % (time, speed))

# print(sample)
