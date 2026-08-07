class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
     

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start
    
    def insert(self, node):
        prev = self.end.prev
        end = self.end
        prev.next = node
        node.next = end
        end.prev = node
        node.prev = prev

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.start.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
