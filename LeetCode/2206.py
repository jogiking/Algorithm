class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        
        for v in dict.values():
            if v%2 == 1:
                return False
        return True
