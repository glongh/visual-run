from collections import OrderedDict
'''
Cache Eviction Flow
# get(i)
if i in cache:
    return cache[i]
else:
# set(i, m) 
    x = longest-in-the-past from cache
    evict x, add i to cache
    return cache[i]
'''


class CacheLRU():
    def __init__(self, size: int) -> None:
        self.size = size
        self.cache = OrderedDict()

    def get(self, key: str) -> str or False:
        if key not in self.cache:
            return False
        else:
            # Move to the key to the end to demonstrate if was recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: str, item: str) -> None:
        # Oa (Parts): cache consists of parts of a solution
        # Cache eviction manager starts to builds up.
        self.cache[key] = item

        # [Ob (Greed used): All changes to 'cache' have been "additive", when a key is evicted, there is no backtrack,
        #  and "optimizing" based on information available at the time, in this case what it is available in the 'cache'
        #  at the time of the request.
        # Greedy step: Evict an item when needed. Evict the element which is Least Recently Used.

        # 1: Moves the key to the end to indicate if was recently used.
        self.cache.move_to_end(key)

        # 2: If the size has been exceeded, we remove the first key, the "Least Recently Used"
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

        # Oc (Complete): 'cache' is completely build.