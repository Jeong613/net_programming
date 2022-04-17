# 쿼드트리
import sys
input= sys.stdin.readline

N = int(input())  # 배열 크기
rect = [list(map(int, input().strip())) for x in range(N)] # 배열에 들어갈 숫자 받아오기

# 체크할 함수
def check_rect(x, y, crit):
    first_obj = rect[x][y] # 검사할 칸

    for i in range(x, x + crit):
        for j in range(y, y + crit):
            if rect[i][j] != first_obj: # 다를 경우
                crit = crit // 2  # 다시 나누기
                print('(', end = "")
                check_rect(x, y, crit)
                check_rect(x, y + crit, crit)
                check_rect(x + crit, y, crit)
                check_rect(x + crit, y + crit, crit)
                print(')', end = "")

                return
    if first_obj == 0:
        print(0, end = "")
    else:
        print(1, end = "")

check_rect(0, 0, N)
