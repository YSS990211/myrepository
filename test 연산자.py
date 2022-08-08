import numbers


print(2**3) #**두번은 제곱이됨 2의3승 2^3=8
print(5%3) # %는 나누기한 값의 나머지 / 나머지 구하기 / 5%3=2
print(5%2) # 1
print(5//3) # // 두번은 몫구하기 , ex) 10나누기3은=3 

print(3 == 3) # ==는 앞의 숫자와 같은지 체크하는용도, Ture
print(4 == 2) # False
print(5*2==10) # Ture

print(1 != 3) #!=을 하면 앞뒤의 숫자가 같지않다를 의미 ==의 반대, Ture
print(not(2!=3)) # not는 반대의 결과를 출력하기 떄문에 , False

print((3>0)and(3<5)) # and(&)조건은 둘다 맞아야 결과가 참으로나옴 하나라도 아니면 안됨
print((3>0)or(3>5)) # or(| >> 엔터위에꺼)  조건은 하나라도 맞으면 참

print(5>4>3) # 연속되는 숫자도 가능

#수식
print(2+2+2+4*4)
number=5*5*10
print(number+5)
number = number + 10 # 260
print(number)
number += 10 # 위에꺼랑 같은 수식이고 저렇게 간단히 가능 , 270
print(number)
number *= 1 # 270
print(number)
number /= 10 # 27
print(number)

number %= 1 # 2로나눈 나머지값 , 1
print(number)
number //= 10 # 2을 10으로 나눈 몫 , 0
print(number)