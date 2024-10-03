class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        nums.sort() 

        while(left < right):
            if nums[left] != left:
                return left
            left += 1
        return left
