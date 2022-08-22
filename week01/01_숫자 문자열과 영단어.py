def solution(s):
    #make list of numbers
    numbers=['zero','one','two','three','four','five','six','seven','eight','nine']
    
    #use enumerate() to use index and values
    for index, num in enumerate(numbers):
        if num in s:
            temp=str(index)
            #change word to number
            s=s.replace(num,temp)
    answer = int(s)
    return answer