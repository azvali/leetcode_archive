def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)

        if first < second:
            new = abs(second) - abs(first)
            heapq.heappush(stones, new)
        elif second > first:
            new = abs(first) - abs(second)
            heapq.heappush(stones, new)
        else:
            continue

    return abs(stones[0]) if stones else 0