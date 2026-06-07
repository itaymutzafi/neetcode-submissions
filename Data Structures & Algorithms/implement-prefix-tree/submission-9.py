class Node:
    def __init__(self, val = "", neighbors = None):
        self.neighbors = {} if not neighbors else neighbors
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:         
        curr = self.root
        for i in range(len(word)):
            tmp = word[i]
            if tmp not in curr.neighbors:
                curr.neighbors[tmp] = Node(tmp)
            curr = curr.neighbors[tmp]
        curr.isEnd = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            tmp = word[i]
            if tmp in curr.neighbors:
                curr = curr.neighbors[tmp]
            else:
                return False
        return curr.isEnd
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            tmp = prefix[i]
            if tmp in curr.neighbors:
                curr = curr.neighbors[tmp]
            else:
                return False
        return True
        
        