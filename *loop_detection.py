
###collide or not, intersect or not
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:  #####fast always comes before fast.next
            fast, slow = fast.next.next, slow.next   ####one step, two step; finally meet
            if fast == slow:
                return True
        return False




#####find the start position of the loop

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
        fast, slow = head, head
        while fast and fast.next:  #####fast always comes before fast.next
            fast, slow = fast.next.next, slow.next   
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
