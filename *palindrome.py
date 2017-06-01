# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse, fast = None, head
        # Reverse the first half part of the list.
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next
        
        
        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        tail = head.next if fast else head
        
        
         # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        
        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse = reverse.next  ######no need to do the restore
            tail = tail.next
        return is_palindrome
    
@@@@@@@second,use stacks

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stk = []
        fast = head
        slow = head
        
        while fast and fast.next:
            stk.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        
        ####when the length is odd
        if fast:
            slow = slow.next
            
        while slow:
            val = stk.pop()
            if slow.val != val:
                return False
            slow = slow.next
        return True
