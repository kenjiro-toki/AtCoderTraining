N, Y = map(int, input().split())

for x in range(N+1):
    for y in range(N+1):
        for z in range(N+1):
            sum = 10000*x + 5000*y + 1000*z
            total = x + y + z
            # print(total)
            if sum == Y and total == N:
                print(f"{x} {y} {z}")
                break
            elif x == y == z == N:
                print("-1 -1 -1")
                break
        else:
            continue
        break
    else:
        continue
    break
