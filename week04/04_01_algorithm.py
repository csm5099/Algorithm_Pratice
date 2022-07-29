def solution(d, budget):
    answer=0
    d.sort(reverse=True)
    while budget > 0 and d != []:
        budget-=d.pop()
        if budget <0:
            break
        answer+=1 
    return answer