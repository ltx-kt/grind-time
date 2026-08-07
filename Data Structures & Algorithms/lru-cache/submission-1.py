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

    def insert(self, node: Node):
        p = self.end.prev
        p.next = node
        node.next = self.end
        self.end.prev = node
        node.prev = p

    def remove(self, node: Node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
        

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
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]
        
