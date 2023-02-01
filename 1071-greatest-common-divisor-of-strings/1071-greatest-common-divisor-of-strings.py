class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def isDivisible(target, source):
            while len(target) > 0:
                if target.startswith(source):
                    target = target[len(source):]
                else:
                    return False
            return True


        s = ''
        b = ''
        lp = ''
        if len(str1) > len(str2):
            b = str1
            s = str2
        else:
            b = str2
            s = str1

        for i in range(1, len(s) + 1):
            sm = s[:i]
            if isDivisible(s, sm):
                if isDivisible(b, sm):
                    lp = sm

        return lp