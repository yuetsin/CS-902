import time
from random import shuffle

ARRAY_SIZE = 10000

sample = list(range(ARRAY_SIZE))
shuffle(sample)

# print(sample)


def shell_sort(lists):
    count=len(lists)
    step=2
    group=int(count/step)
    while group > 0:
        for i in range(group):
            j=i+group
            while j<count:
                key=lists[j]
                k=j-group
                while k>=0:
                    if lists[k]>key:
                        lists[k+group]=lists[k]
                        lists[k]=key
                    k=k-group
                j=j+group
        group = int(group / step)


start = time.process_time()


shell_sort(sample)


finish = time.process_time()

time = (finish - start)
speed = time / ARRAY_SIZE
print("time spend: %fs\nspeed index: %f" % (time, speed))

# print(sample)
