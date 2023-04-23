class Solution:
    def getKthFromEnd(self,head:ListNode,k:'int')-> ListNode:
        former,latter=head,head
        for _ in range(k):
            if not former: return
            former=former.next
        while former:
            former,latter=former.next,latter.next
        return latter