from pandas.io.data import CUR_MONTH

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        

def partition(head, k):
    if not head:
        return head
    beforeStart, beforeEnd, afterStart, afterEnd = None, None, None, None
    cur = head
    while cur:
        if cur.val < k:
            if beforeStart is None:
                beforeStart = cur 
                beforeEnd = beforeStart
            else:
                beforeEnd.next = cur
                beforeEnd = cur 
        else:
            if afterStart is None:
                afterStart = cur 
                afterEnd = afterStart
            else:
                afterEnd.next = cur
                afterEnd = cur 
        cur = cur.next
    if not beforeStart:
        return afterStart
    beforeEnd.next = afterStart
    return beforeStart
                    
def main():
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    k = 2
    res = partition(head, k)
    print(res.val)

if __name__ == '__main__':
    main()
    
