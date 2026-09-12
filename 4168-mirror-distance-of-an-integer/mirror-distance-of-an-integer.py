class Solution(object):
    def mirrorDistance(self, n):
        rev = str(n)[::-1]
        a = int(rev)

        return abs(a - n)
        