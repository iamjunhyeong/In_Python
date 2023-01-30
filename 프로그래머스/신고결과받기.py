def solution(id_list, reports, k):
    mail = [0] * len(id_list)
    report_dict = {reportee: set() for reportee in id_list}
    for report in reports:
        split_report = report.split()
        reporter = split_report[0]
        reportee = split_report[1]
        report_dict[reportee].add(reporter)
    for reporters in report_dict.values():
        if len(reporters) >= k:
            for reporter in reporters:
                mail[id_list.index(reporter)] += 1
    return mail

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))