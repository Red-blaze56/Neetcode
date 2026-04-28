class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.S = []

    def get(self, key: int) -> int:
        print("get->",self.cache)
        if key in self.S:
            self.S.remove(key)
            self.S.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.S:
            self.cache[key]=value
            self.S.remove(key)
        elif len(self.cache)>=self.capacity:
            old = self.S.pop(0)
            del self.cache[old]
        self.cache[key]=value
        self.S.append(key)
        print("put->",self.cache)