from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = end = head
        while end and end.next:            
            current = current.next
            end = end.next.next            

        return current         


class Solution2:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = [head]        
        while head.next:                       
            res.append(head.next)            
            head = head.next
        
        return res[len(res)//2]
        
        
L = ListNode(1)
L.next = ListNode(2)
L.next.next = ListNode(3)
L.next.next.next = ListNode(4)
L.next.next.next.next = ListNode(5)
L.next.next.next.next.next = ListNode(6)

s = Solution()
print(s.middleNode(L).val)

