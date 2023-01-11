class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        sign = 1
        state = 0
        for item in s:

          # print "universal value"
          # print item

            if state == 0:

            # print "state 0"
            # print item

                if item == ' ':
                    continue
                else:
                    state = 1
            if state == 1:

            # print "state 1"
            # print item

                state = 2
                if item == '-':
                    sign = -1
                    continue
                if item == '+':
                    continue
            if state == 2:

            # print "state 2"
            # print item

                if item.isnumeric():

              # print "eita numeric"

                    result = result * 10 + int(item)
                    if result > 2147483648:
                        break
                    continue
                else:
                    break

          # print "res " + result;

            if result > 2147483648:
                break
        result = result * sign
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
        return result        