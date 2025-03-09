def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    

    dummy = ListNode(0, head)
    first , second = dummy , dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next
