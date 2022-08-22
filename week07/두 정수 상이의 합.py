def solution(a, b): return sum([i for i in range(a,b+1)]) or sum([i for i in range(b,a+1)])
'''
for i in range(a:b+1):
    |   |   |   |
    v   v   v   v
sum([i for i in range(a,b+1)])
'''
