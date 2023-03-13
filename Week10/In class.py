################# 3 차 시 #################

num = ()
broad = ("sbs", "kbs", "mbc", "ebs")
mix = (10, "sbs", 120.15, (1, 2, 3))

strlist = ['a', 'b', 'c']
strtup = tuple(strlist)
print(type(strtup))


nb = (1)    # 정수로 인식
print(type(nb))

nb = (1,)   # 튜플로 인식
print(type(nb))


flower = ("장미", "수국", "진달래", "개나리", "튤립")
flowerlist = list(flower)
flowerlist.append("민들레")
print(flowerlist)

flowerlist[0] = "배꽃"
print(flowerlist)

flower = tuple(flowerlist)
print(flower)



num = (11, 12, 13, 14, 15)
res = 0
for i in  num:
    res += i
    print(i)
print(f"합계={res}")




################# 2 차 시 #################

num = [12, 15, 8, 4, 9]

newnum = sorted(num)
print(f"num : {num}")
print(f"new num : {newnum}")

newnum = sorted(num, reverse=True)
print(f"new num : {newnum}")

lang = ["java", "c", "python", "sql", "basic"]
newlang = sorted(lang, key = lambda x:x[0], reverse = False)
print(newlang)
newlang = sorted(lang, key = lambda x:x[0], reverse = True)
print(newlang)



num = (20, 30, 15, 31, 23)
newnum = sorted(num, reverse=False)
res = 0

for i in newnum:
    print(i)
    res += i
print(f"합계:{res}")




num = [[10, 20], [30, 40], [10, 100]]
for i, j in num:
    print(i, j)

for i in num:
    for j in i:
        print(j, end = " ")
    print()



book = [("java", 15000), ("python", 25000), ("c", 18000), ("java", 19000)]
newbook = sorted(book, key=lambda x:x[1], reverse=True)
for i, j in newbook:
    print("{}\t{}".format(i, j))
for i, j in newbook:    
    print(f"{i}\t{j}")



student = [("인터넷", "이정재", "010-123-1234", 90), 
            ("미디어","전지현","010-123-4560", 80),
            ("정통과","송혜교","010-123-2244", 100),
            ("컴퓨터","김소현","010-123-3355", 85),
            ("국문과","강하늘","010-123-7890", 95)]
newstudent = sorted(student, key = lambda x:x[3], reverse=True)
print("학 과\t이 름\t연락처\t\t점수")
for i, j, m, n in newstudent:
    print(f"{i}\t{j}\t{m}\t{n}")



grade= {}
grade["아이키"] = 90
grade["박보검"] = 95
grade["유아인"] = 80
grade["전지현"] = 100
grade["송중기"] = 90
print(grade)
print(grade["전지현"])

grade["전지현"] = 85
print(grade["전지현"])

print(grade.keys())
print(grade.values())
print(grade.items())


for i in grade.keys():
    print(i)

for i in grade.keys():
    print(i, grade[i])




name = ["이순신","강감찬","홍길동"]
score = [80, 90, 100]
grade = dict(zip(name, score))
print(grade)


grade = {'아이키': 90, '박보검': 95, '유아인': 85, '전지현': 100, '송중기': 90}
res = 0
for i in grade.values():
    res += i
for i in grade.keys():
    print(i, grade[i])
print("==========")
print(f"합계:{res}")



movie=[("오징어게임",50.45), ("이터널스",35.46),("그레비티",9.8), ("노타임투다이",52.5),
("스파이더맨",15.47)]
newmovie = sorted(movie, key= lambda x:x[1], reverse=True)
moviedict = dict(newmovie)
num = 1
print("영화제목\t예매율\t순위")
print("========\t======\t====")
for i in moviedict.keys():
    print(i, moviedict[i], num, sep="\t")
    print()
    num += 1


