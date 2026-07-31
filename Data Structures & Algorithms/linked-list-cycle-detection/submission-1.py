# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit_map = {}
        curr = head

        prev = ListNode()
        while curr:
            if (curr.val in visit_map) and visit_map[curr.val] == prev.val:
                return True
            else:
                visit_map[curr.val] =  prev.val
            prev = curr
            curr = curr.next
        return False