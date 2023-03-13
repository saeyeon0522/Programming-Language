gradeList1=[(1,"BTS",80), (2,"HKD",90),(3,"KCH",95), (4,"HMH",70), (5,"YDH",85)]

print("번호\t이름\t성적\t순위")
print("===\t===\t===\t===")

newlist = sorted(gradeList1, key = lambda x : x[2], reverse = True)

num = 1
for i, j, k in newlist:
    print(f"{i}\t{j}\t{k}\t{num}")
    num += 1
            
