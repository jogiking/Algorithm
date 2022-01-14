# Time: O(N*MlogM), Space: O(N)
# M: strs 배열 원소의 최대 길이, N: strs의 길이

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in dict:
                dict[key].append(s)
            else:
                dict[key] = [s]
        return dict.values()