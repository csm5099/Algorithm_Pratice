def solution(arr):
    answer = []
    index=-1
    
    for i in arr:
        #append number
        answer.append(i)
        index+=1
        #prevent out of range
        if index==0:
            continue
        #compare previous and present
        if answer[index-1] == answer[index]:
            answer.pop()
            index-=1
    return answer