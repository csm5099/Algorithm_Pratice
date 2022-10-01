def solution(n, left, right):
    answer = []
    # make the list with given two numbers
    answer = list(range(left,right+1))
    # calculate quotient and remainder from each elements and exchange into requested numbers
    for v in range(len(answer)):
        i = answer[v]//n
        j = answer[v]%n
        answer[v] = i + 1 if i > j else j + 1
    return answer