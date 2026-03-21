today i have solved leetcode problem #1752. Check if Array Is Sorted and Rotated
I would say it was a easy problem
I solved it without facing a problem
#here is my code
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
    
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
    
        return count <= 1
