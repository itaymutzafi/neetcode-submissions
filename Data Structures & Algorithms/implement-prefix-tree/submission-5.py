class Node:
    def __init__(self, val = "", neighbors = None):
        self.val = val
        self.neighbors = [] if not neighbors else neighbors
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:         
        curr = self.root
        for i in range(len(word)):
            tmp = word[:i+1]
            to_ins = True
            for neigh in curr.neighbors:
                if neigh.val == tmp:
                    to_ins = False
                    curr = neigh
                    break
            if to_ins:
                new_node = Node(tmp)
                curr.neighbors.append(new_node)
                curr = new_node
        curr.isEnd = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            tmp = word[:i+1]
            for neigh in curr.neighbors:
                if neigh.val == tmp:
                    curr = neigh
                    break
            if curr.val != tmp:
                return False
        return curr.isEnd
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            tmp = prefix[:i+1]
            for neigh in curr.neighbors:
                if neigh.val == tmp:
                    curr = neigh
                    break
            if curr.val != tmp:
                return False
        return curr.val == prefix
        
        