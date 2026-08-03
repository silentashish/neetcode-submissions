# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        target_pos = length - n

        # Remove the head
        if target_pos == 0:
            return head.next

        curr = head
        l = 0

        # Stop at the node before the one to remove
        while curr:
            if l == target_pos - 1:
                curr.next = curr.next.next
                break

            curr = curr.next
            l += 1

        return head