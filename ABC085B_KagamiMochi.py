N = int(input())
d_list = []
for i in range(N):
    d = int(input())
    d_list.append(d)

d_list.sort()
# print(d_list)

pre = 0
result = []
for i in d_list:
    if i != pre:
        result.append(i)
        pre = i

print(len(result))
