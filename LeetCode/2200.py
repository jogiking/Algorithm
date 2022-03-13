class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_index = [i for i in range(len(nums)) if nums[i]==key]
        answer = []
        for i in range(len(nums)):
            for j in key_index:
                if abs(i-j) <= k:
                    answer.append(i)
                    break
        return answer