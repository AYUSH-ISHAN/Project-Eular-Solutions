import sys
sys.setrecursionlimit(9999999)

final = 999999
count = 1
iter = 100
max_num = 0
inter = 0

for n in range(800000, final):
    inter = n
    while inter != 1:
        if inter % 2 == 0:
            inter = inter / 2
            count += 1

        elif inter != 1:
            inter = 3 * inter + 1
            count += 1

    # else:
    #     list.append(count)
    if count > iter:
        max_num = n
        iter = count

    count = 1
print("largest chain is :", iter)
print("the number with largest chain :",max_num)
# print(list)
# max_value = max(list)
# print(max_value)
#
# for n in range(800000, final):
#     chain(n, iter)
#     print(iter)
#     if count == max_value:
#         print(n)
#     iter = 1
