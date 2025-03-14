def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    slow , fast = head , head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow2 = head

            while slow2 != slow:
                slow2 = slow2.next
                slow = slow.next

            return slow2

    return None



