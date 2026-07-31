# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force solution would be to extract the array
        result_array = []
        while head:
            result_array.append(head.val)
            head = head.next
        # reverse the array and
        result_array.reverse()
        print(result_array)
        # create the new linked list out of array
        if len(result_array) == 0:
            return None

        result_head = ListNode(result_array[0])
        curr = result_head
        for i in range(1, len(result_array)):
            curr.next = ListNode(result_array[i])
            curr = curr.next 
        # return the newly created linked list
        return result_head