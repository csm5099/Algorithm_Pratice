

def solution(name):
    answer = 0
    result_left=0
    result_right=0
    alpha=['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M']
    
    for i in range(0,len(name)):
        if i == len(name)-1 and name[i] == 'A':
            continue
        if i != 0:
            result_right+=1
        n = abs(alpha.index(name[i]) - alpha.index('A'))
        # print(f"right {alpha.index(name[i])} {alpha.index('A')} {n}")
        result_right+=n
        
    for i in range(0,-len(name),-1):
        if i == -len(name)+1 and name[i] == 'A':
            continue
        if i != 0:
            result_left+=1
        n = abs(alpha.index(name[i]) - alpha.index('A'))
        # print(f"left {alpha.index(name[i])} {alpha.index('A')} {n}")
        result_left+=n
        
    if result_right >= result_left:
        answer = result_left
        
    # print(f"{result_right} {result_left}")
    return answer