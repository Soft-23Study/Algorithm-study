c, p = map(int, input().split())
field = list(map(int, input().split()))

shape = [[ [0], [0, 0, 0, 0] ],
         [ [0, 0]],
         [ [0, 0, 1], [1, 0] ],
         [ [1, 0, 0], [0, 1] ],
         [ [0, 0, 0], [1, 0, 1], [ 1, 0 ], [ 0, 1 ] ],
         [ [0, 0, 0], [0, 0], [0, 1, 1], [2, 0] ],
         [ [0, 0, 0], [0, 0], [1, 1, 0], [0, 2] ]]

answer = 0

for case in shape[p-1]:
    for i in range(c - len(case) + 1):
        temp = []
        for k in range(len(case)):
            temp.append(field[i+k] - case[k])

        isAnswer = True
        for k in range(len(case) - 1):
            if temp[k] != temp[k+1]:
                isAnswer = False
                break

        if isAnswer:
            answer += 1


print(answer)


