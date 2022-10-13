############### 1 차 시 ###############

str1 = "Python"
str2 = "Programming"
str3 = "is"
str4 = "a amazing Language."

print(str1, str2, str3, str4)


kor, eng, math = 90, 80, 100
print(kor and eng and math >= 80)


'''kor = int(input("국어 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))
math = int(input("수학 점수를 입력하세요 : "))
avr = (kor + eng + math) / 3

print(f"국어 : {kor}점, 영어 : {eng}점, 수학 : {math}점, 평균 : {avr:.2f}점, 결과 : {avr < 60}")'''




############### 2 차 시 ###############


'''num1 = int(input("숫자 1을 입력하세요 : "))
num2 = int(input("숫자 2를 입력하세요 : "))
res = num1 << num2
print(f"왼쪽 쉬프트 {num1} << {num2} = {res}")'''



############### 3 차 시 ################



'''num = int(input("숫자를 입력하세요 : "))
print(f"당신이 입력한 숫자 {num}는(은) 3의 배수입니다.") if num % 3 == 0 else print(f"당신이 입력한 숫자 {num}는(은) 3의 배수가 아닙니다.")'''



'''price = int(input("가격을 입력하세요 : "))
print("할인 대상 : True") if price >= 60000 else ("할인 대상 : False")'''



age = int(input("나이를 입력하세요 : "))
print("이 등급의 영화를 볼 수 있습니다.") if age >= 17 else print("이 등급의 영화를 볼 수 없습니다.")