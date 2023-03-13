for i in range(5, 0, -1) :
    print(" " * (5 - i), end = "")
    for j in range(i, 0, -1) :
        print(f"{j}", end = "")
    print()
