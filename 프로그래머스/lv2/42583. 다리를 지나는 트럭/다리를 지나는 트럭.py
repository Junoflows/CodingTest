def solution(bridge_length, weight, truck_weights):
    cnt = 0
    stack = [0 for _ in range(bridge_length)]
    hap = sum(stack)
    while True:
        if truck_weights == []:
            return cnt + bridge_length
        
        if truck_weights[0] + hap > weight:
            if truck_weights[0] + hap - stack[0] <= weight:
                hap = hap - stack[0] + truck_weights[0]
                stack.append(truck_weights.pop(0))
                stack.pop(0)
                cnt += 1
            else:
                hap -= stack[0]
                stack.append(0)
                stack.pop(0)
                cnt += 1
        elif truck_weights[0] + hap <= weight:
            hap = hap - stack[0] + truck_weights[0]
            stack.append(truck_weights.pop(0))
            stack.pop(0)
            cnt += 1