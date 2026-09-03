class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for _ in range(len(nums)+1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num, freq in count.items():
            bucket[freq].append(num)

        result = []
        
        for freq in range(len(bucket) -1, 0, -1):
            for num in bucket[freq]:
                result.append(num)

                if len(result) == k:
                    return result


