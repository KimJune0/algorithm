def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    timer = 0
    while truck_weights:
        if sum(bridge[1:]) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            while bridge[1] == 0:
                bridge.pop(0)
                bridge.append(0)
                timer += 1
            bridge.append(0)

        timer += 1
        bridge.pop(0)

    timer += len(bridge)
    return timer


print(solution(3, 10, [1, 2, 3, 5]))

