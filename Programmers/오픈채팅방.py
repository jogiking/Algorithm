def solution(record):
    answer = []
    user_dict = {}
    for log in record:
        temp = log.split(" ")
        op, uid = temp[0], temp[1]
        if op == "Enter":
            answer.append([uid, "님이 들어왔습니다."])
            user_dict[uid] = temp[2]
        elif op == "Leave":
            answer.append([uid, "님이 나갔습니다."])
        elif op == "Change":
            user_dict[uid] = temp[2]

    return list(map(lambda x: user_dict[x[0]]+x[1], answer))