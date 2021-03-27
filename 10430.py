a,b,c = map(int,input().split())
print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print((a%c * b%c)%c)

#map : 여러개의 데이터를 한번에 다른 형태로 바꿔준다
#예를들면 저번문제에서는 a = int(a)라고 썻는데
#지금은 그런게 없는것을 볼수있다.

#map의 특징은 원본 리스트를 변경하지 않고 새 리스트를 생성한다.
#map 타입으로 결과를 리턴하기 때문에 리스트나 튜플 등으로 변환한다.