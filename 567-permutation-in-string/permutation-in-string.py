class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        m = len(s2)

        if k > m:
            return False

        diff = [0] * 26

        for i in range(k):
            diff[ord(s1[i]) - 97] += 1
            diff[ord(s2[i]) - 97] -= 1
        
        if all(x == 0 for x in diff):
            return True

        for i in range(k, m):
            diff[ord(s2[i]) - 97] -= 1
            diff[ord(s2[i - k]) - 97] += 1

            if all(x == 0 for x in diff):
                return True

        return False