import random
import pandas

# names = ["Alex", "Beth", "Ilya", "Marceline", "Caroline", "Eleanore", "Freddie", "Laraeminwe", "Eivana", "Maeve", "Medb"]

# short_names = [name for name in names if len(name) <= 4]

# long_caps_names = [name.upper() for name in names if len(name) > 5]

# print(long_caps_names)


# names = ["Alex", "Beth", "Ilya", "Marceline", "Caroline", "Eleanore", "Freddie", "Laraeminwe", "Eivana", "Maeve", "Medb"]

# students_scores = {name:random.randint(1, 100) for name in names}

# passed_students = {name:score for (name,score) in students_scores.items() if score >= 60}

# print(passed_students)

sorceresses_ranks = {
"sorceress": ["Elyssa the necromancer", "Eivana the bloodwitch", "Surtr the flame-caller"],
"level": [150, 99, 81]
}

sorceresses_dataframe = pandas.DataFrame(sorceresses_ranks)

# for (key, value) in sorceresses_dataframe.items():
#     print(value)

# pandas iterrows

for (index, row) in sorceresses_dataframe.iterrows():
    print(row.level)