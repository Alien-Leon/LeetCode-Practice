# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow = head
        fast = head
        cycle = False
        # 检查链表中是否有环可以采用快慢双指针的形式，若两个指针能够相遇，说明有环
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        """
        当发现链表有环时，两指针会停在环中某一点，设这一点为B点，入环第一点为A点。
        假设A到头结点距离为a，A到B距离为b，那么B点到头结点距离为（a+b）
        由于快指针走的路程为慢指针两倍，那么快指针到达B点时，实际上走了2（a+b）
        如图
        
            1->2->3->4->5
                  ↑     ↓
                  8<-7<-6
            相遇点在点7， 7->3 = 距离a = 1->3, 3->7=距离b
        """
          
        if cycle:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None




