class Node:
        def __init__(self, key, val):
            self.key = key;
            self.val = val;
            self.prev = self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def addNode(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            resNode: Node = self.cache[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            return resNode.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.deleteNode(self.cache[key])
            del self.cache[key]
        if len(self.cache)==self.capacity:
            lru = self.tail.prev
            self.deleteNode(lru)
            del self.cache[lru.key]
        NodeNow = Node(key,value)
        self.addNode(NodeNow)
        self.cache[key] = NodeNow