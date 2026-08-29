class Solution(object):
    def isAnagram(self, s, t):
        res = []
        if len(s)!=len(t):
            return False
        for ch in s:
            res.append(ch)
        for ch in t:
            if ch in res:
                res.remove(ch)
            else :
                return False  
        return True          
            
