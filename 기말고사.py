################## 9 주 차 ##################

num = [10, 15, 20, 25, 30]
res = 0
for i in num:
    res += i
print(res)


number = [1, 2, 3, 3, 4, 5, 6, 7, 3, 2, 8, 9, 10]
count = number.count(3)
print(f"3의 개수={count}개")


num = [15, 23, 18, 47, 23]
odd = 0
even = 0
for i in num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"홀수 개수 = {odd}개\n짝수 개수 = {even}개")


numA = [1, 2, 3]
numB = [10, 20, 30]
print(numA)
numA.extend(numB)
print(numA)


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alpha[4])
print(alpha[-5])
print(alpha[2:6])
print(alpha[-6:-2])


num = [43, 12, 3, 7, 72, 25]
num.sort()
print(num)  #sort : 오름차순


alpha = ['K', 'C', 't', 'E', 'b', 'a', 'M']
alpha.sort()
print(alpha)


num = [15, 11, 9, 6, 3]
num.sort(reverse=True)
print(num)


num = [11, 23, 5, 7, 15, 9, 8]
print(f"정렬전:{num}")
num.sort(reverse=True)
print(f"정렬전:{num}")




################## 10 주 차 ####################

flower = ("국화", "튤립", "장미", "수국")
flowerlist = list(flower)
print(flower)
flowerlist.append("민들레")
print(flowerlist)
flower = tuple(flowerlist)
print(flower)



num = (11, 12, 13, 14, 15)
res = 0
for i in num:
    print(i)
    res += i
print(f"합계={res}")



num = [12, 15, 8, 4, 9]
new1 = sorted(num)
print(new1)
num2 = sorted(num, reverse=True)
print(num2)



lan = ["java", "c", "r", "pascal", "sql", "python"]
newlan1 = sorted(lan, key=lambda x:x[0], reverse=False)
newlan2 = sorted(lan, key=lambda x:x[0], reverse=True)
print(newlan1)
print(newlan2)



num = (20, 30, 15, 31, 23)
new = sorted(num, reverse=False)
res = 0
for i in new:
    print(i)
    res += i
print(f"합계:{res}")




num = [[10, 20], [30, 40], [50,60]]
for i, j in num:
    print(i, j)

for i in num:
    for j in i:
        print(j, end = " ")
    print()



book = [("java", 15000), ("python", 25000), ("c", 18000), ("java", 19000)]
newbook = sorted(book, key= lambda x:x[1], reverse=True)
for i in newbook:
    for j in i:
        print(j, end = "\t")
    print()

for i, j in newbook:
    print("{}\t{}".format(i, j))



student=[("인터넷","이정재","010-123-1234", 90),
("미디어","전지현","010-123-4560", 80), ("정통과","송혜교","010-123-2244", 100),
("컴퓨터","김소현","010-123-3355", 85), ("국문과","강하늘","010-123-7890", 95)]

newstd = sorted(student, key=lambda x:x[3], reverse=True)
print("학 과 \t이 름\t연락처\t\t점수")
for i, j, m, n in newstd:
    print("{}\t{}\t{}\t{}".format(i, j, m, n))



grade={}
grade["아이키"]=90
grade["박보검"]=95
grade["유아인"]=80
grade["전지현"]=100
grade["송중기"]=90

print(grade)
print(grade["전지현"])
print(grade.keys())
print(grade.values())
print(grade.items())

for i in grade.keys():
    print(i)

for i in grade.values():
    print(i)

for i in grade.keys():
    print(i, grade[i])



name = ["이순신", "강감찬", "홍길동"]
score = [80, 90, 100]
new = dict(zip(name, score))
print(new)



grade={'아이키': 90, '박보검': 95, '유아인': 85, '전지현': 100, '송중기': 90}
res = 0
for i in grade.keys():
    print(i, grade[i])
    res += grade[i]
print("========")
print(f"합 계:{res}")



movie_list=[("오징어게임",50.45), ("이터널스",35.46),("그레비티",9.8), ("노타임투다이",52.5),
("스파이더맨",15.47)]
movie = sorted(movie_list, key=lambda x:x[1], reverse=True)
newmovie = dict(movie)
order = 0
print("영화제목\t예매율\t순위")
print("========\t=====\t====")
for i in newmovie.keys():
    order += 1
    print("{}\t{}\t{}".format(i, newmovie[i], order))



def func():
    for i in range(5):
        print("python")
func()


'''def multi():
    n = int(input("원하는 구구단:")) 
    for i in range(9):
        print("{}*{}={}".format(n, i+1, n*(i+1)))
multi()'''


def printArgs(*args):
    for i in args:
        print(i)
printArgs("python", "is", "first", "language")


def printkArgs(**kargs):
    for i, j in kargs.items():
        print(f"{i} : {j}")
printkArgs(key="123", value="A")


def myfunc(a, b):
    hap = a + b
    return hap

a = 10
b = 20
res = myfunc(a, b)
print("{}+{}={}".format(a, b, res))



'''def factorial():
    n = int(input("어떤 숫자: "))
    result = 1
    for i in range(1, n+1, 1):
        result *= i
    print("{}!={}".format(n, result))

factorial()'''



def add1(x, y):
    hap = x + y
    print("합계:", hap)

add1(10, 20)

def add2(x, y):
    hap = x + y
    return hap

print("합계:", add2(10, 20))

def add3():
    a = 10
    b = 20
    print("{}+{}={}".format(a, b, a+b))

add3()



def rect(b, h):
    b = 10
    h = 30
    w = b*h
    return w

'''base = int(input("밑변:"))
high = int(input("높이:"))
result = rect(base, high)
print("사각형의 넓이:", result)'''



'''def plus():
    n = int(input("숫자:"))
    res = 0
    for i in range(1, n+1, 1):
        res += i
        print("{} {}".format(i, res))

plus()'''



apple = 10
def eatApple(n):
    global apple
    apple -= n
    print(f"남은 사과 개수={apple}개")

eatApple(1)
eatApple(3)
eatApple(2)



import math #수학 함수는 소수 첫째자리에서 연산 수행
x = 2.487
y = -2.56

print(math.ceil(x)) #ceil은 무조건 올려서 출력
print(math.ceil(y)) 


print(math.floor(x)) #floor은 무조건 내려서 출럭
print(math.floor(y))


print(math.trunc(x)) #trunc는 무조건 절사
print(math.trunc(y))


print(math.sqrt(100)) #제곱근
print(math.sqrt(10))


print(math.pow(2,3)) #x의 y제곱



# import math 필요 없음 
x = 2.56
y = -2.55
print(round(x,1)) #반올림 구함, 소수 자리 수 지정 가능
print(round(y,0)) 


a = -12
print(abs(a)) # 절대값

print(divmod(15, 3)) # 몫, 나머지 (몫은 정수 실수 모두 한 자리만 출력)

num = [15, 25.5, 33, 47, -11]
print("최대값 :", max(num))
print("최소값 :", min(num))
print("합계 :", sum(num))
print(sum(num, 10)) # 합계 추가 가능

print(chr(48)) # ascii -> char
print(chr(65))
print(chr(97))

print(ord("0")) # char -> ascii
print(ord("A"))
print(ord("a"))


sen = "python programming"
print(sen.find("p")) # 문자 위치 값
print(sen.index("o"))
print(sen.index("o", 7, 18)) # 검색 구간 설정


print(sen.replace("python", "c")) # 단어 변환
print(sen.capitalize()) # 첫글자만 대문자로 변환
print(sen.upper()) # 전부 대문자
print(sen.lower()) # 전부 소문자



'''while True:
    char = input("입력문자:")
    if char == "end" or char == "END":
        break
    if 'A' <= char and char <= 'Z':
        print("입력한 문자 {}는 대문자입니다.".format(char))
    elif 'a' <= char and char <= 'z':
        print("입력한 문자 {}는 소문자입니다.".format(char))
    else:
        print("영문자가 아니므로 재입력하세요!")



def recul(x):
    if x == 1:
        return 1
    else:
        return (x * recul(x - 1))

num = int(input("숫자:"))
print("팩토리얼 값:", recul(num))'''



def power(a,b):
    if b == 1:
        return a
    else :
        return a * power(a, b - 1)

def powerNum(a, b):
    print("{}**{}={}".format(a, b, power(a,b)))

powerNum(2, 4)



def fibonacci(n):
    flist = [0, 1]
    if n == 0:
        flist.clear()
        return flist
    if n == 1:
        flist.pop()
        return flist
    elif n == 2:
        return flist
    
    else:
        for i in range(2, n):
            flist.append(flist[i - 1] + flist[i - 2])
        return flist

'''n = int(input("숫자를 입력하세요:"))
print(fibonacci(n))'''



'''try:
    num = int(input("정수 입력:"))
    n = int(input("나눌 수:"))
    if num % n == 0:
        print("짝수 입니다.")
    else:
        print("홀수 입니다.") 
except:
    print("오류 발생")'''

'''try:
    num1 = int(input("숫자1:"))
    num2 = int(input("숫자2:"))
    n = num1 / num2
    print("{} / {} = {}".format(num1, num2, n))
except ZeroDivisionError:
    print("숫자는 0으로 나눌 수 없습니다!")


numlist = [15, 12, 7, 14, 24]
try:
    i = int(input("리스트 항목 인덱스 위치를 입력하세요:"))
    nb = int(input("나눌 숫자를 입력하세요:"))
    print(f"{numlist[i]}/{nb} = {numlist[i] // nb}")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱스 오류!")
else:
    print("else 처리문입니다.") #정상적 경우면 출력
finally:
    print("finally는 항상 처리되는 문입니다.") # 정상 비정상 모두 출력'''



'''listStr=["python","programming","seoul","korea","university"]
i = int(input("문자열 인덱스를 입력하세요:"))
try:
    print(f"{listStr[i]}....{len(listStr[i])}")
except IndexError:
    print("찾고자 하는 인덱스가 없습니다.")'''


'''f = open("C:\\python_work\\sample.txt", "r", encoding="utf-8")
a = f.read()
print(a)
f.close()

f = open("C:\\python_work\\sample.txt", "r", encoding="utf-8")
line=f.readline()
print(line)
line=f.readline()
print(line)
f.close()'''

f = open("C:\\python_work\\sample.txt", "r", encoding="utf-8")
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()


fw = open("C:\\python_work\\group.txt", "w", encoding="UTF-8")
fw.write("송미자 산업공학과 010-1111-1234\n")
fw.write("이명섭 스페인어과 010-2222-1234\n")
fw.write("아이키 실용무용과 010-3333-1234\n")
fw.write("박태호 영문학과 010-4444-1234\n")
fw.write("아이유 실용음악과 010-555-1234\n")
fw.close()


file = open("C:\\python_work\\program.txt", "w", encoding="UTF-8")
language = ["python\n", "c\n", "java\n", "sql\n", "r\n", "javascript\n"]
file.writelines(language)
file.close()


'''n = int(input("원하는 구구단:"))
newfile1 = open("C:\\python_work\\multi.txt", "w", encoding="UTF-8")
for i in range(1, 10, 1):
    newfile1.write("{}*{}={}\n".format(n, i, n * i))
newfile1.close()

n = int(input("원하는 구구단:"))
newfile2 = open("C:\\python_work\\multi.txt", "a", encoding="UTF-8")
for i in range (1, 10, 1):
    newfile2.write("{}*{}={}\n".format(n, i, n * i))
newfile2.close()'''



readflower = open("C:\\python_work\\flower.txt", "r", encoding="UTF-8")
flowerlist = readflower.readlines()
newlist = []
count = len(flowerlist)

for i in range(count):
    newlist.append(flowerlist[i].upper())

writeflower = open("C:\\python_work\\flower.txt", "w", encoding="UTF-8")
writeflower.writelines(newlist)
writeflower.close() #sibal.. 그지같은 문제


'''
test = open("C:\\python_work\\test.txt", "r", encoding="UTF-8")
testlist = test.readlines()
result = 0
cnt = 0
for i in testlist:
    i = i.split("\n")
    i = int(i[0])
    result += i
    cnt += 1
print(f"합계:{result}")
print("평균:{}".format(result / cnt)) #sibal......못해먹겠네'''



aniprint = open("C:\\python_work\\aniprint.txt", "w", encoding="UTF-8")
animal=['deer', 'bear', 'lion', 'tiger', 'donkey']
for i in animal:
    aniprint.write(i)
    strlen = "\t"* 2 + str(len(i)) + "\n"
    aniprint.write(strlen)
aniprint.close()



#풀이1
weather = open("C:\\python_work\\weather.txt", "r", encoding="UTF-8")
for k in range(6):
    i, j, m = map(float, weather.readline().split())
    avr = (j + m) / 2
    print(f"{int(i)}월 평균 기온은 {avr:0.2f}도입니다.")

#풀이2
w = open("C:\\python_work\\weather.txt", "r", encoding="UTF-8")
wlist = w.readlines()
for i in wlist:
    i = i.split("\n")
    j, k, m = map(float, i[0].split( ))
    avr = (k + m) / 2
    print(f"{int(j)}월 평균 기온은 {avr:0.2f}도입니다.")




import pandas as pd

#Series로 프레임만들기
country = pd.Series(["KOREA","JAPAN","USA","CANADA","FRANCE"])
print(country)

city1 = pd.Series(["SEOUL","TOKYO","WASHINGTON","OTAWA","PARIS"],index=["KOREA","JAPAN",
"USA","CANADA","FRANCE"])
print(city1)

print('\n\n')


# .to_frame()으로 Dataframe형식으로 변환
city2 = city1.to_frame()
print(city2)

print('\n\n')

# .columns = [name] 로 열 이름 변경
city2.columns = ["CAPITAL"]
print(city2)

print('\n\n')


df = pd.DataFrame()
print(df)

print('\n\n')


# list -> dataframe
people = [["최성호",22],["박철수",21],["이민호",23],["성시경",24],["전지현",27]]
peopledf = pd.DataFrame(people, columns=["name", "age"])
print(peopledf)


print('\n\n')


# dict -> dataframe
fruit = {"fruit":["apple","banana","cherry","durian","mango"],"cnt":[5,11,15,22,3]}
fruitdf = pd.DataFrame(fruit)
print(fruitdf)

print('\n\n')

# add
fruitdf["가격"] = [1000,500,1200,2000,1500]
print(fruitdf)

print('\n\n')

# add + calculate
fruitdf["판매대금"] = fruitdf["가격"] * fruitdf["cnt"]
print(fruitdf)

print('\n\n')

fruitdf["sale(%)"] = 0.2
print(fruitdf)

print('\n\n')

fruitdf["sale가격"] = fruitdf["판매대금"] * (1 - fruitdf["sale(%)"])
print(fruitdf)

print('\n\n')


# delete by drop()
# axis = 0 : 행 
# axis = 1 : 열

fruitdf = fruitdf.drop(["sale(%)"], axis=1)
print(fruitdf)

# info about column
print(fruitdf.describe())

print('\n\n')

print(fruitdf.count())

print('\n\n')

print(fruitdf.mean()) 

print('\n\n')

print(fruitdf.std()) 

print('\n\n')

print(fruitdf.var())

print('\n\n')

print(fruitdf.max())

print('\n\n')

print(fruitdf.min())

print('\n\n')

print(fruitdf.mode())

print('\n\n')

print(fruitdf.median())

print('\n\n')




sale1 = pd.read_csv("C:\\python_work\\sale1.csv")
print(sale1)

sale2 = pd.read_csv("C:\\python_work\\sale2.csv")
print(sale2)

gradecsv = pd.read_csv("C:\\python_work\\grade.csv")
print(gradecsv)

salecombine = pd.concat([sale1, sale2])
print(salecombine)


print(salecombine.columns)

print('\n\n')

print(salecombine.index)

print('\n\n')

print(salecombine["판매수량"])

print('\n\n')

print(salecombine[["판매수량", "판매금액"]])

print('\n\n')

salecombine["정가"] = salecombine["판매금액"] 
salecombine["판매금액"] = 0
print(salecombine)

print('\n\n')

salecombine["판매금액"] = salecombine["판매수량"] * salecombine["정가"]
print(salecombine)

print('\n\n')

print(salecombine.head())

print('\n\n')

print(salecombine.tail())


bookdf=salecombine.rename(columns={"제품명" : "도서명"})
print(bookdf)

print(bookdf.dtypes)


import numpy as np

num1 = [10,20,30,40,50] 
num2 = [60,70,80,90,100] 

arr1=np.array(num1) # make array 
print(arr1)
arr2=np.array(num2)
print(arr1)


n1=np.zeros((2,2)) # 0 초기화 
print(n1)
n2=np.ones((2,3)) # 1 초기화
print(n2)
n3=np.full((2,3), 9) # 지정값으로 초기화
print(n3)
n4=np.eye(3) # 2차원 대각선 방향 1, 나머지 0 할당
print(n4)
arr=np.array(range(1,26,1)).reshape(5,5) # 5x5 2차원 배열
print(arr)

arr_2d=[[1,2,3],[4,5,6]]
print(np.shape(arr_2d)) # 몇 행 몇 열


a1=np.array([1,2,3])
a2=np.array([4,5,6])
a3=np.add(a1,a2) 
print(a3)

print("\n\n")

a4=np.subtract(a1,a2) #subtract()함수로 뺄셈
a5=np.multiply
a6=np.divide(a1,a2)

print(a4)
print("\n\n")
print(a5)
print("\n\n")
print(a6)
print("\n\n")

grade=[90,80,100,70,65]
print("max:",np.max(grade))
print("min:",np.min(grade))

print("max index:", np.argmax(grade))
print("min index:", np.argmin(grade))

print("\n\n")

s=np.std(grade)
print("std:{:.2f}".format(s))
print("var:",np.var(grade))

print("\n\n")

grade=[2,4,6,9,16]
print("누적합", np.sqrt(grade))

print("\n\n")

name=["홍길동","강감찬","유관순","김유신","이순신","유관순"] # 중복
n=np.array(name)
print(np.unique(n)) # 중복 제외 오름차순 


num=[5,10,3,3,5,10,8,9,7,6,1,3]
print(np.unique(num))

print("\n\n")


########### 13주차 추가 ############

import pandas as pd
grade1 = pd.read_csv("C:\\python_work\\grade_1.CSV")
grade2 = pd.read_csv("C:\\python_work\\grade_1.CSV")
print(grade1)
print("\n\n")
print(grade2)
gradecombine = pd.concat([grade1, grade2])
print(gradecombine)

print(gradecombine.columns)
print(gradecombine.index)
gradecombine["tot"] = gradecombine["eng"] + gradecombine["math"] + gradecombine["com"]
print(gradecombine)

gradecombine["avg"] = gradecombine["tot"] / 3
print(gradecombine)

pd.options.display.float_format='{:.2f}'.format
print(gradecombine.head(avg))