from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

    def get_list(self):
        l = [self.val]
        node = self.next
        while node:
            l.append(node.val)
            node = node.next
        return l

class Solution:
    remainder = 0

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 and not l2:
            if self.remainder > 0:
                return ListNode(val=self.remainder)
            return None
        elif l1 and l2:
            val = l1.val + l2.val + self.remainder
            self.remainder = val // 10
            return ListNode(val=val % 10, next=self.addTwoNumbers(l1.next, l2.next))
        elif not l1:
            val = l2.val + self.remainder
            self.remainder = val // 10
            return ListNode(val=val % 10, next=self.addTwoNumbers(None, l2.next))
        elif not l2:
            val = l1.val + self.remainder
            self.remainder = val // 10
            return ListNode(val=val % 10, next=self.addTwoNumbers(None, l1.next))
