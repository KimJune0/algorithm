def solution(genres, plays):
    answer = []

    s = {}

    for i in range(len(genres)):
        if genres[i] not in s:
            s[genres[i]] = [plays[i], i, -1]

        else:
            sum = s[genres[i]][0]
            first_index = s[genres[i]][1]
            second_index = s[genres[i]][2]

            s[genres[i]][0] = sum + plays[i]

            if plays[first_index] < plays[i]:
                s[genres[i]][1] = i
                s[genres[i]][2] = first_index

            elif plays[first_index] == plays[i]:
                if i < first_index:
                    s[genres[i]][1] = i
                    s[genres[i]][2] = first_index

                else:
                    if plays[second_index] == plays[i] and i > second_index:
                        pass

                    else:
                        s[genres[i]][2] = i

            elif second_index == -1:
                s[genres[i]][2] = i

            elif plays[second_index] < plays[i]:
                s[genres[i]][2] = i

            elif plays[second_index] == plays[i]:
                if i < second_index:
                    s[genres[i]][2] = i

    s = sorted(s.items(), key=lambda x: x[1][0], reverse=True)

    for genre in s:
        answer.append(genre[1][1])

        if genre[1][2] != -1:
            answer.append(genre[1][2])

    return answer