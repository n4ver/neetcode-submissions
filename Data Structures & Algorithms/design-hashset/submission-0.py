class MyHashSet:

    def __init__(self):
        self.vars = []

    def add(self, key: int) -> None:
        if key not in self.vars: self.vars.append(key)

    def remove(self, key: int) -> None:
        if key in self.vars: self.vars.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.vars
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)