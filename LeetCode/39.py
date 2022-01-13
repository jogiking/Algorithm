# 후보자배열(candidates)에서 하나씩 뽑고 남김없이 채워졌다면(remains) 해당 경우(current)에 추가한다.
# 후보자배열에서 순서대로 볼 때, 한번 봤던 인덱스는 보지 않아야 중복없이 구할 수 있다.(14라인의 candidates[i:])
# Time: O(N^target) N은 candidates의 길이, Space: target

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(candidates, current, remains):
            if remains == 0:
                ans.append(current)
                return
            if remains < 0:
                return
            for i in range(len(candidates)):
                dfs(candidates[i:], current+[candidates[i]], remains-candidates[i])
                
        dfs(candidates, [], target)
        
        return ans