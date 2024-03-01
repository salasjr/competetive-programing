# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        lenn, curr = 0, head
        while curr:
            lenn+=1
            curr=curr.next
        part, rem = lenn//k, lenn%k
        res=[]
        curr=head
        for i in range(k):
            res.append(curr)
            for j in range(part-1+ (1 if rem else 0)):
                if not curr:
                    break
                curr=curr.next
            rem-= (1 if rem else 0)
            if curr:
                curr.next,curr=None,curr.next
        return res





        


        