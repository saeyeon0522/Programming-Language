animal = ['병아리', '오리', '강아지', '거위', '송아지']
leg = [2, 2, 4, 2, 4]
ani_list = [("병아리", 2), ("오리", 2), ("강아지", 4), ("거위", 2), ("송아지", 4)]

newlist = sorted(ani_list, key = lambda x:x[1], reverse = True)

ani_dict = dict(newlist)

res = 0
for i, j in ani_dict.items():
    print(f"{i}\t{j}")
    res += j

print("-----------")
print(f"동물 다리 합계:{res}")
