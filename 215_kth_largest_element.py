def findKthLargest(self, nums: List[int], k: int) -> int:
    maxheap = [-x for x in nums]
    heapq.heapify(maxheap)

    while maxheap and k > 0:
        curr = heapq.heappop(maxheap)
        k -= 1

    return -1 * curr 