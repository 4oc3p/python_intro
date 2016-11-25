from time import asctime
import time


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

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
    r = {}
    for i in hw_results:
        r[i.get("id")] = sum(i.get("task_completion"))
    for i in test1_results:
        r[i.get("id")] += sum([test1_costs[a] * i.get("task_completion")[a-1] for a in test1_costs])
    for i in group:
        group[i]["rank"] = r[i]


def save_students_info(dct, sort_by_key="fullname", revers=False, rewrite=True):
    f = open("students_result.txt", ("a", "w")[rewrite])
    for student_id in sorted(dct, key=lambda w: dct[w][sort_by_key], reverse=revers):
        f.write("-"*41+"\n")
        f.write("%-20s %19s:" % (": ID: ", student_id)+"\n")
        f.write(":" + "."*39 + ":"+"\n")
        f.write("%-20s %19s:" % (": Full name:", dct[student_id]["fullname"])+"\n")
        f.write("%-20s %19s:" % (": Email:", dct[student_id]["email"])+"\n")
        f.write("%-20s %19s:" % (": Github:", dct[student_id]["github"].split("/")[-1])+"\n")
        f.write("%-20s %19s:" % (": Rank:", dct[student_id]["rank"])+"\n")
        f.write("-"*41+"\n")
    f.write(str(asctime())+"\n")
    f.close()


def print_students_info(file):
    f = open(file, "r")
    print(f.read())
    f.close()

with Profiler() as p:
    update_students_results()
    save_students_info(group, revers=True, sort_by_key="rank")
    print_students_info("students_result.txt")

