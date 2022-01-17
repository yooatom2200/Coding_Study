"""
sum() 자체 함수는 시간이 오래 걸린다
무게 관리에 대한 변수만 추가해주고 실행하면
소요시간을 짧게 할 수 있다.
"""
def solution(bridge_length, weight, truck_weights):
    can = [0] * bridge_length
    after = []
    num_truck = len(truck_weights)
    answer = 0
    total_weight = 0
    while can:
        answer += 1
        total_weight -= can.pop(0)
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                tmp = truck_weights.pop(0)
                can.append(tmp)
                total_weight += tmp
            else:
                can.append(0)
        
    return answer