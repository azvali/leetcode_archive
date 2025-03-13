def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow , fast = head , head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    curr = slow.next
    slow.next = None
    prev = None
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp


    first , second = head , prev
    while second:
        tmp1 , tmp2 = first.next , second.next
        first.next = second
        second.next = tmp1
        first , second = tmp1 , tmp2

            

