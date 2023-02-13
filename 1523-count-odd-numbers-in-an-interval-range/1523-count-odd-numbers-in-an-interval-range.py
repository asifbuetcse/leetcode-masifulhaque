class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if (high - low + 1) % 2 == 0:
            return int((high - low + 1) / 2)
        else:
            if low % 2 == 0:
                return int((high - low) / 2)
            else:
                return int((high - low) / 2 + 1)        