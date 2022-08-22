def solution(numbers):
    answer = []
    #select two numbers from list
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            #skip duplicated turn
            if i >= j:
                continue
            #sum selected numbers
            answer.append(numbers[i]+numbers[j])
    #deduplicate
    answer=set(answer)
    answer=list(answer)
    answer.sort()
    return answer