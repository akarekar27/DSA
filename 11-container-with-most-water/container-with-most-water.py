class Solution(object):
    def maxArea(self, height):
        n = len(height)
        low=0
        high=n-1
        maxcurr=0
        while(low<high):
            curr = min(height[low],height[high]) * (high - low)
            maxcurr = max(maxcurr , curr)
            if height[low]<height[high]:
                low+=1
            else:
                high-=1    
        return maxcurr        
