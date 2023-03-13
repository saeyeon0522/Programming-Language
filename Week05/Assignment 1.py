listcode = [1, 2, 3]
purpose= int(input("전력 사용 코드를 입력하세요 : "))
if purpose in listcode:
    usage = int(input("전력 사용량을 입력하세요 : "))
    if purpose == 1:
        cost = 910 + 88 * usage
    elif purpose == 2:
        cost = 1600 + 182 * usage
    else:
        cost = 7300 + 275 * usage
    print(f"용도:{purpose}, 사용량:{usage:0.2f}, 전기요금:{cost:0,.2f}(원)") 

    
