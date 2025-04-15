class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
                
        heap = []
        heapq.heapify(heap)
        res = []

        for i in points:
            x = i[0]
            y = i[1]

            distance = (math.sqrt((0 - x)**2 + (0 - y)**2))
            heapq.heappush(heap, [distance, x , y])

        while k > 0:
            x = heapq.heappop(heap)
            res.append([x[1],x[2]])
            k -= 1
        
        return res