def solution(array, commands):
    answer = []
    
    for command in commands:
        array_copied=array
        array_sliced=[]
        print(command)
        i=command[0]
        j=command[1]
        k=command[2]
        array_sliced=array_copied[i-1:j]
        array_sliced.sort()
        print(array_sliced)
        answer.append(array_sliced[k-1])
    return answer