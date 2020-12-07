import heapq


def solution(scoville, K):
    answer = 0
    heap = []

    for s in scoville:
        heapq.heappush(heap, s)
        # print(heap)

    while True:
        tmp = heapq.heappop(heap)
        # print("tmp", tmp)
        if tmp < K:
            if len(heap) < 1:
                return -1

            # print("after pop", heap)
            heapq.heappush(heap, tmp + 2 * heapq.heappop(heap))
            # print("after push", heap)
            answer += 1

        else:
            return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
