def solution(n):
    answer = 0
    tri=[]
    while n != 0:
        tri.insert(0,n % 3)
        n = n // 3
    for i,num in enumerate(tri):
        answer+=num*(3**i)
    return answer