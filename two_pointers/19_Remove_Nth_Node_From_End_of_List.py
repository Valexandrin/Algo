from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:            
            return head.next

        while fast.next:
            fast, slow = fast.next, slow.next            
        
        slow.next = slow.next.next
        return head

    def show_result(self, head):
        if not head:
            print(head)
            return
        while head.next:
            print(head.val)
            head = head.next
        print(head.val)

    def create_listNode(self, head: List[int]) -> Optional[ListNode]:
        L = curr = ListNode(head[0])
        for node in head[1:]:
            curr.next = ListNode(node)
            curr = curr.next
        return L
    
    def testing(self, head: List[int], n: int):
        L = self.create_listNode(head)
        proc = self.removeNthFromEnd(L, n)
        self.show_result(proc)
        return proc


s = Solution()

s.testing([1,2,3,4,5], 2)
s.testing([1], 1)
s.testing([1,2], 1)
