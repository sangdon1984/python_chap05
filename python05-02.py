# -*-coding:utf-8

print("==모듈==")
# 모듈
# 클래스, 함수, 변수 등을 미리 만들어 두고 필요할 때 가져다 사용할 수 있도록 모아 놓은 파일
# 실행하는 파일과 모듈이 같은 폴더에 존재해야함
# 모듈을 사용하는 이유는 유지보수가 편함
# 다른 사람과의 협업이 가능함
# 모듈 사용 시 사용법만 알고 있으면, 해당 모듈의 내부 구조를 몰라도 사용이 가능함

# 사용방법
# import 모듈명
# 모듈 사용 시 해당 모듈명과 클래스, 함수, 변수 등을 모듈명.멤버로 사용해야 함
# mod.sum()

# from 모듈명 import 모듈 함수
# 모듈 사용 시 해당 모듈의 클래스, 함수, 변수 등을 모듈명 없이 사용할 수 있음

# import mod1
# print("mod1 모듈의 sum 함수 사용 : {0}".format(mod1.sum(3,4)))

# print()
# print("mod1의 safe_sum 함수 사용 : {0}".format(mod1.safe_sum(3, 4)))
# print("mod1의 safe_sum 함수 사용 : {0}".format(mod1.safe_sum(1, "a")))

# from 절을 사용하여 mod1의 sum, safe_sum을 모두 불러와 사용하기 때문에 mod1을 붙여서 사용하면 오히려 오류가 발생함
from mod1 import sum, safe_sum
print("mod1 모듈의 sum 함수 사용 : {0}".format(sum(3,4)))

# 문제1) 사칙 연산을 위한 계산기 프로그램을 모듈을 활용한 방식으로 제작하세요
# 모듈명 : Cal
# 사칙연산 함수명 : plus, minus, multi, divide
# 각각 함수는 매개 변수를 2개씩 가지고 있음(first, second)
print()
print("==문제1==")
import Cal
print("Cal 모듈의 plus 함수 사용 : {0}".format(Cal.plus(3, 4)))
print("Cal 모듈의 minus 함수 사용 : {0}".format(Cal.minus(3, 4)))
print("Cal 모듈의 multi 함수 사용 : {0}".format(Cal.multi(3, 4)))
print("Cal 모듈의 divide 함수 사용 : {0}".format(Cal.divide(3, 4)))

# 클래스나 변수 등을 포함한 모듈
# 일반 함수가 들어있는 모듈과 동일함

# 사용방법
    # 클래스
    # 변수명 = 모듈명.클래스명()

    # 변수
    # 변수명 = 모듈명.변수명
print()
print("==모듈에 포함된 변수, 클래스, 함수 사용하기==")
import mod2

print(mod2.PI)
print(mod2.sum(mod2.PI, 4.4))

result = mod2.sum(3, 4)
print("mod2 모듈을 로드하여 sum함수 사용 : {0}".format(result))

# 문제2) 문제 1의 소스를 수정하여 클래스를 사용한 방식의 사칙연산 프로그램을 제작하세요
# 모듈명 : Cal2
# 클래스명 : Calculator
# 함수명 : plus, minus, multi, divide
# 각 함수는 2개의 매개변수를 가짐(first, second)

print()
print("==문제2==")
import Cal2

cal2 = Cal2.Calculator()

print("Cal2 모듈의 plus 함수 사용 : {0}".format(cal2.plus(3, 4)))
print("Cal2 모듈의 minus 함수 사용 : {0}".format(cal2.minus(3, 4)))
print("Cal2 모듈의 multi 함수 사용 : {0}".format(cal2.multi(3, 4)))
print("Cal2 모듈의 divide 함수 사용 : {0}".format(cal2.divide(3, 4)))

# 문제3) 위의 문제 2번에서 오버로딩을 사용하여 값이 매개 변수에 따라 다른 형태로 출력하는 클래스를 만들고 이를 사용하는 프로그램을 제작하세요
# 모듈명 : Cal3
# 기본 초기화 메서드 : setNumber
    # 매개변수가 총 3개
    # 멤버 변수 first, second 의 값을 초기화 함
# 메서드 이름 : plus, minus, multi, divide
    # 기존 그대로 만들고
    # 멤버 변수를 활용하여 값을 연산
# 메서드의 매개변수의 수에 따라 연산을 달리함 (*args)
    # 추가된 메서드 : totalCal
    # 1번째 매개변수 : self
    # 2번째 매개변수 args의 첫번째 : +, - , *, / (문자열로 받기)
    # 3번째부터 숫자를 입력받음
    # if문 이용해서 매개변수 길이에 따라 다르게 연산 ( 멤버 변수 범위 넘어서면 받은 값을 이용해 연산)
    # 입력받을 매개변수 수 총 5개까지
print()
print("==문제3==")
import Cal3
cal3 = Cal3.Calculator()
cal3.setNumber(50, 30)
print("Cal3 모듈의 plus 함수 사용 : {0}".format(cal3.plus()))
print("Cal3 모듈의 minus 함수 사용 : {0}".format(cal3.minus()))
print("Cal3 모듈의 multi 함수 사용 : {0}".format(cal3.multi()))
print("Cal3 모듈의 divide 함수 사용 : {0}".format(cal3.divide()))

print("Cal3 모듈의 totalCal 함수 {0}연산 매개변수{1}개 : {2}".format("+", 1, cal3.totalCal("+", 5)))
print("Cal3 모듈의 totalCal 함수 {0}연산 매개변수{1}개 : {2}".format("+", 2, cal3.totalCal("+", 4,5)))
print("Cal3 모듈의 totalCal 함수 {0}연산 매개변수{1}개 : {2}".format("+", 3, cal3.totalCal("+", 3,4,5)))
print("Cal3 모듈의 totalCal 함수 {0}연산 매개변수{1}개 : {2}".format("+", 4, cal3.totalCal("+", 2,3,4,5)))
print("Cal3 모듈의 totalCal 함수 {0}연산 매개변수{1}개 : {2}".format("+", 5, cal3.totalCal("+", 1,2,3,4,5)))
print("Cal3 모듈의 totalCal 함수 {0}연산 매개변수{1}개 : {2}".format("-", 5, cal3.totalCal("-", 1,2,3,4,5)))
print("Cal3 모듈의 totalCal 함수 {0}연산 매개변수{1}개 : {2}".format("*", 5, cal3.totalCal("*", 1,2,3,4,5)))
print("Cal3 모듈의 totalCal 함수 {0}연산 매개변수{1}개 : {2}".format("/", 5, cal3.totalCal("/", 1,2,3,4,5)))