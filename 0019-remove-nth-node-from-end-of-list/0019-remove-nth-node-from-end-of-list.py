# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            head = None;
        else:
            first = head
            firstParent = head
            second = head
            for i in range(n-1):
                second = second.next
            while second.next != None:
                firstParent = first;
                first =first.next;
                second = second.next;
            if firstParent == first:
                head = head.next
            else: firstParent.next = first.next
        return head