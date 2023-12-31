
# < 튜플 >
# 파이썬의 튜플(Tuple)은 불변(immutable)하고 순차적인 데이터 구조로,
# 여러 값들을 저장하고 관리
# 변경할 수 없는 특성 때문에 리스트보다 메모리 효율이 높음
# 데이터가 변경될 수 없는 경우에 적합한 데이터 구조
# 튜플은 소괄호( )를 사용하여 표현
# 튜플의 요소들은 쉼표, 로 구분

# 튜플 생성 tuple()
empty_tuple = ()

# 단일 요소 튜플 생성 시 쉼표 필요
single_item_tuple = (1,)

# 정수형 튜플 생성
numbers = (1, 2, 3, 4, 5)

# 문자형 튜플 생성
fruits = ("apple", "banana", "cherry")

# 다양한 자료형이 포함된 튜플 생성
mixed_tuple = (1, "apple", 3.14)

# 튜플 인덱싱(Indexing)
varsfruits = ("apple", "banana", "cherry")
print(fruits[0])

# 튜플 슬라이싱(Slicing)
numbers = (1,2,3,4,5)
print(numbers[1:4])

# 튜플 길이 확인
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# 튜플 요소의 개수 세기
numbers = (1, 2, 3, 2, 1, 3, 1, 1, 2, 3)
print(numbers.count(1))
