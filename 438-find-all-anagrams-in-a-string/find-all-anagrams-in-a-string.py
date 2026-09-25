class Solution:

    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        pCount, sCount = {}, {}

        # 1. Build initial frequency maps for length len(p)
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        l = 0

        # 2. Slide the window across string s
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)

            # Remove character going out of window
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l += 1  # l now points to the new start index of the window

            if sCount == pCount:
                res.append(l)

        return res