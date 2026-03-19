# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Approach: Hash Map
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[num] = i
