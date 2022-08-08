#필요한 정보만 잘라서 사용하는게 슬라이싱

from cgi import print_form


juminnumber = '901211-1234567' # 컴퓨터는 맨 앞자리숫자가 1이 아닌 0부터 시작함

print('성별 : ' + juminnumber[6]) # 필요한 값만 가져오기위해 대괄호 사용
print('년생 : ' + juminnumber[0:2]) # :(콜로니) 사용시 0부터 2직전까지값 (0,1)
print('월 : ' + juminnumber[2:4]) 
print('일 : ' + juminnumber[4:6]) 

print('생년월일 : ' + juminnumber[:6]) #0을 굳이 쓰지않아도 처음부터 6직전까지 a의값까지출력
print('뒷자리 : ' + juminnumber[7:14]) 
print('뒷자리 : ' + juminnumber[7:]) #뒷자리를 적지않으면 끝까지 값을 출력

print('뒷자리 (뒤에서부터)' + juminnumber[-7:]) #뒤에서부터 시작하려면 -1부터 시작, 맨뒤 7번째부터 끝까지