import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = ["+", "-", "*", "/"]
        self.res = 0
        s = []
        
        for tok in tokens:
            if tok in oper:
                second = s.pop()
                first = s.pop()
                if tok == "+":
                    s.append(first + second)
                elif tok == "*":
                    s.append(first * second)
                elif tok == "/":
                    if first < 0 or second < 0:
                        s.append(math.ceil(first / second))
                    else:
                        s.append(math.floor(first / second))
                else:
                    s.append(first - second)
            else:
                s.append(int(tok))
            print(s)
        
        return s[0]
                

                
            
            
            