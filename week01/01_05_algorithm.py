def solution(numbers, hand):
    answer = ''
    pad_row=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    pad_col=[[1,4,7,'*'],[3,6,9,'#'],[2,5,8,0]]
    number_location=[]
    left_hand=0
    right_hand=0
    left_xy=[]
    right_xy=[] 
    input_xy=[]
    
    for input_num in numbers:
        for col_index,j in enumerate(pad_col):
            if input_num in j:
                if col_index == 0:
                    left_hand=input_num
                    answer+='L'
                if col_index == 1:
                    right_hand=input_num
                    answer+='R'
                if col_index == 2:
                    for ii,row in enumerate(pad_row):
                        for jj,number in enumerate(row):
                            if input_num==number or str(right_hand)==number:
                                input_xy=[ii,jj]
                                break
                    for ii,row in enumerate(pad_row):
                        for jj,number in enumerate(row):
                            if left_hand==number or str(right_hand)==number:
                                left_xy=[ii,jj]
                                break
                    for ii,row in enumerate(pad_row):
                        for jj,number in enumerate(row):
                            if right_hand==number or str(right_hand)==number:
                                right_xy=[ii,jj]
                                break
                    a=abs(left_xy[0]-input_xy[0])+abs(left_xy[1]-input_xy[1])
                    b=abs(right_xy[0]-input_xy[0])+abs(right_xy[1]-input_xy[1])
                    if a == b:
                        if hand=='left':
                            left_hand=input_num
                            answer+='L'
                        else:
                            right_hand=input_num
                            answer+='R'
                    elif a < b:
                        left_hand=input_num
                        answer+='L'
                    else:
                        right_hand=input_num
                        answer+='R'
    return answer