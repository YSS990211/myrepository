#리스트 []
#지하철 칸별로
열차1 = 10
열차2 = 20
열차3 = 30

# 열차 = [열차1,열차2,열차3]
# print(열차)

열차 = ['메시','호날두','네이마르']
print(열차)

#메시가 탄 열차는 몇번째인가
print(열차.index('메시')+1) # 0 부터 시작하기 때문에 보기 쉽게 1을 더함

열차.append('음바페') # append 입력값을 함수 뒤에 붙힌다
print(열차)

열차.insert(1,'부폰') # 입력해둔 함수 값 사이에 새로운 값을 추가한다, 입력 순서 인덱스를 넣으면 기존자리 값부터 밀려남 
print(열차)

print(열차.pop()) # pop는 뒤에서 하나의 값을 빼냄
print(열차)

숫자 = [3,4,6,5,2,1]
숫자.sort() # sort 는 숫자 정렬을 해준다
print(숫자)

숫자.reverse() # reverse 뒤집기
print(숫자)

숫자.clear() # 리스트 지우기
print(숫자)

#리스트 확장
ㅇㅇ=['ㅇ','ㄹ', True]
number=[1,2,3,False]
ㅇㅇ.extend(number) # extned 를 통해 리스트를 합침
print(ㅇㅇ)