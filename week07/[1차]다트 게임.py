def solution(dartResult):
    answer = 0
    #cause of "*" calculate
    scoreBoard=[0]
    temp="" # include '10'
    index=0
    
    #scanning string
    for element in dartResult:
        #searching number
        if element.isdigit():
            temp+=element
            continue
        #if the element is a character do the calculate
        elif element.isalpha():
            index+=1
            #change type str to int
            scoreBoard.append(int(temp))
            temp=""
            if element ==  'D':
                scoreBoard[index] = scoreBoard[index]**2
            elif element ==  'T':
                scoreBoard[index] = scoreBoard[index]**3
        else:
            if element =='*':
                scoreBoard[index-1]*=2
                scoreBoard[index]*=2
            elif element =='#':
                scoreBoard[index]*=-1
        
        answer = sum(scoreBoard)
        
    return answer