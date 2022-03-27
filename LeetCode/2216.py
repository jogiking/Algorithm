class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if len(res) % 2 == 0 or n != res[-1]:
                res.append(n)
        
        # res는 남길것인데 짝수여야하므로 홀수면 한개를 더지운다
        return len(nums)-(len(res)-len(res)%2)
