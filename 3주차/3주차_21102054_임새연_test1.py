name = input("이름을 입력하세요")
korean = int(input("국어 점수를 입력하세요"))
english = int(input("영어 점수를 입력하세요"))
math = int(input("수학 점수를 입력하세요"))
sum = korean + english + math
average = (korean + english + math) / 3
print("{0}군의 성적은 총점:{1}, 평균:{2:0,.2f}점 입니다.".format(name, sum, average))
