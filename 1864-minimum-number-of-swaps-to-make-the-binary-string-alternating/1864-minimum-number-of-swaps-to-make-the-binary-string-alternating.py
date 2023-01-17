class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        c1 = 0
        c2 = 0
        p1 = 0
        p2 = 0
        min = -1
        for i in range(len(s)):
            target = ''
            if i % 2 == 0:
                target = '1'
            else:
                target = '0'
            if s[i] != target:
                c1 += 1
                if s[i] == '1':
                    p1 += 1
                else:
                    p1 -= 1

        for i in range(len(s)):
            target = ''
            if i % 2 != 0:
                target = '1'
            else:
                target = '0'
            if s[i] != target:
                c2 += 1
                if s[i] == '1':
                    p2 += 1
                else:
                    p2 -= 1

        if p1 == 0:
            min = c1 / 2
        if p2 == 0 and (c2 / 2 < min or min == -1):
            min = c2 / 2
        return min

        