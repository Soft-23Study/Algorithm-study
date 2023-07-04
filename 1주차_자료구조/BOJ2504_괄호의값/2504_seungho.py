questions = list(input())

box = [] # 괄호 저장 스택
plus = [] # 중간 버퍼 : 괄호 안에서 더해져야 할 값들 저장
multiply = [] # 초기 버퍼 : 괄호 안에서 곱해져야 할 값들 저장
final = [] # 최종 버퍼 : 괄호 없는 상태에서 최종 값들 저장
result = -1 # 비정상괄호는 0 / 정상괄호는 sum(final)

for q in questions:
    if q in ['(', '[']: #push
        if len(multiply)>0:
            temp_mul = 1
            for a in multiply: #push 때릴때 multiply 스택에 값 있으면, 곱한 값들을 plus 스택으로 옮긴다.
                temp_mul *= a
            plus.append(temp_mul)
            multiply.clear()
        box.append(q) #push
    elif q==')': #pop
        if len(box) == 0 or box[-1] == '[': #비정상괄호
            result = 0
            break
        if len(box)>=2: #속괄호일때는 현재 값 multiply로 이동
            multiply.append(2)
            box.pop()
        elif len(box)==1: #겉괄호일때는 multiply 값 있으면 곱한 다음 plus에 push
            temp_mul = 1
            for a in multiply:
                temp_mul *= a
            plus.append(temp_mul)
            multiply.clear()
            box.pop() #pop
            final.append(2*sum(plus)) #plus에 있는 값들을 합한 후 2 곱하고 final에 push
            plus.clear()
    elif q==']':
        if len(box) == 0 or box[-1] == '(':
            result = 0
            break
        if len(box) >= 2:
            multiply.append(3)
            box.pop()
        elif len(box)==1:
            temp_mul = 1
            for a in multiply:
                temp_mul *= a
            plus.append(temp_mul)
            multiply.clear()
            box.pop()
            final.append(3*sum(plus)) #plus에 있는 값들을 합한 후 2 곱하고 final에 push
            plus.clear()
if result==0 or len(box)>0:
    print(0)
else:
    print(sum(final))

'''
indexError로 삽질을 하긴 했지만, 잘 고친다음 맞추나 싶었는데 채점중(40%)에서 실패...
풀이를 봐도 내 풀이가 어디서 틀린 부분이 있는지를 모르겠다.
더 연구해봐야 할 문제
'''