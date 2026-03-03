# Last updated: 3/3/2026, 11:24:15 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        dummyNode = ListNode()
9        curr = dummyNode
10
11        carry = 0
12
13        while l1 or l2 or carry:
14            sum = carry
15            if l1:
16                sum+=l1.val
17                l1 = l1.next
18            if l2:
19                sum+=l2.val
20                l2 = l2.next
21
22            new_node = ListNode(sum%10)
23            curr.next = new_node
24            curr = curr.next
25
26            carry = sum // 10
27
28        return dummyNode.next
29            
30
31