class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start,end = s.split(":")
        word=list("abcdefghijklmnopqrstuvwxyz".upper())
        answer=[]
        for i in range(word.index(start[0]), word.index(end[0])+1):
            for j in range(int(start[1]),int(end[1])+1):
                answer.append(word[i]+str(j))
        return answer