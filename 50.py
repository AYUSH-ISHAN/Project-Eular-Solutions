

list = []
def prime_checker(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    else:
        return 1

for j in range(2, 1000):
    if prime_checker(j):
        list.append(j)
print(list)
greatness_checker = 1
for list_len in range(1,len(list)):
    sub_list = list[0:list_len]
    #print(sub_list)
    contestant = len(sub_list)
    sum_of_sub_list = sum(sub_list)
    if contestant > greatness_checker and sum_of_sub_list in list:
            greatness_checker = contestant
            print(sum(sub_list))
