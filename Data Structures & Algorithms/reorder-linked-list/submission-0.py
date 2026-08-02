# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_item = []

        # Convert linked list to array
        curr = head
        while curr:
            list_item.append(curr.val)
            curr = curr.next

        n = len(list_item)
        rlist_item = list_item[::-1]
        order_list = []

        mid = (n + 1) // 2

        for i in range(n // 2):
            order_list.append(list_item[i])
            order_list.append(rlist_item[i])

        # Add middle element if length is odd
        if n % 2 == 1:
            order_list.append(list_item[mid - 1])

        # Overwrite the original linked list
        curr = head
        for val in order_list:
            curr.val = val
            curr = curr.next