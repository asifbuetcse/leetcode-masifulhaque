class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        j = -1
        tempArray = [0] * 32
        maxDiff = 0
        binaryArray = [] * len(nums)
        for item in nums:
            x = [int(d) for d in str(bin(item))[2:]]
            x.reverse()
            x = x + [0] * (32 - len(x))
            binaryArray.append(x)
        while j < len(nums):
            if 2 in tempArray:
                while 2 in tempArray:
                    if j - p > maxDiff:
                        maxDiff = j - p
                    x = binaryArray[p]
                    tempArray = [x1 - x2 for x1, x2 in zip(tempArray, x)]
                    p = p + 1
            else:
                j += 1
                if j >= len(nums):
                    break
                x = binaryArray[j]
                tempArray = [x1 + x2 for x1, x2 in zip(tempArray, x)]
        if j - p > maxDiff:
            maxDiff = j - p
        return maxDiff

        