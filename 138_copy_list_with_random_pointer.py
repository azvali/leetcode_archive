def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    
    hashmap = {None: None}
    curr = head

    while curr:
        copy = Node(curr.val)
        hashmap[curr] = copy
        curr = curr.next
    
    curr = head
    while curr:
        copy = hashmap[curr]
        copy.next = hashmap[curr.next]
        copy.random  = hashmap[curr.random]
        curr = curr.next

    return hashmap[head]