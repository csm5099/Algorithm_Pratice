def solution(id_list, report, k):    
    report=set(report)
    reprt=list(report)
    
    reported_dict={}
    report_db={}
    report_result={}
    
    for i in id_list:
        reported_dict[i]=0
        report_db[i]=[]
        report_result[i]=0
        
    for i in report:
        temp_reporter=i.split(' ')[0]
        temp_reported=i.split(' ')[1]
        if temp_reporter in id_list:
            reported_dict[temp_reported]+=1
            report_db[temp_reporter].append(temp_reported)
    ban_list=[]
    for key, value in reported_dict.items():
        if value >=k:
            ban_list.append(key)
            
    for key, value in report_db.items():
        for i in value:
            for j in ban_list:
                if i==j:
                    report_result[key]+=1
    answer=report_result.values()
    answer = list(answer)
    return answer