def solution(s):
    answer = 1000
    
    # calculate length of string and make list
    divisors=[x for x in range(1,len(s)+1)]
    
    for divisor in divisors:
        tmp_ls=[]
        s_copied=s[:]
        compressed=""
        
        #slice the string with given number
        tmp_ls = [s[i:i+divisor] for i in range(0, len(s), divisor)]
            
        #compress string
        cnt=1
        for j in range(len(tmp_ls)):            
            
            #last character exception
            if j+1 == len(tmp_ls):
                compressed+=str(cnt) if cnt > 1 else ''
                compressed+=tmp_ls[j]
                break

            #count same character
            if tmp_ls[j] == tmp_ls[j+1]:
                cnt+=1
                continue
                
            #compressing step
            if tmp_ls[j] != tmp_ls[j+1]:
                compressed+=str(cnt) if cnt > 1 else ''
                compressed+=tmp_ls[j]
                cnt=1
                continue
        
        # leastest string
        answer = len(compressed) if len(compressed) < answer else answer
        
    return answer