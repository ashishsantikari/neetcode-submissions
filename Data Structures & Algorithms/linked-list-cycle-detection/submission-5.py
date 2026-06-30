# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        # visited = {}
        # curr = head

        # while curr:
        #     if curr.val in visited and visited[curr.val] == curr.next:
        #         return True
        #     visited[curr.val] = curr.next
        #     curr = curr.next
        
        # return False

        ptr1 = head
        ptr2 = head.next


        while ptr1 and ptr2 and ptr1.next and ptr2.next and ptr2.next.next:
            if ptr1.val == ptr2.val:
                return True
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        
        return False


