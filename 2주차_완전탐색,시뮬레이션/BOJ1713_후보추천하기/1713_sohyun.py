# 후보 추천하기

# 문제
# 일정기간 동안 전체 학생의 추천에 의해 선정됨
# 후보 수 만큼 사진들을 만듬
# 초기에 사진틀은 다 비어있음
# A가 B 추천 -> 추천받은 B사진 틀에 게시
# 비어있는 사진틀 없으면 추천 받은 횟수 가장 적은 학생 사진 삭제 후 새로운 친구
# 적은 친구가 두명넘으면 오래된 사진 삭제
# 기존 사진에 있는 학생이 추천받으면 추천 횟수만 증가
# 삭제된 학생의 추천수는 0으로 바뀜
#최종후보가 누구인지 구하시오


# 알고리즘 구상
# 순서대로 투표한 값에 따라 배열을 잡아서 인덱스 올려주고
# 최댓값을 이용해서 배열 하나에 다 해결하려고 했는데 최대를 여러개 꺼낸다는게 구현 방법 모르겠음
# 그래서 후보에 들어간 친구들 배열과 득표 배열을 따로 잡아서 시도
import sys

n = int(sys.stdin.readline())
s = int(sys.stdin.readline())
vote_lst = list(map(int,sys.stdin.readline().split()))

ans = []
ans_check = [] # 득표수를 담는 배열

for i in vote_lst:
    # print(i)
    # 후보인 친구가 득표했을때 그냥 +1 / 변화는 결과는 없음
    if i in ans: 
        idx = ans.index(i)
        ans_check[idx] += 1
    #후보 아닌 친구가 득표
    else: 
        # 만약에 후보 수를 넘어가게 추가가 된거면 
        if len(ans) >= n: 
            idx = ans_check.index(min(ans_check))
            ans.pop(idx)
            ans_check.pop(idx)
            #득표수도 0 된니까 그냥 빼버려
        #그냥 추가
        ans.append(i)
        ans_check.append(1)
 
ans.sort()   # 증가하는 순서         
print(*ans) # 괄호없애고 출력