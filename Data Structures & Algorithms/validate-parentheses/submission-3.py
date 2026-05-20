class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "}": "{" ,
            ")": "(" ,
            "]": "["
        }
        
        stack = []
        for ch in s:
            if ch not in dic:
                stack.append(ch)
            else:
                if stack:
                    if dic[ch] != stack[-1]:
                        return False
                    stack.pop()
                else:
                    return False
        return len(stack) == 0