class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
        
        result = 0
        for num in nums:
            if num - 1 not in num_set:
                cons = 0
                while num in num_set:
                    cons += 1
                    num += 1
                result = max(result, cons)
        
        return result
