
# 재귀 함수  -  (강의자료 exam 14 ~ 15.py)
# - 자기 자신을 호출하는 함수
# - 분할정복에 주로 사용 -> 자료 구조를 구현할 때 재귀함수를 많이 활용됩
# - 원형: def recu():
#            print("recursive")
#            recu()


# Lambda 함수
# - 람다 함수는 파이썬에서 익명 함수를 생성하는 방법
# - 간결한 문법으로 이름이 없는 간단한 함수를 생성하는데 사용 => 한 줄짜리 함수 정의할 때 사용
# - 원형: lambda 매개변수(입력으로 사용되는 인자들): 기능        
#     ex) lambda x,y: x + y     => 더하기 함수 
#
# 람다 함수 구현 예시
# - 람다 함수는 변수로 대입할 수 있음
# - 함수 호출 시 매개변수로 전달 가능(함수형 프로그래밍 개념)
# ex) add = lambda x,y: x + y
#     result = add(3,5)
#     print(result)
