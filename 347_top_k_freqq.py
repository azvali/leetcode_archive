class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        maxheap = []
        res = []

        for x in range(len(nums)):
            hashmap[nums[x]] = hashmap.get(nums[x], 0) + 1

        for key , v in hashmap.items():
            heapq.heappush(maxheap, [-v,key])

        for _ in range(k):
            res.append(heapq.heappop(maxheap)[1])
        
        return res
        
