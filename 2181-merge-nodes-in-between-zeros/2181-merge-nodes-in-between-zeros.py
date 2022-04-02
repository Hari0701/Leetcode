# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res, cur = head, head.next
        while cur.next:
            if cur.val:
                res.val += cur.val 
            else:
                res.next = res = cur
            cur = cur.next
        res.next = None
        return head