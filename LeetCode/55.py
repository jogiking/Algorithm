# Time: O(N), Space: O(1), N은 nums 배열의 길이

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_value = 0
        current_end = 0
        size = len(nums)
        for i in range(size):
            if max_value < i:
                break
                
            max_value = max(max_value, i + nums[i])
            if i == current_end:
                current_end = max_value
        
        return max_value >= size-1