class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        dict = {}
        globalMin = -1
        for i in range(len(cards)):
            if cards[i] in dict:
                if globalMin == -1 or globalMin > i - dict[cards[i]] + 1:
                    globalMin = i - dict[cards[i]] + 1
            dict[cards[i]] = i
        return globalMin       