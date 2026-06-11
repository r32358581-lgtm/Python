count = int(input("입력할 값의 개수: "))

values = []

for i in range(count):
    num = int(input())
    values.append(num)

print("값의 합계=", sum(values))