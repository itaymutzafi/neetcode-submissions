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
                    last = stack.pop()
                    if dic[ch] != last:
                        return False
                else:
                    return False
        return len(stack) == 0