while True :
    num = int(input("구구단 입력:"))
    print(f"구구단 입력:{num}")
    if num == 0 :
        print("Good Bye!")
        break
    else :
        i = 1
        while i < 10 :
            print("{0} * {1} = {2}".format(str(num), str(i), str(num * i)))
            i += 1
