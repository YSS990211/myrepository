from ctypes import get_last_error
from operator import index
from re import A
from turtle import color


print('a'+'b') # +는 붙여서 출력 , 는 띄워서 출력
print('c','d')

#방법 1 %d %s %c 를 이용 (별로 좋지않은거같음)
print('나는 %d살 입니다.'% 20+'여자친구도 %d살입니다' % 20) # %에 숫자를 지정해줄수있고 d는 정수를 뜻함
print('나는 %s을 좋아해' %'코딩') # s는 언어
print('사탕은 영어로 %c로 시작해' % 'C') # c는 캐릭터라는 뜻으로 한가지 글자만 출력

#방법 2 .format을 이용
print('저의꿈은 {0}입니다'.format('데이터분석가','빅테이터전문가'))
print('나이는{age[0]}, 취미는{ppt[1]}, 너의 취미는{ppt[0]}'.format(age = ('20','30'), ppt=('볼링','라이딩')))
# .format은 대괄호를 이용하여 대괄호 안에 설정한 내용 및 변수를 넣을 수 있다.

# 변수를 미리 설정한 후 f를 이용하여 문장 출력
age = '25'
color = '검정'
print('나는',age+'살이며',color+'색을 좋아해요')
print(f'나는 {age}이며 {color}색을 좋아해') # 사용시 대괄호를 이용하여 설정한 변수값을 출력할수있음 


# 탈출문자
print('아 오늘도 역시 퇴사를 \n 하고 코딩 공부를 하고싶다') # \n은 줄바꿈
print(f'''아 오늘도 역시 
집에 가고싶었다
내나이{age}살..''') # ' 혹은 " 3개를 입력하고 줄바꿈을 직접해도된다

# 따운표를 다르게 입력하지 않아도 출력하는법 Ex) 나는'신윤수'입니다 그냥 입력시 나는, 입니다만 범위안에들어 오류발생
print("나는 '신윤수'입니다.") # "를 먼저써도되지만 불편함
print('나는\'신윤수\'입니다')

# \역슬래쉬 하나만 입력시 오류발생 ex) 경로출력시 문제가생김
print('D:\\Desktop\\python>') # \\를 두번 입력하면 \ 하나로 출력

# \r = 커서를 맨앞으로 이동 ('나는 바보다\r너는')입력시 너는 바보다 출력
# \r 뒤에 너는 이라는 단어가 커서 맨앞으로가면 나는 자리에 붙여넣기가 되는거
print('나는야 멍청이\r너는너는')

#문제
# 사이트별 암호 만들기
# 예) http://naver.com
# 규칙 1 http:// 제외 > naver.com
# 규칙 2 처음 만나는 점(.) 이후 부분 제외 > naver
# 규칙 3 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성 > nav51!

# fullrink1 = 'http://naver.com' # 예
fullrink1 = 'http://kakao.com' # 예
fullrink2 = fullrink1.replace('http://','') #규칙1
rink = fullrink2[0:5] # 규칙2
비밀번호 = rink[0:3] + str(len(rink)) + str(rink.count('e')) + '!'
print('{0} 의 비밀번호는 {1} 입니다.'.format(fullrink1, 비밀번호)) 