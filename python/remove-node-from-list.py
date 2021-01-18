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
        count = 0
        toremove = 0
        nextnode = head
        while nextnode is not None:
            count += 1
            nextnode = nextnode.next
        if count == 1 and n == 1:
            return ListNode("")
        toremove = count - n
        if toremove == 0:
            return head.next
        headnode = head
        for i in range(count):
            prev = headnode
            headnode = headnode.next
            if i == toremove-1:
                headnode = headnode.next
                prev.next = headnode
                break
        return head
                
