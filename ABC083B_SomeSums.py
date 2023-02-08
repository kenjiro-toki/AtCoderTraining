N, A, B = map(int, input().split())

output = []
for i in range(N):
    num = [int(a) for a in str(i+1)]
    # print(num)
    total_num = sum(num)
    # print(total_num)
    if total_num >= A and total_num <= B:
        # print(i+1)
        output.append(i+1)

print(sum(output))
