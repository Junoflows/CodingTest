from collections import deque
def solution(participant, completion):
    participant = deque(sorted(participant))
    completion = deque(sorted(completion))

    li = []
    while True:
        if completion == deque([]):
            break
        if completion[0] == participant[0]:
            completion.popleft()
            participant.popleft()
        elif completion[0] != participant[0]:
            return participant[0]
    
    if li == []:
        return [x for x in participant if x not in completion][0]
    else:
        return li[0]
