#-*-coding:utf-8

class Calculator:
    def setNumber(self, first, second):
        self.first = first # 멤버변수 선언
        self.second = second
    def plus(self):
        return self.first + self.second
    def minus(self):
        return self.first - self.second
    def multi(self):
        return self.first * self.second
    def divide(self):
        return self.first / self.second
    def totalCal(self, choice, *args):
        if choice == "+":
            result = self.first + self.second
            for i in args:
                result = result + i
        elif choice == "-":
            result = self.first - self.second
            for i in args:
                result = result - i
        elif choice == "*":
            result = self.first * self.second
            for i in args:
                result = result * i
        elif choice == "/":
            result = self.first / self.second
            for i in args:
                result = result / i
        else:
            print("잘못된 입력입니다.")
        return result