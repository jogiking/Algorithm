class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def combi(stack, path):
            answer.append(stack)
            for i in range(path,len(nums)):
                combi(stack+[nums[i]],i+1)
                
        combi([],0)
        return answer
