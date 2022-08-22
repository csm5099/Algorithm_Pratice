def solution(arr, divisor):
    #if the element is a factor, append it
    answer = sorted([i for i in arr if i % divisor == 0])
    #if the list is empty append -1
    if answer == []:
        answer.append(-1)
    return answer