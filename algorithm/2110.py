#공유기 설치 이분탐색
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = list(int(input()) for x in range(N)) # 집 위치 리스트로 받기
home.sort() # 집 위치를 순서대로 나열하여 계산하기 편하게 함

# 가장 인접한 공유기의 거리가 최소가 되야하기때문에
min_dis = 1
max_dis = max(home) - min(home)

def find_install(min_dis, max_dis):
    ans = 1 # 최소값

    while min_dis <= max_dis:
        mid = (min_dis + max_dis) // 2
        wifi = home[0] # 공유기 설치
        cnt = 1

        for i in range(1, len(home)):
            if home[i] >= wifi + mid : # 비교할 값에 mid 거리 이상에 집이 있으면
                wifi = home[i]  # 공유기 설치
                cnt += 1

        if cnt >= C : # 공유기를 설치한 값이 C보다 크거나 같을 경우
            ans = mid
            min_dis = mid + 1 # 거리 늘리기 (더 좋은 값이 있을 수 있으니)
            
            
        else : # 공유기 설치한 값이 C에 도달하지 못한 경우
            max_dis = mid - 1 # 거리 줄이기
    
    return ans

print(find_install(min_dis, max_dis))