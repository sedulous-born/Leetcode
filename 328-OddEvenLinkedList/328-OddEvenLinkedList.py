# Last updated: 3/3/2026, 3:03:38 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        dummyNode1 = ListNode()
9        dummyNode2 = ListNode()
10        curr1 = dummyNode1
11        curr2 = dummyNode2
12
13        curr = head
14        i = 0
15
16        while curr:
17            new_node = ListNode(curr.val)
18            if(i%2==0):
19                curr1.next = new_node
20                curr1 = curr1.next
21            else:
22                curr2.next = new_node
23                curr2 = curr2.next
24
25
26            curr = curr.next
27            i+=1
28
29        curr1.next = dummyNode2.next
30        return dummyNode1.next