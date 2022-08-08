from cgi import print_environ
from datetime import date

# 주석 팁 ''' 이렇게 3개입력 하고 문장 쓰고 다시 3개 쓰면 주석처리됨
# 여러문장 주석할땐 문장 드래그해서 ctrl + / 하면 전체적으로 주석이됨
''' 예시를 들어보면
이렇게 주석이 된다'''

#참 / 거짓 (boolean)
print(5>10)
print(not 5>10)
print(not True)
# not 입력시 반대의 결과가 나온다

# 변수
name ='봄이'
age = 24
hobby = '산책'
job = '여자친구'
is_adult = age <= 23 #입력값보다 나이설정변수(age)가 크거나 같다면 True 아니라면 False
print('내가아는 ' + name + '는 '+ hobby +'을 좋아해')
print('' + name + '는 ' , age ,'살 '+ job +'야')
#의문에 답을 얻고싶다면 (str)입력 , 정수를 넣을시 str(정수형을 문자형으로 바꿔줌) 추가해야함(안그러면 오류가생김)
# , 입력시 띄어쓰기됨 그대신 str 안써도됨
print('' + name + '는 올해로 24살이 맞을까?' ,is_adult)
name = '최봄이' # 변수를 특정 구간에 다시 입력시 입력 구간다음부터 출력됨
print('그 사람의 전체적인 이름은 '+ name +'야')
