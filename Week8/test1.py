num = int(input("어떤 수:"))
sign = 1

for i in range(2, num, 1) :
    if num % i == 0 :
        sign = -1
        break;
if sign == -1 :
    print(f"{num}은(는) 소수가 아닙니다")
else :
    print(f"{num}은(는) 소수입니다.")
