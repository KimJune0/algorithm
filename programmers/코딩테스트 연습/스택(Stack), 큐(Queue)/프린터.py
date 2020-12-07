def solution(priorities, location):
    arr = [0] * 10
    final = []
    find = False

    for i in range(len(priorities)):
        priorities[i] = [priorities[i], i]  # [[1,1], [1,2], [9,1], [1,3], [1,4], [1,5]]
        arr[priorities[i][0]] += 1

    k = 1

    while priorities:

        #print(k, priorities)
        #print(k, arr)
        k += 1
        tmp = priorities[0]
        priorities.pop(0)

        for i in range(tmp[0] + 1, 10):
            if arr[i] > 0:
                priorities.append(tmp)
                find = True
                break

        if find:
            find = False

        else:
            arr[tmp[0]] -= 1
            final.append(tmp)

    # print(final)

    for i in range(len(final)):
        if final[i][1] == location:
            return i+1


print(solution([5, 3, 1, 2, 3,5,1,2,3], 2))
