# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        head1 = head2 = ListNode(0)
        head1.next = head
        head2.next = head
        count = 0
        
        while head1:
            count += 1
            head1 = head1.next
            
        if count%2 == 0:
            mid = count//2
        else:
            mid = count//2 + 1
        
        for i in range(mid):
            head2 = head2.next
        
        return head2