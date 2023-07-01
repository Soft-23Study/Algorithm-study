# 절댓값 힙

# 정수 x input
# 배열에서 절댓값 작은 거 출력 -> 제거
# 작은 값이 같다면 원래 수 제일 작은거 출력 -> 제거


# 1st algorithm
# 음수와 양수로 구분
# 음수의 절댓값 최소 vs 양수의 절댓값 최소 비교
# 같다면 음수 쪽 걸 삭제

import sys,heapq

n = int(sys.stdin.readline())
arr_plus = []
arr_minus = []


for i in range(n):
    x = int(sys.stdin.readline())

    if x > 0 :
        # add x
        heapq.heappush(arr_plus,x) 
    elif x < 0 :
        heapq.heappush(arr_minus,-x) # 절댓값으로 넣기
    else :
        # 출력 x -> 제거
        if len(arr_plus)+len(arr_minus) == 0 :
            print(0)

        elif len(arr_plus) == 0 and len(arr_minus) != 0:
                print(-heapq.heappop(arr_minus))  
            
        elif len(arr_minus) == 0 and len(arr_plus) != 0:
                print(heapq.heappop(arr_plus)) 
        else : 
            if arr_plus[0] < arr_minus[0] :
                print(heapq.heappop(arr_plus)) 
            else:
                print(-heapq.heappop(arr_minus)) 

    # print(arr_plus)
    # print(arr_minus)

# 정리 : imput 말고 -> int(sys.stdin.readline()) 써야 시간 처리 빠름 

# (추가) 코드가 너무 복잡한것같아서 구글링하여 다른 코드 참고 
# 2st algorithm
# abs 절댓값 함수 쓴다

# import sys, heapq

# abs_heap = []
# n = int(sys.stdin.readline())
# for i in range(n):
# 	num = int(sys.stdin.readline())
# 	if num:
# 		heapq.heappush(abs_heap, (abs(num), num))
# 	else:
# 		if abs_heap:
# 			print(heapq.heappop(abs_heap)[1])
# 		else:
# 			print(0)

# 튜플 , abs 이용한 간단한 풀이
