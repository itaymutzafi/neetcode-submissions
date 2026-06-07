class RandomizedSet:

    def __init__(self):
        self.L = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return
        self.L.append(val)
        self.d[val] = len(self.L) - 1
        # every val is in the d only once, since this is a set

    def remove(self, val: int) -> bool:
        if not val or val not in self.d or not self.L:
            return 
        i = self.d[val]
        if i != len(self.L) - 1:
            self.d[self.L[-1]] = i
            self.L[-1], self.L[i] = self.L[i], self.L[-1]
        self.L.pop()
        del self.d[val]

    def getRandom(self) -> int:
        if not self.L:
            return None
        i = random.randint(0,len(self.L) - 1)
        return self.L[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()