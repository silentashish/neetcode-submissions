# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Brute force
        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        length_nodes = len(nodes)
        rm_target = length_nodes - n

        # Remove the target node from the array
        nodes = nodes[:rm_target] + nodes[rm_target + 1:]

        # If the list is now empty
        if not nodes:
            return None

        # Rebuild the links
        head = nodes[0]
        curr = head
        for i in range(1, len(nodes)):
            curr.next = nodes[i]
            curr = curr.next

        # Important: terminate the list
        curr.next = None

        return head