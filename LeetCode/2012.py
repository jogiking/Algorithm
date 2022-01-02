class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        ans = 0
        length = len(nums)
        
        minArr = [0]*len(nums)
        minArr[-1] = nums[-1]
        
        for i in reversed(range(length-1)):
            minArr[i] = min(nums[i], minArr[i+1])
        
        maxValue = nums[0]
        for i in range(1, length-1):
            if maxValue < nums[i] < minArr[i+1]:
                ans += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                ans += 1
            maxValue = max(nums[i], maxValue)
            
        return ans
     
