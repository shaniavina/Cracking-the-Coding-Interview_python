
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        

def kthToLast(head, k):
    if not head:
        return head
        
    slow = head
    fast = head
    for i in range(k):
        if fast:
            fast = fast.next
        else:
            return None
    while fast:
        slow = slow.next
        fast = fast.next
    return slow
                    
def main():
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    k = 3
    res = kthToLast(head, k)
    print(res.val)

if __name__ == '__main__':
    main()
    
