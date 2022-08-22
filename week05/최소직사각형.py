def solution(sizes):
    #sort each inputs
    for i in range(len(sizes)):
        (sizes[i][0], sizes[i][1]) = (sizes[i][0], sizes[i][1])if sizes[i][0] < sizes[i][1] else (sizes[i][1], sizes[i][0])
    #select height and width that the biggest number from list
    return max(list(i[0] for i in sizes)) * max(list(i[1] for i in sizes))