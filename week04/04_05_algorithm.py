def solution(progresses, speeds):
    
    answer = []
    
    while progresses != []:
        
        #daily progress
        for i, s in enumerate(zip(progresses, speeds)):
            progresses[i] = sum(s)

        #release
        release = 0
        while progresses[0] >= 100:
            del progresses[0]
            del speeds[0]
            release += 1
            if progresses == [] and speeds ==[]:
                break
        
        # append released projects count
        if release > 0:
            answer.append(release)
            
    return answer