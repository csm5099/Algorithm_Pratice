def solution(name):
    answer = 0
    # minimum control count
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# calcurate minimum control count
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # searching 'A'
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        print(next)
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        print(f"{i} {min_move} {2*i+len(name) - next} {i+2*(len(name) -next)}")
        min_move = min([min_move, 2*i+len(name) - next, i+2*(len(name) -next)])
        
    answer += min_move
    return answer