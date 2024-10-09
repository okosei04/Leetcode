# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
            
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        k = k % length

        if k == 0:
            return head
        
        fast = head
        for _ in range(k):
            fast = fast.next
        
        slow = head

        while fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        fast.next = head

        return temp
