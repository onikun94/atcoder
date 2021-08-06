def TrueTen(num):
    incNum = num + 1
    if incNum == 10:
        return 0
    else:
        return incNum


if __name__ == "__main__":
    pasw = input()
    x1 = int(pasw[0])
    x2 = int(pasw[1])
    x3 = int(pasw[2])
    x4 = int(pasw[3])

    x1a = TrueTen(x1)
    x2a = TrueTen(x2)
    x3a = TrueTen(x3)

    if x1 == x2 == x3 == x4:
        print("Weak")
    elif x4 == x3a and x3 == x2a and x2 == x1a:
        print("Weak")
    else:
        print("Strong")
