class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, len(days)):
            days[i] = days[i - 1] + days[i]
        days.insert(0,0)
        return max(min(days[int(leaveAlice.split('-')[0])-1]
                  + int(leaveAlice.split('-')[1]), days[int(leaveBob.split('-'
                  )[0])-1] + int(leaveBob.split('-')[1]))
                  - max(days[int(arriveAlice.split('-')[0])-1]
                  + int(arriveAlice.split('-')[1]), days[int(arriveBob.split('-'
                  )[0])-1] + int(arriveBob.split('-')[1])) + 1, 0)