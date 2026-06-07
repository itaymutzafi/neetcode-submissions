class RandomizedSet:

    def __init__(self):
        self.L = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.L.append(val)
        self.d[val] = len(self.L) - 1
        # every val is in the d only once, since this is a set
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        i = self.d[val]
        if i != len(self.L) - 1:
            self.d[self.L[-1]] = i
            self.L[-1], self.L[i] = self.L[i], self.L[-1]
        self.L.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.L)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()