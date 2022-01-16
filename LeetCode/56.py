# Time: O(N^2*logN), Space: O(N), N은 intervals의 길이

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def addInterval(group, case):
            if not group or group[-1][1] < case[0]:
                group.append(case)
            else:
                group[-1][1] = max(group[-1][1], case[1])
                
        ans = []
        intervals.sort(key = lambda x: (x[0], x[1]))
        for element in intervals:
            addInterval(ans, element)
        return ans