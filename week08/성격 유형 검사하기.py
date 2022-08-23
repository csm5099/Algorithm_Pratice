def solution(survey, choices):
    answer = ''
    #score board
    ptype={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0,}
    #score calculate
    for t,s in zip(survey,choices):
        if s ==4:
            pass
        elif s<4:
            ptype[t[0]]+=(-s%4)
        elif s>4:
            ptype[t[1]]+=s%4
    # comparing
    answer += 'R' if ptype['R'] >= ptype['T'] else 'T'
    answer += 'C' if ptype['C'] >= ptype['F'] else 'F'
    answer += 'J' if ptype['J'] >= ptype['M'] else 'M'
    answer += 'A' if ptype['A'] >= ptype['N'] else 'N'
    return answer