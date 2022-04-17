# 나무 자르기

N, M = map(int, input().split())  # n : 나무 개수, m : 원하는 나무 길이

tree_height = list(map(int, input().split())) # 나무의 높이
tree_height.sort(reverse=True)
cnt_tree = 0 # 집에 가져갈 나무의 길이
criteria = tree_height[1]   # 목재 절단기 기준 높이

while cnt_tree < M :
    cnt_tree = 0 # 기준이 초기화되므로 자른 목재 길이 총합도 초기화
    for x in tree_height : 
        diff = x - criteria  # 절단기로 자른 후 남은 길이
        if diff > 0 : # 양수일 경우 나무가 잘린 거니까 가져가기
            cnt_tree += diff
    criteria -= 1

print(criteria)