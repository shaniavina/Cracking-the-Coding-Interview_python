
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
####runner, no buffer but O(N^2) time
def deleteDuplicates1(head):
    if not head:
        return head
        
    cur = head
    while cur:
        runner = cur
        while runner.next:
            if cur.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next
    return head

#####iterate, use hash table
def deleteDuplicates2(head):
    if not head:
        return head
    cur = head
    check = {}
    while cur and cur.next:
        if cur.next.val not in check:
            check[cur.next.val] = 1
        else:
            cur.next = cur.next.next
    return head
                    
def main():
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    res = deleteDuplicates2(head)
    print(res.val)

if __name__ == '__main__':
    main()
    
