# num = int(input())
# if num >=1 and num <=9 :
#     print('한 자리 숫자입니다.')
# elif num >=10 and num <=99:
#     print('두 자리 숫자입니다.')
# else : 
#     print('세 자리 숫자입니다.')

score = int(input())
if score == 0 :
    print('F')
elif score >=88 :
    print('A+')
elif score >=77 :
    print('A0')
else :
    print('B+')