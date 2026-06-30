# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        p = head
        while p:
            values.append(p.val)
            p = p.next
        
        p = head
        
        print("values", values)

        while p:
            p.val = values.pop()
            p = p.next
        
        return head