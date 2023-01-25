#################### 1 차 시 ##################


count = 0

for i in range(5) :
    count += 1
    for j in range(1, count + 1, 1) :
        print(j, end="")
    print("")



print("\n###########\n")



for i in range(1, 6, 1):
    for j in range(5, i - 1, -1):
        print(j, end = "")
    print()



print("\n###########\n")


count = 5
for i in range(5) :
    j = count
    for k in range(count) :
        print(j, end="")
        j -= 1
    count -= 1
    print("")



print("\n###########\n")



#################### 2 차 시 ##################




'''num = int(input("숫자를 입력하세요 : "))
print(f"숫자 입력 : {num}")
for i in range(num + 1) :
    if i <= 5 :
        print(i, end=" ")



print("\n###########\n")


sum = 0
while True:
    num = int(input("숫자를 입력하세요 : "))
    sum += num
    if num == 0 :
        break
print(f"합계={sum}")



print("\n###########\n")

count = 0
while True:
    animal= input("내가 좋아하는 동물?")
    count += 1
    if animal == "코알라":
        break
print(f"{count}회만에 정답을 맞추셨습니다.")'''




print("\n###########\n")




#################### 3 차 시 ##################




num = [15, 23, 42, 50, 22, 31, 1]
count = int(len(num))
for i in range(count):
    if num[i] % 2 == 1:
        print(num[i], end = " ")



print("\n###########\n")



'''sum =  0
for i in range(5):
    num = int(input("숫자를 입력하세요 : "))
    if num> 0 :
        sum += num
print(f"양수 정수 합계 : {sum}")




print("\n###########\n")



sum =  0
for i in range(5):
    num = int(input("숫자를 입력하세요 : "))
    if num != 3 :
        sum += num
print(f"합계:{sum}")'''




print("\n###########\n")


'''print("while 이용")

num = int(input("숫자 입력:"))
i = 2
flag = True
if i >= 2 :
    while i <= num / i :
        if num % i == 0:
            flag = False
            print(f"{num}은(는) 소수가 아닙니다.")
            break
        i += 1
if num >= 2 and flag == True:
    print(f"{num}은(는) 소수 입니다.")
else :
    print("입력값이 잘못 되었습니다")
        



print("for 사용")

num = int(input("숫자 입력:"))
i = 2
flag = True
if num >= 2 :
    for i in range(2, num // i + 1, 1) :
        if num % i == 0:
            flag = False
            print(f"{num}은(는) 소수가 아닙니다.")
            break
        i += 1
if num >=2 and flag == True:
    print(f"{num}은(는) 소수 입니다.")
else :
    print("입력값이 잘못 되었습니다")'''
        


for i in range(1, 6, 1):
    for j in range(1, i + 1, 1):
        print(j, end="")
    print()
