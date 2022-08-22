def solution(a, b):
    day=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    days=[31,29,31,30,31,30,31,31,30,31,30,31]
    sum_days = sum(days[0:a-1]) + b
    return day[sum_days%7]