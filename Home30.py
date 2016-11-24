from time import asctime


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
    for i in group:
        for j in range(len(hw_results)):
            if hw_results[j].get("id") == i:
                group[i]["rank"] += sum(hw_results[j].get("task_completion"))
        for k in range(len(test1_results)):
            if hw_results[k].get("id") == i:
                l = [test1_results[k].get("task_completion")[y]*test1_costs[y+1] for y in range(len(test1_results[k].get("task_completion")))]
                group[i]["rank"] += sum(l)


def save_students_info(dct, sort_by_key="fullname", revers=False, rewrite=True):
    l = [dct[i][sort_by_key] for i in dct]
    if revers:
        l.sort(reverse=True)
    else:
        l.sort()
    checker = 0
    if rewrite:
        f = open("students_result.txt", "w")
    else:
        f = open("students_result", "a")
    while checker < len(dct):
        for i in dct:
            if dct[i][sort_by_key] == l[checker]:
                f.write("-"*41+"\n")
                f.write("%-20s %19s:" % (": ID: ", i)+"\n")
                f.write(":" + "."*39 + ":"+"\n")
                f.write("%-20s %19s:" % (": Full name:", dct[i]["fullname"])+"\n")
                f.write("%-20s %19s:" % (": Email:", dct[i]["email"])+"\n")
                f.write("%-20s %19s:" % (": Github:", dct[i]["github"][dct[i]["github"].rfind("/", 0)+1:])+"\n")
                f.write("%-20s %19s:" % (": Rank:", dct[i]["rank"])+"\n")
                f.write("-"*41+"\n")
        checker += 1
    f.write(str(asctime()))
    f.close()


def print_students_info(file):
    f = open(file, "r")
    print(f.read())
    f.close()


update_students_results()
save_students_info(group)
print_students_info("students_result.txt")

