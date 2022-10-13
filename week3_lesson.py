############### 1 차 시 ###############


'''num1 = int(input("첫 번째 정수를 입력하세요 : "))
num2 = int(input("두 번째 정수를 입력하세요 : "))
num3 = int(input("세 번째 정수를 입력하세요 : "))
sum = num1 + num2 + num3

print(f"{num1}과 {num2}과 {num3}의 합은 {sum:,}이다.")'''



############### 2 차 시 ###############


grade = [70, 50, 80, 90, 60]
print(grade)
print(grade[0], grade[3])

fruit = []
print(fruit)

# 리스트 항목 추가
fruit.append("cherry")
fruit.append("peach")
fruit.append("melon")
fruit.append("blueberry")
fruit.append("pineapple")
fruit.append("kiwi")
print(fruit)

# 항목 삭제 (값 직접 입력)
fruit.remove("blueberry")
print(fruit)

# 항목 삭제 (인덱스 입력 / 리스트 자체 삭제)
del fruit[1]
print(fruit)
del fruit[-1]
print(fruit)
test = []
del test

# 항목 삭제 (마지막 / 인덱스 입력)
fruit.pop()
print(fruit)
fruit.pop(1)
print(fruit)


fruit.append("peach")
fruit.append("melon")
fruit.append("blueberry")

# 모든 항목 값 삭제
fruit.clear()
print(fruit)



############### 3 차 시 ################



print((5 * 5 + 2 * ((25 - 5) / 5)) ** 2)


'''son = int(input("분자를 입력하세요 : "))
mom = int(input("분모를 입력하세요 : "))

print("나눗셈 몫 =", son // mom)
print("나눗셈 나머지 =", son % mom)'''


fah = int(input("화씨 온도를 입력하세요 : "))
cel = (fah - 32.0) / 1.8
print(f"입력한 화씨 온도 {fah}은 섭씨 온도로 {cel:,.2f}도 이다.")