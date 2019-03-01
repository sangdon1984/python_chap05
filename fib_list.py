print("=== insert 이용 반복문 만들기 전 테스트 ===")
a=[0, 1]
print(len(a)) # len(a) = 2
a.insert(len(a), a[len(a)-2] + a[len(a)-1])
print(a)
print(len(a)) # len(a) = 3
a.insert(len(a), a[len(a)-2] + a[len(a)-1])
print(a)

print("=== insert 이용 반복문 ===")
b = [0, 1]
n = 20
while len(b) < n:
    b.insert(len(b), b[len(b)-2] + b[len(b)-1])
print(b)

print("=== append 이용 ===")
c = [0, 1]
n = 20
while len(c) < n:
    c.append(c[len(c)-2] + c[len(c)-1])
print(c)

print("=== 사용자 입력 append 이용 반복문===")
d = [0, 1]
n = input("n : ")
n = int(n)
while len(d) < n:
    d.append(d[len(d)-2] + d[len(d)-1])
print(d)