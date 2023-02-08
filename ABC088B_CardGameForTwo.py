N = int(input())
num = list(map(int, input().split()))
# print(num)

Alice = []
Bob = []

for i in range(N):
    if num:
        Max = max(num)
        # print(Max)
        Alice.append(Max)
        num.remove(Max)
        # print(num)
        if num:
            Max = max(num)
            Bob.append(Max)
            num.remove(Max)
    else:
        break

Alice_sum = sum(Alice)
Bob_sum = sum(Bob)
result = Alice_sum - Bob_sum
print(result)
