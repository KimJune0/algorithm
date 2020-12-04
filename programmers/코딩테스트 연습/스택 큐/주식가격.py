def find(arr, start):
    min = arr[start]
    ans = 0

    for i in range(start+1, len(arr)):
        if arr[i] < min:
            ans += 1
            return ans

        else:
            ans += 1

    return ans

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        answer[i] = find(prices, i)

    return answer


prices = [1, 2, 3, 2, 3]


print(solution(prices))



