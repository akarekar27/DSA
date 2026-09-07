class Solution:

  def checkSubarraySum(self, nums: list[int], k: int) -> bool:
    # Early exit for arrays shorter than 2
    n = len(nums)
    if n < 2:
      return False

    # Check for consecutive zeros edge case immediately (O(n) pass)
    for i in range(n - 1):
      if nums[i] == 0 and nums[i + 1] == 0:
        return True

    # Hash table storing earliest index for each remainder
    seen = {0: -1}
    prefix = 0

    for i, x in enumerate(nums):
      prefix = (prefix + x) % k
      prev_idx = seen.setdefault(prefix, i)
      if i - prev_idx >= 2:
        return True

    return False