# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lena=0
        lenb=0
        dummyA=ListNode()
        dummyB=ListNode()
        dummyA.next=headA
        dummyB.next=headB
        while headA or headB:
            if headA:
                headA=headA.next
                lena+=1
            if headB:
                headB=headB.next
                lenb+=1
        if lena>lenb:
            z=lena-lenb+1
            while z>0:
                dummyA=dummyA.next
                z-=1
            dummyB=dummyB.next
        else:
            z=lenb-lena+1
            while z>0:
                dummyB=dummyB.next
                z-=1
            dummyA=dummyA.next
        while dummyA != dummyB:
            dummyA=dummyA.next
            dummyB=dummyB.next
        return dummyA
        
                
       

        