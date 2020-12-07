def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    num = len(completion)
    
    answer = participant[num]
    
    for i in range(num):
        if participant[i] != completion[i]:
            answer = participant[i]
            break;
    
    return answer