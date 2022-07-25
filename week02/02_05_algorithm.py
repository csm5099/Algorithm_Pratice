def solution(n, lost, reserve):
    answer = 0
    lost_list=[False]*n
    reserve_list=[False]*n
    
    for index in lost:
        lost_list[index-1]=True
            
    for index in reserve:
        reserve_list[index-1]=True
            
    for i, reserve in enumerate(reserve_list):
        if reserve == True:
            if i-1 >=0:
                if lost_list[i-1]==True:
                    lost_list[i-1]=False
                    continue
            if i+1 <n:
                if lost_list[i+1]==True:
                    lost_list[i+1]=False
                    continue
    answer = lost_list.count(False)
    return answer