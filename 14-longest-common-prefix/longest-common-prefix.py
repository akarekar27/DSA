class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
            
        result = ""
        base = strs[0]
        for i in range(0 , len(base)):
            for ch in strs[1:]:
                if i == len(ch) or ch[i]!=base[i]:
                    return result

            result+=base[i] 
        return result               