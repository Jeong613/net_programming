# 정사각형 1051
import sys
input= sys.stdin.readline
n,m= list(map(int,input().split()))  # n : 세로 m : 가로
rect = []
ans = 1
for x in range(n) :  # 직사각형에 들어갈 숫자 받아오기
    rect.append(list(input().strip()))

# 제일 큰 정사각형 크기    
max_rect = min(n, m) - 1  # 인덱스라 - 1

for x in range(n) :
    for y in range(m) :
        for index in range(max_rect, 0, -1) :
            if n <= x + index or m <= y + index :
                break
            #정사각형 꼭지점 비교
            if rect[x][y] == rect[x + index][y] == rect[x][y + index] == rect[x + index][y + index] :
                ans = (index+1) * (index+1)
print(ans)