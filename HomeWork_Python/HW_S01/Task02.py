# Задача 2. Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ not
# ⋁ - or
# ⋀ - and

for X in 1, 0:
    for Y in 1, 0:
        for Z in 1, 0:
            print(f'{X = }, {Y = }, {Z = }  result: {not(X or Y or Z) == (not X and not Y and not Z)}')