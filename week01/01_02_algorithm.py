def solution(lottos, win_nums):
    
    #count zeros for high score
    zero_count=lottos.count(0)
    
    #chage data type for deduplication
    lottos_set=set(lottos)
    win_nums_set=set(win_nums)
    
    #remove zero because zero has been used before
    lottos_set.discard(0)
    
    #checking numbers of the lowest rank & highest rank
    instersection = lottos_set & win_nums_set
    matches_list=[]
    matches_list.append(len(instersection))
    matches_list.append(matches_list[0]+zero_count)
    
    answer = []
    
    for match in matches_list:
        rank = 1
        for i in range(6,-1,-1):
            if match == i:
                answer.insert(0,rank)
                break
            if i==1:
                continue
            rank+=1
    
    return answer