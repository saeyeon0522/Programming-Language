char = input("알파벳을 입력하시오:")
sign = 1 if 'A' <= char <= 'Z' else 0
if sign == 1:
    print(f"당신이 입력한 문자 {char}은 대문자입니다.")
else:
    print(f"당신이 입력한 문자 {char}은 소문자입니다.")
