# Counter 길이가 1일 때 어떻게 처리할지 생각하는데 오래걸렸다.

from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        size = len(nums)
        odd = Counter([nums[i] for i in range(1,size,2)])
        odd[-1] = 0
        even = Counter([nums[i] for i in range(0,size,2)])
        even[-1] = 0
        
        even_common = even.most_common()
        odd_common = odd.most_common()
        if odd_common[0][0] != even_common[0][0]:
            answer = size - even_common[0][1] - odd_common[0][1]
        else:
            answer = size - max(even_common[1][1]+odd_common[0][1], even_common[0][1]+odd_common[1][1])
            
        return answer
            
