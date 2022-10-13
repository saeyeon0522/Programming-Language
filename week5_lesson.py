#################### 1 차 시 #######################



'''des = int(input("소프트웨어 설계 점수를 입력하세요 : "))
dev = int(input("소프트웨어 개발 점수를 입력하세요 : "))
db = int(input("데이터베이스 구축 점수를 입력하세요 : "))
lan = int(input("프로그래밍 언어 활용 점수를 입력하세요 : "))
sys = int(input("정보시스템 구축 관리 점수를 입력하세요 : "))
avr = int((des + dev + db + lan + sys) / 5)
if avr >= 60 and des >= 40 and dev >= 40 and db >= 40 and lan >= 40 and sys >= 40 :
    print(f"평균 : {avr}\n결과 : 합격")
else :
    print(f"평균 : {avr}\n결과 : 불합격")


score = float(input("이번 학기 학점을 입력하세요 : "))
if score >= 4.0 :
    print("장학금 신청 대상")
else :
    print("장학금 학점 미달")

num = int(input("숫자를 입력하세요 : "))
if num % 2 == 0 :
    print(f"입력한 수 {num}은 짝수이다.")
else :
    print(f"입력한 수 {num}은 홀수이다.")'''



#################### 2 차 시 #######################



'''num = int(input("숫자를 입력하세요 : "))
if num < 100 :
    if num > 50:
        print(f"입력한 수 {num}은 50보다 크고 100보다 작습니다.")
    else:
        print(f"입력한 수 {num}은 50보다 작습니다.")
else :
    print(f"입력한 수 {num}은 100보다 큽니다.")



num = int(input("숫자를 입력하세요"))
if num / 10 != 0 :
    if num /10 >= 10 :
        if num / 10 >= 100 and num / 10 < 1000:
            print("네 자릿수 숫자입니다.")
        else :
            print("세 자릿수 숫자입니다.")
    else :
        print("두 자릿수 숫자입니다.")
else :
    print("한 자릿수 숫자입니다.")'''



#################### 3 차 시 #######################



'''fruit=[]
fruit.append(input("과일을 입력하세요 : "))
fruit.append(input("과일을 입력하세요 : "))
fruit.append(input("과일을 입력하세요 : "))
fruit.append(input("과일을 입력하세요 : "))
fruit.append(input("과일을 입력하세요 : "))

if "딸기" in fruit:
    print("맛있는 딸기가 있습니다.")'''



sub = [1203, 1250, 1275, 1290]
num = int(input("교수과목 코드를 입력하세요 : "))
if not num in sub:
    print("해당 강좌 없음")
else:
    if num == sub[0]:
        print("과목명 : 파이썬 프로그래밍")
    elif num == sub[1]:
        print("과목명 : 컴퓨팅 사고")
    elif num == sub[2]:
        print("과목명 : 빅 데이터")
    else:
        print("과목명 : IoT")



speed = int(input("자동차 속도를 km/h 단위로 입력하세요 : "))
if speed >= 120:
    print(f"차량 속도 : {speed}, 속도 진단 : 고속")
elif speed >= 100:
    print(f"차량 속도 : {speed}, 속도 진단 : 과속")
elif speed >= 60:
    print(f"차량 속도 : {speed}, 속도 진단 : 중속(안전 운행)")
else:
    print(f"차량 속도 : {speed}, 속도 진단 : 저속")
