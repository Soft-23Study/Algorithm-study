import sys

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    people = []
    for _ in range(n):
        first, sec = map(int,sys.stdin.readline().split())
        people.append((first,sec))

    answer = 1
    
    people.sort()

    sec_pass_limit = people[0][1]
    for j in range(1,n):
        if people[j][1] < sec_pass_limit: 
            answer += 1 
            sec_pass_limit = people[j][1]

    print(answer)