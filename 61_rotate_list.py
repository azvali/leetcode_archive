def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

    curr = head
    n = 1
    while curr and curr.next:
        curr = curr.next
        n += 1

    k = k % n
    if not head or not head.next or k == 0:
        return head

    p1 = head
    for i in range(n - k - 1):
        p1 = p1.next

    newhead = p1.next
    p1.next = None
    curr.next = head

    return newhead