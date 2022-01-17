from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_index = {string: i for i, string in enumerate(id_list)}

    violator_dict = defaultdict(set)
    for log in report:
        temp = log.split(" ")
        reporter = temp[0]
        violator = temp[1]
        violator_dict[violator].add(reporter)

    for reporters in violator_dict.values():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_index[reporter]]+=1

    return answer