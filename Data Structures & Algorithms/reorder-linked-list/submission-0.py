# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        l = head
        r = head
        prev_r = None

        while l and l.next:
            while r.next:
                prev_r = r
                r = r.next

            tmp = r
            prev_r.next = None
            tmp.next = l.next
            l.next = tmp

            # move the pointers
            l = tmp.next
            r = head
            
        


            