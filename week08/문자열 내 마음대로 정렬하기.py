def solution(strings, n):
    answer=[]
    #find n(th) string and insert 1st
    for index,value in enumerate(strings):
        strings[index]=value[n]+strings[index]
    #sort the list and remove 1st charater
    for i in sorted(strings):
        answer.append(i[1:])
    return answer