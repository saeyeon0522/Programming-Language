money=int(input("용돈을 입력하세요"))
left= money - 3550
div500 = left // 500
mod = left % 500
div100 = mod // 100
mod = left % 100
div10 = mod // 50
print(f"거스름돈 : {left}원")
print(f"500원 짜리 거스름돈 : {div500}개")
print(f"100원 짜리 거스름돈 : {div100}개")
print(f"10원 짜리 거스름돈 : {div10}개")

