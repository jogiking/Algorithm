# 풀이시간 43분(문제읽기 10분)
# 오래걸린 원인은? -> 각 단계별로 어떻게 풀건지 충분히 정리를 하지 않은 상태에서 문제를 풀어나감(여기서 이렇게하고 다음 단계되고 다시 생각하는 과정을 반복) -> 이게 정말 원인일까?

def get_diff(start, end):
    s_h, s_m = list(map(int, start.split(":")))
    e_h, e_m = list(map(int, end.split(":")))
    return (e_h*60+e_m)-(s_h*60+s_m)
    
def solution(fees, records):    
    answer = []
    total_time = {}
    parking_cars = {}
    for log in records:
        log_time, car_number, status = log.split()
        if status == "IN":
            if car_number not in total_time:
                total_time[car_number] = 0
            parking_cars[car_number] = log_time
        elif status == "OUT":
            total_time[car_number] += get_diff(parking_cars[car_number], log_time)
            del parking_cars[car_number]

    # 23:59까지 아직 나가지 않은 차들의 시간 추가
    for remain in parking_cars:
        total_time[remain] += get_diff(parking_cars[remain], "23:59")

    for car_number, total in sorted(total_time.items()):
        cost = fees[1] + max((total-fees[0]+fees[2]-1)//fees[2]*fees[3], 0)
        answer.append(cost)
    return answer