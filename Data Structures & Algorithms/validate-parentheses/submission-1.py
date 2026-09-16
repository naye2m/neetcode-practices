class Solution:
    def isValid(self, s: str) -> bool:
        opps = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        opening_brs = "{[("
        
        c=[]
        for x in s:
            print(x,"".join(c))
            if x in opening_brs: c.append(x)
            elif x in opps and not len(c): return False
            elif len(c) and c.pop() != opps[x]: return False
            
        
        return not len(c)
