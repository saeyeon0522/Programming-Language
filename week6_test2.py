num = [15, 23, 45, 11, 55]
sum = 0

for i in range(5):
    sum += num[i]
    print(num[i])

avr = sum / 5
print(f"합계:{sum}")
print(f"평균:{avr:.2f}")
