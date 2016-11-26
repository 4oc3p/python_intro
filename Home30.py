from time import asctime
import sys


group = {
    1024: {"fullname": "Грицаенко Евгений",  "email": "", "github": "https://github.com/ZhenyaGricaenko", "rank": 0},
    1025: {"fullname": "Гамов Олег",         "email": "", "github": "https://github.com/Aminazine", "rank": 0},
    1026: {"fullname": "Андреева Ольга",     "email": "", "github": "", "rank": 0},
    1027: {"fullname": "Алексеенко Наталия", "email": "", "github": "", "rank": 0},
    1028: {"fullname": "Петина Ольга",       "email": "", "github": "", "rank": 0},
    1029: {"fullname": "Балан Николай",      "email": "", "github": "https://github.com/Slipy901",  "rank": 0},
    1030: {"fullname": "Кривенко Максим",    "email": "", "github": "https://github.com/Maksym444", "rank": 0},
    1031: {"fullname": "Локтев Владимир",    "email": "", "github": "https://github.com/4oc3p",     "rank": 0},
    1032: {"fullname": "Сорокина Татьяна",   "email": "", "github": "", "rank": 0},
    1033: {"fullname": "Юрин Руслан",        "email": "", "github": "", "rank": 0},
    1034: {"fullname": "Румянцев Аркадий",   "email": "", "github": "", "rank": 0},
    1035: {"fullname": "Торбеев Алексей",    "email": "", "github": "", "rank": 0},
    1036: {"fullname": "Сташук Екатерина",   "email": "", "github": "", "rank": 0}
}

hw_results = [
    {"id": 1024, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] },
    {"id": 1025, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0] },
    {"id": 1026, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1027, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0] },
    {"id": 1028, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1029, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1030, "task_completion": [1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0] },
    {"id": 1031, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] },
    {"id": 1032, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1033, "task_completion": [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1034, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1035, "task_completion": [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1036, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] }
]


test1_results = [
    {"id": 1024, "task_completion": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
    {"id": 1025, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1026, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1027, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1028, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1029, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1030, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1031, "task_completion": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
    {"id": 1032, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1033, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1034, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1035, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"id": 1036, "task_completion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
]

test1_costs = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 2,
    7: 4,
    8: 4,
    9: 4,
    10: 8,
    11: 8,
    12: 15
}


def update_students_results():
    for hw_result in hw_results:
        group[hw_result.get("id")]["rank"] = sum(hw_result.get("task_completion"))
    for test1_result in test1_results:
        group[test1_result.get("id")]["rank"] += sum([test1_costs[a] * test1_result.get("task_completion")[a-1] for a in test1_costs])


def save_students_info(dct, sort_by_key="fullname", reverse=False, write_to_file=False, rewrite=True):
    file = (sys.stdout, open("results.txt", ("a", "w")[rewrite]))[write_to_file]
    for student_id in sorted(dct, key=lambda w: dct[w][sort_by_key], reverse=reverse):
        print("%s\n%-20s %30s:\n:%s:" % ("-"*52, ": ID: ", student_id, "."*50), file=file)
        for keys in sorted(dct[student_id]):
            print("%-15s %35s:" % (": " + keys.capitalize() + ":", dct[student_id][keys]), file=file)
        print("-"*52, file=file)
    print(str(asctime()), file=file)
    file.close()


update_students_results()
save_students_info(group, reverse=True, sort_by_key="rank")

