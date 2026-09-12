class Solution(object):
    def maxDistance(self, colors):
        max_s = 0
        n = len(colors)
        
        # Check furthest from the first house (index 0)
        for r in range(n - 1, -1, -1):
            if colors[r] != colors[0]:
                max_s = max(max_s, r)
                break
                
        # Check furthest from the last house (index n - 1)
        for l in range(n):
            if colors[l] != colors[-1]:
                max_s = max(max_s, n - 1 - l)
                break
                
        return max_s