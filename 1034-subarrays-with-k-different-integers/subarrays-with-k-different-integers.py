class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.atMost(nums,k) - self.atMost(nums, k-1)
    def atMost(self , nums , k):    
        my_dict = {}
        l = 0
        r = 0
        count = 0
        for r in range(0 , len(nums)):
            my_dict[nums[r]] = my_dict.get(nums[r],0)+1
            while len(my_dict)>k:
                my_dict[nums[l]]-=1
                if my_dict[nums[l]] == 0:
                    del my_dict[nums[l]]
                l+=1    
            count += (r-l+1)
        return count    