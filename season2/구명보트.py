from collections import deque

def solution(people, limit):
    
    answer = 0
    # converse list to deque
    people = deque(sorted(people))
    
    
    while people:
        # if there is only one element, then break
        if len(people) == 1:
            answer += 1
            break
        # if the sum of elements at both ends of the deque is less than the limit, pop them.
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        # if not, pop the last element 
        else:
            people.pop()
        answer += 1
    return answer