class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        fs = ''
        carry = 0
        if len(a) != len(b):
            b = b.zfill(len(a))
            a = a.zfill(len(b))

        for i in range(len(a) - 1, -1, -1):
            ts = int(a[i]) + int(b[i]) + carry
            if ts == 0:
                fs = '0' + fs;
                carry = 0;
            if ts == 1:
                fs = '1' + fs
                carry = 0
            if ts == 2:
                fs = '0' + fs
                carry = 1
            if ts == 3:
                fs = '1' + fs
                carry = 1
        if carry == 1:
            fs = '1' + fs
        return fs        