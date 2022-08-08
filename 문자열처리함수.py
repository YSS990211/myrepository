from operator import index
from platform import python_branch
from turtle import home


ㅎㅎ = 'Python is Awesome'
print(ㅎㅎ.lower()) # lower 입력시 문자열함수가 소문자로 출력
print(ㅎㅎ.upper()) # upper 입력시 문자열함수가 대문자로 출력
print(ㅎㅎ[0].isupper()) # ㅎㅎ라는 함수의 0번째 단어가 대문자가 맞는지 체크
print(len(ㅎㅎ)) # ㅎㅎ라는 함수의 글자수 세주는 함수
print(ㅎㅎ.replace('Python', 'r')) # ㅎㅎ라는 함수에서 '앞'의 글자를 찾아 '뒤' 문장으로 변경출력

인덱스 = ㅎㅎ.index('e') # 인덱스는 원하는 글자가 몇번째에 있는지 알려줌 대신 맨앞부터 1개만 찾음
print(인덱스)
인덱스 = ㅎㅎ.index('e' , 인덱스 + 1) # 위에서 찾은 번호 다음 위치를 알려줌
print(인덱스)

print(ㅎㅎ.find('ee')) # find는 index와 비슷하지만 다른게 인덱스는 없다면 오류가 나고 파인드는 -1이 나옴
print(ㅎㅎ.count('e')) # count 는 입력한 글자가 몇번이나 출력됐는지 출력 없으면 0

