# 쇠막대기

import sys
input = sys.stdin.readline

str = input().rstrip()  # 끊어주기 오른쪽으로 하나씩
stack = []
cnt = 0  # ans

for i in range(len(str)):  # 문자열 길이만큼 포문 돌리기
    if str[i] == '(':
        stack.append('(')

    else:  #')'일 때
        if str[i-1] == '(':  # 레이저일 경우
            stack.pop()
            cnt += len(stack)
        
        else:  # 쇠막대기일 경우
            cnt += 1  # 끝에 꺼 하나 추가
            stack.pop()

print(cnt)