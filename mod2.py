#-*-coding:utf-8

# 클래스나 변수 등을 포함한 모듈

PI = 3.141592
class Math:
    def solv(self, r):
        return PI * (r ** 2)
    
def sum(a, b):
    return a + b

# if __name__=="__main__": 를 이용하여 정상적으로 작동하는지 확인
if __name__=="__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))