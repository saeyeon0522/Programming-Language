############## 1 차 시 ##############



count = 0

for i in range(5) :
    num = int(input("숫자를 입력하세요 : "))
    if num % 2 == 0:
        print(f"{num}은(는) 짝수입니다.")
    else:
        print(f"{num}은(는) 홀수입니다.")
        count += 1
print(f"홀수 개수 : {count}")




nb = 5
for i in range(5) :
    print(f"{nb}")
    nb -= 1




############### 2 차 시 ###############


  
sum = 0
num_list = [1, 3, 5, 7, 9]
for i in num_list :
    sum += i
print(f"{sum}")




for i in num_list[::-1] :   # 뒤에서부터 출력
    print(f"{i}")


for i in reversed(num_list) :
    print(f"{i}")


num_list.reverse()
for i in num_list :
    print(f"{i}")




zoo = ["rabbit", "goat", "tiger", "lion", "giraffe", "zebra"]

for i in reversed(zoo) :
    print(f"{i} ", end = '')


for i in reversed(zoo) :
    wordlen = len(i)
    print(f"{i} : {wordlen}")


zoo = ["rabbit", "goat", "tiger", "lion", "giraffe", "zebra"]

animal = input("동물을 입력하세요 : ")


if animal in zoo:
    for i in zoo :
        print(f"{animal}(은)는 동물원에 있습니다.")
        break
else :
    print(f"{animal}(은)는 동물원에 없습니다.")




############### 3 차 시 ################



i = 1
while i < 6 :
    str_num = str(i)
    i += 1
    print(f"Python Program {str_num}번 출력")




num = int(input("숫자를 입력하세요 : "))
i = 1
while i < 10 :
    print("{0} * {1} = {2}".format(str(num), str(i), str(num * i)))
    i += 1





while 1 :
    num = int(input("숫자 입력 : "))
    if num % 2 == 1 :
        print(f"{num}은 홀수입니다.")
        break
    else :
        print(f"{num}은 짝수입니다.")
        continue
        




animal = ["dog", "duck", "pony", "donkey", "giraffe", "elephant", "cat"]

i = 0
count = len(animal)
while i < count :
    print(animal[i])
    i += 1
    





















































