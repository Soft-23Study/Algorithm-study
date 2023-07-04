# ---------------------------------------------------- 답 참고
# 1. stack 관리하며 괄호 적절성 체크하기
#   a. 열린 괄호를 만나면 -> stack 에 넣는다.
#   b. 닫힌 괄호를 만나면 -> stack 의 유효성 체크(stack 이 비어있진 않은지 + stack 마지막 값이 현재 괄호 모양과 상응하는지) -> stack pop 한다.
#   c. 마지막에 stack 이 완전히 비어 있는지 확인한다. (완전히 비어 있어야 제대로 된 괄호임 !!)
# 2. 덧셈, 곱셈 연산하기 (분배 법칙을 기억하자..)
#   a. 열린 괄호를 만나면 -> stack 에 넣으며 temp 에 *2 나 *3 을 한다.
#   b. 닫힌 괄호를 만나면 -> 이전 괄호에서 열린 뒤 바로 닫힌 경우(애기 괄호에 해당하는 경우) answer 에 더해준다.
#                    -> temp 를 다시 2나 3으로 나눠준다.
# ---------------------------------------------------- 
string = input()

stack = []
temp = 1
answer = 0

for i in range(len(string)):
    if string[i] == "(":
        stack.append(string[i])
        temp *= 2
    elif string[i] == "[":
        stack.append(string[i])
        temp *= 3
    elif string[i] == ")":
        if len(stack) == 0 or stack[-1] != "(":
            answer = 0
            break
        if string[i-1] == "(":
            answer += temp
        stack.pop()
        temp = temp // 2
    else:
        if len(stack) == 0 or stack[-1] != "[":
            answer = 0
            break
        if string[i-1] == "[":
            answer += temp
        stack.pop()
        temp = temp // 3

if stack:
    print(0)
else:
    print(answer)