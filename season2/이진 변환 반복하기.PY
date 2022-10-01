def solution(s):
    answer = [0,0]
    # repeat till the given string equals to '1'
    while s != '1':
        length_before = len(s)
        s = s.replace('0','')
        length_after = len(s)
        # count repeats
        answer[0] += 1
        # count removed number of zeros
        answer[1] += (length_before - length_after)
        # converse DEC to BIN
        s = format(length_after, 'b')
    return answer