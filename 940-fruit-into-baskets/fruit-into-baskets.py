class Solution(object):
    def totalFruit(self, fruits):
        max_len=0
        l = 0
        r = 0
        my_dict = {}
        while r<len(fruits):
            my_dict[fruits[r]] = my_dict.get(fruits[r],0)+1
            if len(my_dict)>2:
                my_dict[fruits[l]]-=1
                if my_dict[fruits[l]]==0:
                    del my_dict[fruits[l]]
                l+=1
            if len(my_dict)<=2:
                max_len = max(max_len , r-l+1)
            r+=1
        return max_len      

        