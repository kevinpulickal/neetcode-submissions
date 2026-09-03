class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numset:
                current = num
                length = 1

                while current + 1 in numset:
                    length += 1
                    current += 1

                longest = max(longest, length)
        return longest

