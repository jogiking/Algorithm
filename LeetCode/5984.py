# 2개의 부분집합으로 분리해서 풀려고 했지만 잘 되지 않았음.
#
# 가장 큰 숫자 순서대로 하나씩 뽑고 순서대로 2개의 부분집합의 밑수로 만들면서 최소값을 구하는 방법(그리디)으로 해결함.
# 예를들어 [9,3,2,1]이 주어져있다면, 가장 큰 9, 3을 각각 뽑아서 2개의 부분집합의 끝수로 만들면 (x9, x3)이 된다. 가장 큰 숫자를 맨뒤로 보냈으므로,
# 부분집합의 가장 앞자리 수는 전체 집합에서 가장 작은 수가 되므로 이 경우 각 부분집합의 합은 최소값이 된다.

class Solution:
    def minimumSum(self, num: int) -> int:
        arr=list(map(int,str(num)))
        arr.sort(reverse=True)
        answer=0
        position=0
        for i in range(len(arr)):
            answer+=arr[i]*10**position
            if i%2==1 :
                position+=1
        return answer
