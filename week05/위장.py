def solution(clothes):
    answer = 1
    dict_clothes={}
    
    # turn into dictionary
    for item,key in clothes:
        if key not in dict_clothes:
            dict_clothes[key] = 1
        else:
            dict_clothes[key] += 1
    # (2C1+1C0) * (1C1+1C0) - 1
    for i in list(j+1 for j in dict_clothes.values()):
        answer *= i
    
    return answer-1