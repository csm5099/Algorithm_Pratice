def solution(numbers, hand):
    number_dict ={
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        '*':(3,0),0:(3,1),'#':(3,2)
        }
    answer=''
    left_dist=0
    right_dist=0
    #[0]left, [1]right
    thumb=['*','#']
    for input_num in numbers:
        if input_num in [1,4,7]:
            thumb[0]=input_num
            answer+='L'
        elif input_num in [3,6,9]:
            thumb[1]=input_num
            answer+='R'
        else:
            left_dist = (abs(number_dict[thumb[0]][0] - number_dict[input_num][0]) + abs(number_dict[thumb[0]][1] - number_dict[input_num][1]))
            
            right_dist = (abs(number_dict[thumb[1]][0]-number_dict[input_num][0]) + abs(number_dict[thumb[1]][1] - number_dict[input_num][1]))
            print(f"{left_dist} {right_dist}")
            if left_dist==right_dist:
                if hand=='left':
                    thumb[0]=input_num
                    answer+='L'
                else:
                    thumb[1]=input_num
                    answer+='R'
            elif left_dist < right_dist:
                thumb[0]=input_num
                answer+='L'
            else:
                thumb[1]=input_num
                answer+='R'
    return answer