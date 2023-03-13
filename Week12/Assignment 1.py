f = open("C:\\python_work\\animal.txt", "w", encoding="utf-8")
ani_list=[]
for i in range(5):
    ani = input("동물을 입력해주세요: ")
    f.write(ani)
    f.write("\n")
f.close()
    
    
