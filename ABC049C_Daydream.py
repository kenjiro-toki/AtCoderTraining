S = input()
SCopy = S
T = ""


while len(S) > 0:
    A = S.find("dream")
    B = S.find("dreamer")
    C = S.find("erase")
    D = S.find("eraser")
    E = S.find("dreamera")  # dreameraserの並びの時のための汚い対処
    if B == 0 and E != 0:
        T += "dreamer"
        S = S.removeprefix("dreamer")
        # print(S)
    elif A == 0:
        T += "dream"
        S = S.removeprefix("dream")
        # print(S)
    elif D == 0:
        T += "eraser"
        S = S.removeprefix("eraser")
        # print(S)
    elif C == 0:
        T += "erase"
        S = S.removeprefix("erase")
        # print(S)
    else:
        print("NO")
        # print(S)
        break

if SCopy == T:
    print("YES")
