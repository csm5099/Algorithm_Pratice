def solution(board, moves):
    answer = 0
    result=[]
    new_board=list(map(list, zip(*board)))
    
    for i in range(len(new_board)):
        new_board[i].reverse()
        new_board[i] = [j for j in new_board[i] if j != 0]
    
    for i in moves:
        if new_board[i-1] == []:
            continue
        temp=new_board[i-1]
        result.append(new_board[i-1].pop())
        if result[len(result)-2] ==result[len(result)-1] and len(result)>=2:
            result.pop()
            result.pop()
            answer+=2
    return answer