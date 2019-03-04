#-*-coding:utf-8

def sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a, b)
    return result

# 모듈의 테스트
# 제작한 모듈이 정상적으로 동작하는지 확인하는 구문
# 현재 실행한 파일이 실제 실행한 파일인지 아니면 import된 파일인지를 확인하는 구문

# 파이썬의 실행 시작 지점
# python 파이썬 코드 파일을 하면 자동으로 main문이 생성됨
# if __name__ == "__main__":

# public static void main(args[]){
# }

if __name__=="__main__":
    print(safe_sum("a", 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))