def solution(new_id):
    #step1. make string lower case
    new_id=new_id.lower()
    #step2. remove not allowed characters 
    new_id=list(new_id)
    copied_new_id=[]
    for i in new_id:
        while (i.isalpha() or i.isdigit() or i=='-' or i=='_' or i=='.'):
            copied_new_id.append(i)
            break
    new_id=copied_new_id
    #step3. '.' deduplication
    new_id = "".join(new_id)
    while ".." in new_id:
        new_id = new_id.replace('..','.')
    new_id=list(new_id)
    #step4. remvove first '.'
    if new_id[0]=='.':
        new_id.remove('.')
    #step5. if the string is empty, append 'a'
    if len(new_id)==0:
        new_id.append('a')
    #step6. if length of string is greater than or equal to 16, save 15 characters from left. however if the end of ID is '.', remove it.
    if len(new_id)>=16:
        new_id=new_id[:15]
    if new_id[-1]=='.':
        new_id.pop()
    #step7. if the length of string is less than or equal to 2, duplicate last character until the length is 3.
    while len(new_id)<=2:
        new_id.append(new_id[-1])
    
    answer=''.join(new_id)
    return answer