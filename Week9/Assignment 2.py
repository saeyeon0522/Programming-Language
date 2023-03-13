num1 = int(input("첫 번째 수:"))
num2 = int(input("두 번째 수:"))
numlist = []

if num1 <= num2:
    for i in range(1, num1 + 1) :
        if num1 % i == 0 and num2 % i == 0:
            numlist.append(i)            
else:
    for i in range(1, num2 + 1) :
         if num1 % i == 0 and num2 % i == 0:
            numlist.append(i)

print("두 수 공약수 ", end = "")
print(numlist)
print(f"{num1}과 {num2}의 최대 공약수=", end="")
print(numlist[-1])
