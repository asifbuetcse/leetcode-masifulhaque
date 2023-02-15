class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [int(x) for x in str(k)]
        f = []

        if len(num) > len(res):
            diff = len(num) - len(res)
            nar = [0] * diff
            nar.extend(res)
            res = nar

        if len(num) < len(res):
            diff = len(res) - len(num)
            nar = [0] * diff
            nar.extend(num)
            num = nar

        cr = 0
        for i in range(len(num) - 1, -1, -1):
            s = num[i] + res[i] + cr
            if s > 9:
                f.insert(0, s % 10)
                cr = int(s / 10)
            else:
                f.insert(0, s)
                cr = 0
        if cr > 0: f.insert(0, cr)
        return f        