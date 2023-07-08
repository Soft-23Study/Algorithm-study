import sys

size = int(input())

for i in range(0,size):
    word = list(map(str, input().rstrip()))
    result = word

    a_index = len(word) - 2
    while a_index >= 0:
        if word[a_index] < word[a_index+1]:
            break
        a_index -= 1

    if a_index == -1:
        print("".join(result))
        continue

    b_index = len(word) - 1
    while b_index != a_index:
        if word[a_index] < word[b_index]:
            break
        b_index -= 1

    word[a_index], word[b_index] = word[b_index], word[a_index]


    # 이 부분은 구현하는 코드가 있을것 같아서 찾아봤더니 있길래 배웠음
    result = word[:a_index+1]
    result.extend((list(reversed(word[a_index+1:]))))
    print("".join(result))