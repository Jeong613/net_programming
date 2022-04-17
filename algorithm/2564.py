# 경비원

import sys
input = sys.stdin.readline


w, h = map(int, input().split())  # 직사각형 블록 입력받기
store_num = int(input())  # 상점 개수
dist = []
ans = 0


def dist_func(loc, dis):
    if loc == 1:  # 북
        return dis
    
    elif loc == 2:  # 남
        return w + h + w - dis

    elif loc == 3:  # 서
        return w + h + w - dis
    
    elif loc == 4:  # 동
        return w + h + w - dis

for i in range(store_num+1):
    loc, dis = map(int, input().split())
    dist.append(dist_func(loc, dis))