class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()

        while maxheap or q:
            time += 1

            if not maxheap:
                time = q[0][1]
            else:
                c = 1 + heapq.heappop(maxheap)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
            
        return time