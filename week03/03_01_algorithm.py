def solution(answers):
    answer = []
    score_list=[0,0,0]
    std1 = list(range(1,6))
    std2 = [2,1,2,3,2,4,2,5]
    std3 = [3,3,1,1,2,2,4,4,5,5]
    
    while len(std1) < len(answers) or len(std2) < len(answers) or len(std3) < len(answers):
        std1+=std1
        std2+=std2
        std3+=std3

    std1=std1[:len(answers)]    
    std2=std2[:len(answers)]
    std3=std3[:len(answers)]
    
    for a,s1,s2,s3 in zip(answers,std1,std2,std3):
        if a == s1:
            score_list[0]+=1
        if a == s2:
            score_list[1]+=1
        if a == s3:
            score_list[2]+=1
            
    for i, score in enumerate(score_list):
        if score == max(score_list):
            answer.append(i+1)
    return answer