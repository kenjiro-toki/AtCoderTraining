five_hundred = int(input())
one_hundred = int(input())
fifty = int(input())
sum = int(input())

calc_list = []

for i in range(five_hundred + 1):
    for j in range(one_hundred + 1):
        for k in range(fifty + 1):
            calc = i*500 + j*100 + k*50
            calc_list.append(calc)

print(calc_list.count(sum))
