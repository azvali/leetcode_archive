def hasCycle(self, head: Optional[ListNode]) -> bool:
    
    hashset = set()
    cur = head

    while cur and cur.next:
        if cur not in hashset:
            hashset.add(cur)
            cur = cur.next
        else:
            return True

    return False