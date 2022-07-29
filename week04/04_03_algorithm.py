def solution(left, right):
    answer = 0
    sqr=list(i**2 for i in range(1,32))
    nums=list(range(left,right+1))
    for i in nums:
        if i in sqr:
            answer-=i
        else:
            answer+=i
    return answer