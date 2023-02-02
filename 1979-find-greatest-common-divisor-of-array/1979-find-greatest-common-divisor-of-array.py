class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = min(nums)
        y = max(nums)
        while(y):
            x, y = y, x % y
        return abs(x)
      