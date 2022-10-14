class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        s = 0
        push = 1
        while push & xor == 0:
            s += 1
            push = push << 1
        otherXor = 0
        for item in nums:
            if item & push > 0:
                otherXor = otherXor ^ item
        return[otherXor, otherXor ^ xor]
        