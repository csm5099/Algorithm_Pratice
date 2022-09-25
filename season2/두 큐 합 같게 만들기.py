from collections import deque

def solution(queue1, queue2):
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    for cnt in range(len(q1)*3):
        if sum1 == sum2:
            return cnt
        if sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
    return -1