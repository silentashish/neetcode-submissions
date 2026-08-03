# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force approach 
        result_list = []

        for linked_list in lists:
            curr = linked_list
            while curr:
                result_list.append(curr)
                curr = curr.next
        result_list.sort(key = lambda x : x.val)
        
        if not result_list:
            return None

        head = result_list[0]
        curr = head
        for i in range(1,len(result_list)):
            curr.next = result_list[i]
            curr = curr.next
        return head