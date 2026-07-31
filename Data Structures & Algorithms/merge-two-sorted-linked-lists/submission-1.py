# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        
        if not list2:
            return list1
        
        # initalize the list with the greater items
        result = ListNode(list1.val if list1.val <list2.val else list2.val)
        if list1.val <list2.val:
            list1 = list1.next
        else:
            list2 = list2.next

        curr = result
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
       
        # handle case when list2 is empty and list1 still have items
        while list1:
            curr.next = ListNode(list1.val)
            list1 = list1.next
            curr = curr.next

        # handle case when list1 is empty and list2 still have items
        while list2:
            curr.next = ListNode(list2.val)
            list2 = list2.next
            curr = curr.next

        return result