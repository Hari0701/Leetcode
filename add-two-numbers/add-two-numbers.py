# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        root = None
        
        while l1.next != None or l2.next != None:
            if l1.next != None:
                num1 += str(l1.val)
                l1 = l1.next
            if l2.next != None:  
                num2 += str(l2.val)
                l2 = l2.next
        num1 += str(l1.val)  
        num2 += str(l2.val)

        val = int(num1[::-1]) + int(num2[::-1])
        
        def insert(root, item):
            temp = ListNode(item)
            if (root == None):
                root = temp
            else :
                ptr = root
                while (ptr.next != None):
                    ptr = ptr.next
                ptr.next = temp                     
            return root
        
        while len(str(val)) > 1:
            ele = val %10
            val = val//10
            root = insert(root,ele)
        root = insert(root,val)
       
        return root