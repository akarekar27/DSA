class Solution(object):
    def shuffle(self, nums, n):
        ar = []
        for i in range(n):
            ar.append(nums[i]) 
            ar.append(nums[i+n])
        return ar    