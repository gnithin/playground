import concurrent.futures

import config
from queue import Queue
import math

sort_q = Queue()
threshold_len = 10


# Create a recursive algo -
def get_through(st_index, e_index):
    if (e_index - st_index) > threshold_len:
        mid = math.floor((st_index + e_index)/2)
        s1 = get_through(st_index, mid)
        s2 = get_through(mid+1, e_index)
        return s1 if s1 < s2 else s2
    else:
        return max(range(st_index, e_index+1))

def pivot(st_index, e_index):
    v = get_through(st_index, e_index)
    sort_q.put(v)

# Removing the list to the starting and the ending index
def find_max(s_ind, e_ind):
    sort_q.put(max(range(s_ind, e_ind+1)))

# Why is this soo crappy!!!???
grouping = 100
with concurrent.futures.ThreadPoolExecutor(
     max_workers=config.num_workers) as executor:
    for i in range(0, config.limit, grouping):
        executor.submit(get_through, i, i+grouping)

# Resolving this is also a problem
resolver = []
while not sort_q.empty():
    resolver.append(sort_q.get())

print(max(resolver))
