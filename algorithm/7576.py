# 토마토
from collections import deque

M, N = map(int, input().split()) # M : 열, N : 행
box = [list(map(int, input().split())) for _ in range(N)] # 토마토 박스리스트에 넣기
q = deque([])

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    day = 0  # 최소 날짜
    while q:
        day += 1

        for z in range(len(q)):
            x, y = q.popleft()

            for i in range(4): # 상하좌우 4번만 돌아가면 되니까
                nx = x + dx[i]
                ny = y + dy[i]

                # 해당 좌표가 박스크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
                if -1 < nx < N and -1 < ny < M and box[nx][ny] == 0:
                    box[nx][ny] = 1 # 익은 토마토로 바꿔주기
                    q.append([nx, ny])
    
    for i in range(N): # 다 돌았는데 안익은 토마토 있으면 -1 반환
        for j in range(M):
            if box[i][j] == 0 :
                return -1
            
    return day - 1  # 모두 익었으면 day 출력



for i in range(N):
    for j in range(M):
        if box[i][j] == 1: # 익은 토마토부터 bfs시작
            q.append([i,j])

print(bfs())
