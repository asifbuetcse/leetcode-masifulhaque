# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            head = None;
        else:
            slow = head
            slowParent = head
            fast = head
            while fast.next and fast.next.next:
                slowParent = slow;
                slow = slow.next;
                fast = fast.next.next;

            if fast.next != None:
                slowParent = slow;
                slow = slow.next;
            slowParent.next = slow.next;
        return head;
        