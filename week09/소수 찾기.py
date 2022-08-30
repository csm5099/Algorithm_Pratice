def solution(n):
    n+=1
    numbers=[True]*n
    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i] == True:
            for j in range(i+i,n,i):
                numbers[j]=False
    return len([x for x in range(2,n) if numbers[x] == True])