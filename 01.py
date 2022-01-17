def qsort(a):
    if len(a) == 2:
        if a[0] > a[1]:
            a[0], a[1] = a[1], a[0]
        return a
    # Если длинна списка больше 2
    elif len(a) > 2:
        # То считаем среднее
        average = sum(a) // len(a)
        sp_1 = [] # Элементы меньше среднего
        sp_2 = [] # Элементы равные среднему
        sp_3 = [] # Элементы больше среднего

        for i in a:
            if i < average:
                sp_1.append(i)
            elif i > average:
                sp_3.append(i)
            else:
                sp_2.append(i)
        return qsort(sp_1) + sp_2 + qsort(sp_3)

    else:
        return a


a = [5, 8, 1, 5, 3, 5, 2, 0, 2, 5, 2]
print(a)
a = qsort(a)
print(a)