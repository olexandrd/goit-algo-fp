nodes = [
    "Київ",
    "Львів",
    "Харків",
    "Одеса",
    "Дніпро",
    "Запоріжжя",
    "Івано-Франківськ",
    "Хмельницький",
    "Вінниця",
    "Чернівці",
    "Полтава",
    "Суми",
]


edges = [
    ("Київ", "Львів", {"weight": 8}),
    ("Київ", "Харків", {"weight": 9}),
    ("Львів", "Харків", {"weight": 38}),
    ("Харків", "Одеса", {"weight": 12}),
    ("Одеса", "Дніпро", {"weight": 7}),
    ("Дніпро", "Запоріжжя", {"weight": 1}),
    ("Івано-Франківськ", "Хмельницький", {"weight": 2}),
    ("Хмельницький", "Вінниця", {"weight": 2}),
    ("Вінниця", "Чернівці", {"weight": 14}),
    ("Полтава", "Суми", {"weight": 10}),
    ("Суми", "Київ", {"weight": 16}),
    ("Київ", "Івано-Франківськ", {"weight": 12}),
    ("Івано-Франківськ", "Чернівці", {"weight": 5}),
    ("Чернівці", "Харків", {"weight": 48}),
    ("Хмельницький", "Дніпро", {"weight": 44}),
    ("Одеса", "Львів", {"weight": 21}),
    ("Полтава", "Запоріжжя", {"weight": 8}),
    ("Івано-Франківськ", "Суми", {"weight": 41}),
    ("Вінниця", "Київ", {"weight": 4}),
    ("Чернівці", "Полтава", {"weight": 19}),
]


