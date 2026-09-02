class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
                
            chars.add(s[right])

            if right - left + 1 > longest:
                longest = right - left + 1

        return longest
        
       
                
