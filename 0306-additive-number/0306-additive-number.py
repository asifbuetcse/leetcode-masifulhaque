class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        finalResult = False


        def check(a, b, c):
            insertedIntoWhile = False

          # print a, b, c, int(a) + int(b), i, j, type(c)

            while len(c) > 0 and c.startswith(str(int(a) + int(b))):

            # print "djilse", a,b,c

                if str(a).startswith('0') and len(str(a)) > 1 \
                    or str(b).startswith('0') and len(str(b)) > 1:
                    break
                insertedIntoWhile = True
                c = c[len(str(int(a) + int(b))):]
                (a, b) = (b, int(a) + int(b))

            # print "inside while", a, b, c

            if insertedIntoWhile:
                if len(c) == 0:
                    return True

              # print "wow"

            return False


        for i in range(int(len(num) / 2) + 1):
            if finalResult == True:
                break
            a = num[0:i + 1]

          # print "aaaaa", a

            for j in range(i + 1, len(num)):
                if finalResult == True:
                    break
                b = num[i + 1:j + 1]

            # print "bbbb", a, b

                c = num[j + 1:len(num)]
                funcResult = check(a, b, c)

            # print funcResult

                if funcResult == True:
                    finalResult = True
                    break
        return finalResult
