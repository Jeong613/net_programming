# 패션왕 신해빈

from itertools import combinations
T = int(input())  # 테스트 개수

for t in range(T):
    outfits_num = int(input())  # 의상 수
    outfits = []  # 옷 리스트
    ans = []  # 조합된 옷 리스트
    for i in range(outfits_num):
        clothes, category = input().split()
        outfits.append(category)  # 입력 받기 오룬쪽만 입력 받기
    S = set(outfits)  # 중복 삭제
    diff = len(outfits) - len(S)  # 중복과 원래 옷의 차이

    if len(S) != 1:  # 모든 옷 종류가 같지 않을 경우
        for i in range(1, len(outfits)):
            for x in list(combinations(outfits, i)):
                ans.append(x)
        print(len(ans) - diff)
    else:  # 한가지 종류일 경우
        print(len(outfits))
