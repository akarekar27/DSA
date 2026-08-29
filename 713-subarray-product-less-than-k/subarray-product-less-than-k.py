class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if (k<=1):
            return 0
        l = 0
        r = 0
        count = 0
        prod = 1

        for r in range(0 , len(nums)):
            prod *= nums[r]
            while (prod >= k):
                prod = prod//nums[l]
                l+=1
            count += (r-l+1)   
        return count     
