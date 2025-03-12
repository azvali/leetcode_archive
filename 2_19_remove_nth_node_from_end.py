def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    
    
    dummy = ListNode(0)
    dummy.next = head
    l , r = dummy, dummy

    
    for _ in range(n + 1):
        if r:
            r = r.next
        
    while r :
        l = l.next
        r = r.next
    
    if l.next:
        l.next = l.next.next
    
    
    return dummy.next
    
    
        
        