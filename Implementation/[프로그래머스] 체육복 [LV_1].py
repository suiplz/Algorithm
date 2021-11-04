# -*- coding: utf-8 -*-
"""프로그래머스_체육복.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13jFd52Z55HSi36NfntEdCCoQP0U79lJt
"""

def solution(n, lost, reserve):
    ls = []
    answer = n - len(lost)
    for i in lost:
        for u in reserve:
            if i == u:
                ls.append(i)

    for i in ls:
        lost.remove(i)
        reserve.remove(i)
        answer += 1

    lost.sort()
    reserve.sort(reverse = True)
    
    i = 0
    while True:
        if len(lost) == 0  or len(reserve) == 0:
            break
        if i >= len(lost):
            break
        
        for u in range(len(reserve)-1,-1,-1):
            if reserve[u] -1 <= lost[i] <= reserve[u]+1:
                answer += 1
                reserve.pop()
                break
        
        i += 1
                
    return answer