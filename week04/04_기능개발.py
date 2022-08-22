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
        
        #choose minimum of sum, left searching and right searching 
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
        
    answer += min_move
    return answer