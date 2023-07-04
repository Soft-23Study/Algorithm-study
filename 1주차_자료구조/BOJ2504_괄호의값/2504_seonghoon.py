
# 괄호 안의 값(예를 들면 " [(())] ")을 계산해주는 방법을 40분정도 고민하다가 막혀서 답안을 살펴봤다..

x = input()

stack = []
temp_result = []
result = 0

for i in range(len(x)):
    if x[i] == '(' or x[i] == '[':
        stack.append(x[i])
    elif x[i] == ')':
        temp = 0

        if not stack:
            result = 0
            break
        while stack:
            ch = stack.pop()
            if ch == '[':
                print(i)
                exit(0)  # return은 왜 안되지?
            elif ch == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            else:
                temp += ch

    elif x[i] == ']':
        temp = 0

        if not stack:
            result = 0
            break
        while stack:
            ch = stack.pop()
            if ch == '(':
                print(i)
                exit(0) # return은 왜 안되지?
            elif ch == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            else:
                temp += ch
    else:
        print(0)
        exit(0)

for i in stack:
    result += i

print(result)



