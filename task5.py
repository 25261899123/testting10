"""Дан список целых чисел. Заменить отрицательные на -1, положительные - на число 1, ноль
оставить без изменений.
"""
Spisoks = [1,2,6,-23,4,-14,-133,523,0]
new_spisoks = []
for spisok in Spisoks:
    if spisok > 0:
        new_spisoks.append(1)
    elif spisok < 0:
        new_spisoks.append(-1)
    else:
        new_spisoks.append(0)
        print (new_spisoks)

