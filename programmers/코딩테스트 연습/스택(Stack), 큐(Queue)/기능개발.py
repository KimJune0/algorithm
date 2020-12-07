import math


def solution(progresses, speeds):

    answer = []
    start = 0
    count = 0

    while start != len(progresses) - 1:

        day = math.ceil((100 - progresses[start]) / speeds[start])
        count += 1

        for i in range(start + 1, len(progresses)):
            progresses[i] += day * speeds[i]

        for i in range(start + 1, len(progresses)):
            if progresses[i] >= 100:
                count += 1

            else:
                print("append %d start %d" % (count, i))
                answer.append(count)
                start = i
                count = 0
                break

            if i == len(progresses) - 1:
                answer.append(count)
                start = i

    if count == 0:
        answer.append(1)

    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))


