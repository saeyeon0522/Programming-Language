############## 1 장 #############

'''print("a", "b", "c", sep="")




num1,num2 = input("number : ").split()
sum = int(num1) + int(num2)
print(f"{num1}과 {num2}의 합계는 {sum:,}이다.")




kor, eng, math = input("score : ").split()
sum = int(kor) + int(eng) + int(math)
avr = sum / 3
print(f"국어 : {kor}\n영어 : {eng}\n수학 : {math}\n총점 : {sum}\n평균 : {avr:.2f}")




won = int(input("cost : "))
dollar = won / 1196
print(f"환전하고 싶은 원화 {won:,}원은 US 달러로 $ {dollar:,.2f} 이다.")




up, down, height = input("length : ").split()
area = (int(up) + int(down)) * int(height) / 2
print(f"윗변(Cm) : {up}\n밑변(Cm) : {down}\n높이(Cm) : {height}\n사다리꼴의 넓이 : {area:.1f}")




name = input("name : ")
si, gu, dong = input("address : ").split(",")
print(f"{name}씨! 당신이 사는 곳은 {si} {gu} {dong}입니다.")



################### 2 차 시 ###################



tot = (3+3) * (5*2) / 2
print(tot)



fah = int(input("temp : "))
cel = (fah - 32.0) / 1.8
print(f"입력한 화씨온도 {fah}도는 섭씨온도로 {cel:,.2f} 이다.")



sec = int(input("second : "))
second = sec % 60
minute = (sec // 60) % 60
hour = (sec // 60) // 60
print(f"입력받은 {sec}초는 {hour}시간 {minute}분 {second}초 이다.")




################### 3 차 시 ######################




num = 16
num = num >> 2
print(num)


num1 = 0x19 & 0x20
print(num)
num2 = 0xf2 | 0x164
print(num2)
num3 = 0x7e ^ 0x2c
print(num3)




nb = int(input("number : "))
print(f"어떤 수 : {nb}")
print(f"2진수 : {bin(nb)}, 8진수 : {oct(nb)}, 10진수 : {nb}, 16진수 : {hex(nb)}")

print("\n")

print(f"어떤 수 : {nb}")
print("2진수 : {:b} , 8진수 : {:o}, 10진수 : {:d}, 16진수 : {:x}".format(35, 35, 35, 35))



val = int(input("num1 : "))
pwr = int(input("num2 : "))

print(f"어떤 값 : {val}\n왼쪽 쉬프트 : {pwr}\n왼쪽 쉬프트 {val} << {pwr} =", val << pwr)



alpha = input("alphabet : ")
print(f"당신이 입력한 문자 {alpha}는 대문자입니다.") if 'A' <= alpha <= 'Z' else print(f"당신이 입력한 문자 {alpha}는 소문자입니다.")



num = int(input("number : "))
print(f"어떤 숫자 : {num}")
print(f"당신이 입력한 숫자는 홀수입니다.") if num % 2 == 1 else print(f"당신이 입력한 숫자는 짝수입니다.")





#################### 4 차 시 ####################




gpa = float(input("gpa : "))
if gpa >= 4.0 :
    print("장학금 신청 가능")
else :
    print("학점 미달")



certi = input("자격증 유무 ( Y/N ) :")
grade = int(input("grade : "))
if certi == 'Y' and grade == 4 :
    print("지원 대상")
else :
    print("자격 미충족")



name = input("name : ")
height = int(input("height : ")) / 100
weight = int(input("weight : "))
bmi = weight / (height ** 2)
print(f"bmi : {bmi:.2f}")
if bmi >= 30 :
    print(f"{name}은 비만")
elif 29>= bmi and bmi >= 25 :
    print(f"{name}은 과체중")
elif 24>= bmi and bmi >= 20 :
    print(f"{name}은 정상")
else :
    print(f"{name}은 저체중")



use = int(input(" 1 집 2 공 3 산 : "))
kwh = float(input("amount : "))
if use == 1 :
    cost = 910 + 88 * kwh
elif use == 2 :
    cost  = 1600 + 182 * kwh
elif use == 3 :
    cost = 7300 * 275 * kwh
else :
    cost = -1

if cost >= 0 :
    print(f"cost : {cost:,.2f}원")
else :
    print("용도 잘못 입력")





################## 5 차 시 ##################

count = 0

for i in range(5) :
    num = int(input("num : "))
    if num % 2 == 0 :
        count += 1
print(f"even : {count}")




grade = [90, 85, 70, 60, 95]

for i in range(len(grade)) :
    if grade[i] >= 90 :
        print(f"{i + 1} 번 학생 {grade[i]}점 : 장학금 대상")




count = 0

while True :
    print("python !")
    count += 1
    if count == 3 :
        break





name = ['A', 'B', 'C']
for i in range(len(name)) :
    print(f"{name[i]}, hi")




animal = ["dog", "duck", "pony", "donkey", "giraffe", "elephant", "cat"] 
for i in range(len(animal)) :
    if len(animal[i]) <= 5 :
        print(animal[i])




word = "korea"
for i in range(len(word)) :
    print(word[i])






################## 6 차 시 ##################



res = 0

for i in range(5) :
    num = int(input("num : "))
    if num != 3 :
        print(f"{num}")
        res += num
print(f"sum : {res}")'




for i in range(4) :
    for j in range(4) :
        if j == 2 :
            continue
        else :
            print(f"{i} {j}")





nb = int(input("num : "))
sign = 1
for i in range(2, nb, 1) :
    if nb % i == 0 :
        print("소수 아님")
        sign = -1
        break
if sign == 1 :
    print("소수 맞음")




for i in range(1, 6, 1) :
    print("*" * i)


print("\n")

for i in range(5) :
    print(" " * i, end = "")
    print("*" * (5 - i))

    

for i in range(5) :
    print(" " * i, end = "")
    for j in range(i + 1, 6, 1) :
        print(j, end = "")
    print()



for i in range(5) :
    print(" " * (4 - i), end = "")
    for j in range(1, i + 2, 1) :
        print(j, end = "")
    print()'''

num1 = 10
num2 = 20
num3 = 30
num4 = 40
print("{0} {3} {2} {1}".format(num1, num2, num3, num4))