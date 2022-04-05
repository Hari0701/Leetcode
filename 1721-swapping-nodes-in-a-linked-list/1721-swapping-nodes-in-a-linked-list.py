# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter=res=cur= head
        end = start = 0
        count = 1
        while counter.next != None:
            count += 1
            counter = counter.next
            
        while start < k -1:
            res = res.next
            start += 1
            
        idx = count - k  + 1
        while end < idx -1:
            cur = cur.next
            end += 1
            
        res.val, cur.val = cur.val, res.val
        return head
        
            
            