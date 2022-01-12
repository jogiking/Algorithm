# lower bound, upper bound 문제였다.
# Time: O(2*logN) = O(logN), Space: O(1)

class Solution:
    def bs_left(self, nums, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid        
        return left if nums[left] == target else -1
    
    def bs_right(self, nums, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left-1 if nums[left-1] == target else -1
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        size = len(nums)
        # 왼쪽 경계선 찾기
        start = self.bs_left(nums, 0, size - 1, target)
        # 오른쪽 경계선 찾기
        end = self.bs_right(nums, 0, size, target)
        return [start, end]