# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0, head)
        new_head = prev
        curr = prev
        tail = prev

        while n:
            tail = tail.next
            n -= 1

        print("tail", tail.val)
        
        while tail:
            prev = curr
            curr = curr.next
            tail = tail.next
        print("at the end of tail", tail, "curr", curr.val, "prev", prev.val)

        tmp = curr.next
        curr.next = None
        prev.next = tmp

        return new_head.next

