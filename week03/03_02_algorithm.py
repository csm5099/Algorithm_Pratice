def solution(nums):
    answer=0
    answer=len(set(nums))
    if len(set(nums)) > len(nums)//2:
        answer=len(nums)//2
    return answer