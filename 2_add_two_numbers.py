def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            
    dummy = ListNode()
    cur = dummy
    carry  = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        curtotal = val1 + val2 + carry
        carry = curtotal // 10
        curtotal = curtotal % 10
        cur.next = ListNode(curtotal)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    
    return dummy.next