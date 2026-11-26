class MyHashMap:

    def __init__(self):
        self.keys = []
        self.vals = []

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.vals[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.vals.append(value)

    def get(self, key: int) -> int:
        if key not in self.keys: return -1
        return self.vals[self.keys.index(key)]

    def remove(self, key: int) -> None:
        if key in self.keys:
            self.vals[self.keys.index(key)] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)