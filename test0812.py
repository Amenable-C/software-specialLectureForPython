score1 = int(input("영어 점수 입력 : "))
score2 = int(input("수학 점수 입력 : "))
if((score1 + score2) >= 100):
    if((score1 >= 40) and (score2 >= 40)):
        print("합격입니다!")
    elif((score1 < 40) and (score2 >= 40)):
        print("영어 과락 불합격")
    else:
        print("수학 과락 불합격")
else:
    print("총점 미달 불합격")