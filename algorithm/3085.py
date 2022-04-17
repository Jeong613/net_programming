# 사탕게임
# input은 sys.stdin.readline 하는게 좋음

N = int(input()) # 행, 열 길이 받기
arr = [list(input()) for _ in range(N)]  # 사탕 색상 받아오기
ans = 0 # 사탕 최대 개수

def check(arr):
    n = len(arr)
    ans = 1 # 사탕 최소 값 = 1
    
    for i in range(n):
        # 열 확인
        cnt = 1 # 먹을 수 있는 사탕 최소 값 
        for j in range(n - 1): # n까지 바꿔야하니까
            if arr[i][j] == arr[i][j + 1]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt > ans: # 먹을 수 있는 사탕값이 최소값보다 클 때 ans에 담아주기
                ans = cnt
        # 행 확인        
        cnt = 1
        for j in range(n - 1):
            if arr[j][i] == arr[j + 1][i]:
                cnt +=1
            else:
                cnt = 1
            
            if cnt > ans: 
                ans = cnt # 먹을 수 있는 사탕값이 최소값보다 클 때 ans에 담아주기
                
    return ans


for i in range(N):
    for j in range(N):
        # 열 바꾸기
        if j+1 < N: # j+1 - 인접한 부분
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            
            temp = check(arr)
            
            if temp > ans:
                ans = temp
            # 다시 바꿔두기    
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            
        # 행 바꾸기
        if i + 1 < N:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            
            temp = check(arr)
            
            if temp > ans:
                ans = temp
            # 다시 바꿔두기    
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(ans)