class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        r = 0
        max_len = 0

        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0)+1
            while(mp[s[r]]) > 1:
                mp[s[l]] -=1
                l+=1
            max_len = max(r-l+1 , max_len)
        return max_len     
    