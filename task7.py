# Для заданного целого числа X выведите 1, если оно положительное, -1, если оно отрицательное, 
# или 0, если оно равно
# в ноль.
# Попробуйте использовать для этого каскад if-elif-else.
list1 = [1,2,3,-5,-6,-9,0,45]
pol_list =[]
otr_list =[]
for y in list1:
    if y >= 1:
        pol_list.append(y)
    elif y <= -1:
        otr_list.append(y)
    else:
        continue
print(pol_list)
print(otr_list)

