flowerList = ["sunflower", "rose", "lily", "cosmos", "tulip"]

flower = input("좋아하는 꽃 : ")
if flower in flowerList :
    length = len(flower)
    print(f"내가 좋아하는 꽃 {flower}이(가) 리스트에 있습니다.")
    print(f"{flower}의 길이는 {length} 글자입니다.")

if flower not in flowerList :
    print(f"내가 좋아하는 꽃 {flower}이(가) 리스트에 없습니다.")
