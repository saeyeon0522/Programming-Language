f=open("C:\\python_work\\weather.txt", "r", encoding="utf-8")

try:
    for i in range(6):
        m, l, h = map(float, f.readline().split())
        avr = (l+h)/2
        print(f"{i+1}월의 평균 기온은 {avr:0.2f}도 입니다.")
except:
    print("Error")
    exit(1)
    
f.close()
