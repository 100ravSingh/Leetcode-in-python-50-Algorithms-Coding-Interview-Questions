class Solution:
    def searchRange(self, A: List[int], target: int) -> List[int]:
        left = 0
        right = len(A)
        ans = []
      
        if len(A) == 0:
            return [-1,-1]

        if target not in A:
            return [-1,-1]

        while(left < right):
            if A[left] == target:
                ans.append(left)
            left += 1
          
        if len(ans) < 2:
            ans.append(ans[0])
    
        return [ans[0],ans[-1]]
