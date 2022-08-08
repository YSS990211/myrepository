from random import * # 랜덤 라이브러리를 사용한다는뜻
print(random()) #랜덤수를 출력함, 0.0~1.0 미만의 값 생성
print(random()*10) # 0.0~1.0 미만의 값에서 10을 곱함
print(int(random()*10)) #int 입력시 정수만 출력시켜줌 
print(int(random()*10)) #int 입력시 정수만 출력시켜줌 
print(int(random()*10)+1) # 1~10 이하의 정수 임의값 출력(기존 0~10미만인데 1 더해서)

#로또번호 뽑기
print(int(random()*45)+1) # 1~45 이하의 임의값출력 
print(int(random()*45)+1) 
print(int(random()*45)+1) 
print(int(random()*45)+1) 
print(int(random()*45)+1) 
print(int(random()*45)+1)

print(randrange(1, 46)) #randrange=범위 랜덤값 , 1~46미만의 임의값생성
print(randint(1, 45)) #randint는 randrange와 달리 a,d값을 포함하여 임의값 생성 1~45

# 퀴즈
'''매월 스터디 그룹의 모임을 하는데 날짜는 최대 28일까지이고
매월 1~3일은 정비날로 만나지 않는다 랜덤한 날짜를 출력하라'''

print('스터디 모임은 매월 ' , randint(4,28) , '일로 경정') # 정수출력시 ,, or str
print('스터디 모임은 매월 ' + str(randint(4,28)) + '일로 경정')