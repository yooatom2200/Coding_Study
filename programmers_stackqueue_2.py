def solution(bridge_length, weight, truck_weights):
    can = [0] * bridge_length
    after = []
    num_truck = len(truck_weights)
    answer = 0
    
    while can:
        answer += 1
        can.pop(0)
        if truck_weights:
            if sum(can) + truck_weights[0] <= weight:
                can.append(truck_weights.pop(0))
            else:
                can.append(0)
        
    return answer