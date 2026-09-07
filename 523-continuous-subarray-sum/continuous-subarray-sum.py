class Solution(object):
    def checkSubarraySum(self, nums, k):
        my_dict = {0:-1}
        prefix = 0
        for i in range(len(nums)):
            prefix+=nums[i]

            rem = prefix % k
            if rem in my_dict:
                if i - my_dict[rem] >=2:
                    return True
            else:
                my_dict[rem] = i
        return False           
