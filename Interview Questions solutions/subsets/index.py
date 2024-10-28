class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [[],nums]

        nums.sort()
        ans = [[]]

        for i in nums:
            combinations = []
            for combination in ans:
                combinations.append(combination+[i])
                combinations.append(combination)
            ans = combinations 
        return ans
