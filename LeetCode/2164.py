class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [nums[i] for i in range(0,len(nums),2)]
        odd = [nums[i] for i in range(1,len(nums),2)]
        even.sort()
        odd.sort(reverse=True)
        temp = []
        temp = []
        for i in range(len(nums)):
            if i%2==0:
                temp.append(even[i//2])
            else:
                temp.append(odd[i//2])
        return temp