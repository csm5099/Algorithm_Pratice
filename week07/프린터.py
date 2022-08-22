def solution(priorities, location):
    answer = 0
    
    def enqueue(arr):
        arr.append(arr[0])
    
    def dequeue(arr):
        tmp = arr[0]
        del arr[0]
        return tmp
    
    def peek(arr):
        return arr[0]
    
    while True:
        #skip low priorities
        for i in range(priorities.index(max(priorities))):
            enqueue(priorities)
            dequeue(priorities)
            
            #calculate location
            location-=1
            if location < 0:
                location = len(priorities)-1
                            
        # count up
        if peek(priorities) == priorities[location] and location == 0:
            answer+=1
            return answer
        del priorities[0]
        location-=1
        answer+=1
                        
    return answer