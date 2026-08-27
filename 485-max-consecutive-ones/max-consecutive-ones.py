class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_cnt = 0
        cnt = 0
        n = len(nums)
        for i in range(0 , n):
            if nums[i] == 1:
                cnt+=1
                max_cnt = max(max_cnt , cnt)
            else:
                cnt = 0
        return max_cnt        


