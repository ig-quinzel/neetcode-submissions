class MyHashSet:

    def __init__(self):
        self.size=1000
        self.buck=[[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        ind=key%self.size
        if key not in self.buck[ind]:
            self.buck[ind].append(key)

    def remove(self, key: int) -> None:
        ind=key%self.size
        if key in self.buck[ind]:
            self.buck[ind].remove(key)    

    def contains(self, key: int) -> bool:
        ind=key%self.size
        if key in self.buck[ind]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)