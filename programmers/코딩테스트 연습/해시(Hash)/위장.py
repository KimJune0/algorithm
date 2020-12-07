def solution(clothes):
    answer = 0

    s = {}

    for cloth in clothes:
        if hash(cloth[1]) not in s:
            s[hash(cloth[1])] = 1

        else:
            s[hash(cloth[1])] += 1

    first = True

    print(s)

    for gear in s:
        if first:
            answer = s[gear]
            first = False

        else:
            answer += answer * s[gear] + s[gear]

    return answer