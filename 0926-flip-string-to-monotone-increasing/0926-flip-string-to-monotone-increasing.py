class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        min = len(s)
        tz = [0] * len(s)
        to = [0] * len(s)
        if s[0] == '1':
            tz[0] = 1
        if s[len(s) - 1] == '0':
            to[len(s) - 1] = 1

        for i in range(1, len(s)):
            tz[i] = tz[i - 1] + int(s[i])

        for i in range(len(s) - 2, -1, -1):
            to[i] = to[i + 1] + 1 - int(s[i])
        for i in range(len(s) - 1):
            if tz[i] + to[i + 1] < min:
                min = tz[i] + to[i + 1]
        if tz[len(s) - 1] < min:
            min = tz[len(s) - 1]
        if to[0] < min:
            min = to[0]
        return min
        