N = int(input())
num = input().split()

counter = 0
a = 0
while a == 0:
    for i in range(N):
        if int(num[i]) % 2 != 0:
            a += 1
            print(counter)
            break

        num[i] = int(num[i]) / 2
    counter += 1
