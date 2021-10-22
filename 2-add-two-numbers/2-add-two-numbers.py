# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        added = ListNode(val = (l1.val + l2.val) % 10)
        carryover = (l1.val + l2.val) // 10
        currentnode = added 
        
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            currentnode.next = ListNode(val = (carryover + l1.val + l2.val) % 10)
            carryover = (carryover + l1.val + l2.val) // 10
            currentnode = currentnode.next
            
        while l1.next:
            l1 = l1.next
            currentnode.next = ListNode(val = (carryover + l1.val) % 10)
            carryover = (carryover + l1.val) // 10
            currentnode = currentnode.next
        
        while l2.next:
            l2 = l2.next
            currentnode.next = ListNode(val = (carryover + l2.val) % 10)
            carryover = (carryover + l2.val) // 10
            currentnode = currentnode.next
            
        
        if carryover > 0:
            currentnode.next = ListNode(val = (1))
            
        return(added)