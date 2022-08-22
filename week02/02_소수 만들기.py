from itertools import combinations
import math

def is_prime(num):
    sqrt = math.sqrt(num)

    if sqrt < 2:
        return False

    for i in range(2, int(sqrt+1)):
        if num % i == 0:
            return False
    return  True

def solution(nums):
    answer = 0
    total=0
    
    arr = list(combinations(nums, 3))
    for n1, n2, n3 in arr:
        total=n1+n2+n3
        if is_prime(total):
            answer += 1
            
    return answer