class Solution(object):
    def pivotIndex(self, nums):
        sum = 0
        for num in nums:
            sum += num
        leftSum = 0
        for i in range(len(nums)):
            rightSum = sum-leftSum-nums[i]
            if leftSum == rightSum:
                return i 
            leftSum += nums[i]
        return -1    
