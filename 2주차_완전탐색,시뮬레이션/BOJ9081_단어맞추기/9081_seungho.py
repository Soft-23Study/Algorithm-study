tc = int(input())

for i in range(tc):
    word = list(input())
    point = word[-1]
    answer = ""
    for i in range(len(word)-2, -1, -1):
        if ord(word[i]) < ord(point):
            # 앞 문자가 뒤 문자보다 작을때 (변곡점)
            min_word = word[i+1]
            min_word_idx = i+1
            for w in range(i+2, len(word)):
                if ord(word[i]) < ord(word[w]) < ord(min_word):
                    min_word = word[w]
                    min_word_idx = w
            word[min_word_idx] = word[i]
            word[i] = min_word
            answer = "".join(word[:i+1])
            for r in sorted(word[i+1:]):
                answer += r
            print(answer)
            break
        else:
            # 앞 문자가 뒤 문자보다 클때 (지나간다)
            point = word[i]
            if i==0:
                print("".join(word))


