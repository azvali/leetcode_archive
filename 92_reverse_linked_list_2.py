def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    


    dummy = ListNode()
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    currprev = None
    for _ in range(right - left + 1):
        tmp = curr.next
        curr.next = currprev
        currprev = curr
        curr = tmp
    
    prev.next.next = curr
    prev.next = currprev

    return dummy.next
