class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.miniheap = nums
        self.k = k
        heapq.heapify(self.miniheap)
        while len(self.miniheap) > k:
            heapq.heappop(self.miniheap)



    def add(self, val: int) -> int:
        heapq.heappush(self.miniheap, val)
        if len(self.miniheap) > self.k:
            heapq.heappop(self.miniheap)
        return self.miniheap[0]


