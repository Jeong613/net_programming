# 보석상자
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # n : 아이들 수, m : 보석 종류

coj = []  # 보석 종류별 개수 담을 곳
for x in range(M):
    coj.append(int(input()))

low = 1  # 나눠줄 수 있는 제일 작은 수 
high = max(coj)

while low <= high:
    mid = (low + high) // 2
    total = 0  # 인당 가져갈 수 있는 보석 수
    for color in coj:
        if color % mid == 0:
            total += color//mid
        else:
            total += (color//mid) + 1 
    #total 수집 후
    # 한 명이 가져가는 보석의 수를 늘림
    if total > N:  # N명보다 더 많은 사람이 보석을 가져간 거기 때문에 나눠주는 보석 수를 늘려야함
        low = mid + 1

    else:
        high = mid - 1

print(low)