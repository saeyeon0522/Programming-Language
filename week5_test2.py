name = str(input("이름을 입력하세요 : "))
kor = int(input("국어 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))
math = int(input("수학 점수를 입력하세요 : "))
avr = (kor + eng + math) / 3
sub = kor + eng + math

if avr >= 95:
    score = "A+"
elif avr >= 90:
    score = "A"
elif avr >= 85:
    score = "B+"
elif avr >= 80:
    score = "B"
elif avr >= 75:
    score = "C+"
elif avr >= 70:
    score = "C"
elif avr >= 65:
    score = "D+"
elif avr > 60:
    score = "D"
else:
    score = "F"
    
print(f"{name}군의 총점은 {sub}점, 평균은 {avr:0.2f} 점, 학점은 {score}학점입니다.")
