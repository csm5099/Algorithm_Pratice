def solution(N, stages):
    answer = []
    #create a list filled with zeroes by a given length
    failed = list(0 for x in range(1,N+1))
    
    #calculate fail rate
    clear=len(stages)
    for i in range(1,N+1):
        if i in stages:
            failed[i-1] = stages.count(i) / clear
            clear -= stages.count(i)
        else:
            continue
            
    #rank the level
    for i in range(N):
        i = failed.index(max(failed))
        answer.append(i+1)
        failed[i] = -1
    
    return answer