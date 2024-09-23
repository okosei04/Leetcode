# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        slow = head
        prev1 = None

        for _ in range(left - 1):
            prev1 = slow
            slow = slow.next
        
        prev = None
        curr = slow 

        for _ in range(left, right + 1):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        if prev1:
            prev1.next = prev
        
        else:
            head = prev
        

        slow.next = curr

        return head