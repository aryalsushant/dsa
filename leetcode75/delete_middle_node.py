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
        #its like the "find the middle node problem" only change i'd have
        #to do is skip the middle node by connecting slow.next to the node
        #previous to slow
        if head == None or head.next == None:
            return None
        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev = slow #prev tracks the node below the slow
            slow = slow.next
            fast = fast.next.next
        #now attach prev to slow.next, so slow is skipped
        prev.next = slow.next

        return head

        