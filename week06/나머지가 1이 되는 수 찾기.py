def solution(n):
    answer=2
    while (n - 1) % answer != 0:
        answer+=1
    return answer