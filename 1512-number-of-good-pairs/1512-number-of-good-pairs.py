class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        goodPair = 0
        i = 0
        while i <= len(nums) - 1:
            j = i + 1
            while j <= len(nums) - 1 and nums[j] == nums[i]:
                j += 1
            j -= 1
            if j > i:
                goodPair += (j - i + 1) * (j - i) / 2
                i = j + 1
            else:
                i += 1
        return int(goodPair)        