def solution(arr):
    
    while len(arr) != 1:
        
        a = arr[0]
        b = arr[1]
        a,b = (a,b) if a>b else (b,a)

        mod=0
        while a % b != 0:
            mod = a % b
            a = mod
            a,b = (a,b) if a>b else (b,a)
        GCD=b
        LCM = arr[0] * arr[1] / GCD
        
        arr.append(LCM)
        arr=arr[2:]
        
    return int(arr[0])