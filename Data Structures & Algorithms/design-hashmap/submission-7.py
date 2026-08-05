class MyHashMap:

    def __init__(self):
        self.size=10
        self.buck=[[]for _ in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        ind=key%self.size
        for i in range(len(self.buck[ind])):
            k,v=self.buck[ind][i]
            if k==key:
                self.buck[ind][i]=((key,value))
                return
        self.buck[ind].append((key,value))

    def get(self, key: int) -> int:
        ind=key%self.size
        for i in range(len(self.buck[ind])):
            k,v=self.buck[ind][i]
            if k==key:
                return v
        return -1
        
    def remove(self, key: int) -> None:
        ind=key%self.size
        for i in range(len(self.buck[ind])):
            k,v = self.buck[ind][i]
            if k==key:
                del self.buck[ind][i]
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)