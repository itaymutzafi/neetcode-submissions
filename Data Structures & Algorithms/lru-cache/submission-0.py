class ListNode:
    def __init__(self, val = 0, key = 0, nex = None, prev = None):
        self.val = val
        self.nex = nex
        self.prev = prev
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        # LRU -> Linked List of the LRU, and dict for keys.
        self.cache = {}
        self.head = ListNode() # head is the last used node
        self.tail = ListNode() # tail is the node to delete
        self.head.prev = self.tail
        self.tail.nex = self.head
        self.capacity = capacity

    def _delete_node(self, node):
        prev_node = node.prev
        next_node = node.nex
        prev_node.nex = next_node
        next_node.prev = prev_node
    
    def _insert_to_head(self, node):
        tmp_head = self.head.prev
        self.head.prev = node
        tmp_head.nex = node
        node.prev = tmp_head
        node.nex = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            curr = self.cache[key]
            self._delete_node(curr)
            self._insert_to_head(curr)
            return curr.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            curr = self.cache[key]
            curr.val = value
            self._delete_node(curr)
            self._insert_to_head(curr)
            return

        if self.capacity == len(self.cache):
            tmp = self.tail.nex
            self._delete_node(tmp)
            del self.cache[tmp.key]

        new_node = ListNode(value, key)
        self._insert_to_head(new_node)
        self.cache[key] = new_node                          
