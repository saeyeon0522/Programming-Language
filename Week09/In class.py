############### 1 차 시 ###################

num = [10, 15, 20, 25, 30]
res = 0
for i in num:
    res += i
print(f"리스트 합계={res}")



num = [1, 2, 3, 3, 4, 5, 6, 7, 2, 3, 8, 9, 10]
count = 0
for i in num:
    if i == 3:
        count += 1
print(f"3의개수={count}개")



num = [15, 23, 18, 47, 23]
even = 0
odd = 0
for i in num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"홀수 개수 = {odd}개\n짝수 개수 = {even}개")




################## 2 차 시 ###################



numA = []
numA.append(1)
numA.append(2)
print(numA)

numB = [10, 20, 30]
numA.extend(numB)
print(numA)



alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
alpha[:]    #처음 ~ 끝
alpha[3:]   #시작 위치 ~ 끝
alpha[:4]   #처음 ~ 끝 - 1 위치
alpha[2:4]  #시작 위치 ~ 끝 - 1 위치



print(alpha[4])
print(alpha[-5])


print(alpha[2:6])
print(alpha[-6:-2])



strlist = ['K', 'C', 't', 'E', 'b', 'a', 'M']
strlist.sort()
print(strlist)



num = [15, 11, 9, 6, 3]
num.sort(reverse=True)
print(num)


num.sort(reverse=False)
print(num)


num = [11, 23, 5, 6, 15, 9, 8]
print(f"정렬 전: {num}")
num.sort(reverse=True)
print(f"정렬 후: {num}")

