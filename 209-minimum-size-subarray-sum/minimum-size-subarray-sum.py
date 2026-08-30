class Solution(object):
    def minSubArrayLen(self, target, nums):
        sum = 0
        ans = max
        l = 0
        r = 0
        for r in range (0 , len(nums)):
            sum+=nums[r]
            while sum >= target:
                ans = min(ans , r-l+1)
                sum-=nums[l]
                l+=1
        if ans == max:
            return 0
        else :
            return ans           