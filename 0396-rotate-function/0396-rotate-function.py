class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ini = 0
        tot = sum(nums)
        for i in range(len(nums)):
            ini = ini + i * nums[i]
        m = ini
        for i in range(len(nums) - 1):
            temp = ini - tot + nums[i] * len(nums)
            ini = temp
            if ini > m:
                m = ini
        return m        