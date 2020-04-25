from collections import deque

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key):
        value = self.cache.get(key, -1)
        if value != -1:
            self.queue.remove(key)
            self.queue.append(key)
        return value

    def put(self, key, value):
        if self.cache.get(key, None) is None:
            if len(self.cache) == self.capacity:
                least_recently_used = self.queue.popleft()
                del self.cache[least_recently_used]
        else:
            self.queue.remove(key)
        self.cache[key] = value
        self.queue.append(key)