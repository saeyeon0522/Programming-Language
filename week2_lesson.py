################## 2 차 시 #################

a = 10 
b = 20
print(a+b)



'''a = int(input("a를 입력하세요 : "))
b = int(input("b를 입력하세요 : "))
if a > b :
    print(f"{a}")
else :
    print(f"{b}")'''



num = 1
while num <= 100 :
    print(f"{num}")
    num += 1

num = 1
sum = 0
while num <= 100 :
    sum += num
    num += 1
print(f"{sum}")
print(101 * 50)



even = 2
while even <= 100 :
    print(f"{even}")
    even += 2



################### 3 차 시 ####################



name = "Saeyeon"
print("My name is", name, ".")  # 앞뒤 띄어쓰기 자동
regular = 2000000
bonus = 500000
salary = regular + bonus

# 숫자 세 자리마다 콤마
print("{0}의 월급은 기본급 {1:,}원, 보너스 {2:,}원, 총 급여액 {3:,}원이다." .format(name, regular, bonus, salary))



num1, num2, num3 = 100, 200, 300

# 정수형 숫자 자리 형식 지정 : d 앞에 숫자
print("{0:d},{1:5d},{2:05d}".format(num1, num2, num3))



num1 = 4500000000
num2 = 100000.29354

# 실수형 숫자 자리 형식 지정 : f 앞에 숫자
print("num1 : {0:0,.2f}, num2 : {1:,.2f}" .format(num1, num2))
