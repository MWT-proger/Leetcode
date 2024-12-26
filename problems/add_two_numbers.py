from itertools import zip_longest
from typing import Optional


# Definition for singly-linked list.
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
            if val >= 10:
                val = val - 10
                self.remainder = 1
            else:
                self.remainder = 0

            return ListNode(val=val, next=self.addTwoNumbers(l1.next, l2.next))

        elif not l1:
            val = l2.val + self.remainder
            if val >= 10:
                val = val - 10
                self.remainder = 1
            else:
                self.remainder = 0

            return ListNode(val=val, next=self.addTwoNumbers(None, l2.next))

        elif not l2:
            val = l1.val + self.remainder
            if val >= 10:
                val = val - 10
                self.remainder = 1
            else:
                self.remainder = 0

            return ListNode(val=val, next=self.addTwoNumbers(None, l1.next))


node_l1_p3 = ListNode(val=3)
node_l1_p2 = ListNode(val=4, next=node_l1_p3)
node_l1_p1 = ListNode(val=7, next=node_l1_p2)


node_l2_p3 = ListNode(val=1)
node_l2_p2 = ListNode(val=5, next=node_l2_p3)
node_l2_p1 = ListNode(val=9, next=node_l2_p2)
print("Тест 0")
print(node_l1_p1.get_list())
print(node_l2_p1.get_list())
solution = Solution()
print(solution.addTwoNumbers(l1=node_l1_p1, l2=node_l2_p1).get_list())


node_l1_p3 = ListNode(val=2)
node_l1_p2 = ListNode(val=4, next=node_l1_p3)
node_l1_p1 = ListNode(val=3, next=node_l1_p2)


node_l2_p3 = ListNode(val=5)
node_l2_p2 = ListNode(val=6, next=node_l2_p3)
node_l2_p1 = ListNode(val=4, next=node_l2_p2)
print("Тест 1")
print(node_l1_p1.get_list())
print(node_l2_p1.get_list())
solution = Solution()
print(solution.addTwoNumbers(l1=node_l1_p1, l2=node_l2_p1).get_list())

node_l1_p1 = ListNode(9)

node_l1_p2 = ListNode(9, node_l1_p1)

node_l1_p3 = ListNode(9, node_l1_p2)

node_l1_p4 = ListNode(9, node_l1_p3)

node_l1_p5 = ListNode(9, node_l1_p4)

node_l1_p6 = ListNode(9, node_l1_p5)

node_l1_p7 = ListNode(9, node_l1_p6)

node_l1_p8 = ListNode(9, node_l1_p7)


node_l2_p1 = ListNode(9)

node_l2_p2 = ListNode(9, node_l2_p1)

node_l2_p3 = ListNode(9, node_l2_p2)

node_l2_p4 = ListNode(9, node_l2_p3)
print("Тест 2")

print(node_l1_p8.get_list())
print(node_l2_p4.get_list())
solution = Solution()
print(solution.addTwoNumbers(l1=node_l1_p8, l2=node_l2_p4).get_list())
