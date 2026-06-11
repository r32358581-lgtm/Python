STUDENTS = 5
ist = []
count = 0

for i in range (STUDENTS):
    value = int(input("성적을 입력하시오:"))
    ist.append(value)

print("성적 평균=", sum(ist) / len(ist))
print("최대 점수=", max(ist))
print("최소 점수=", min(ist))

for score in ist:
    if score >= 80:
        count += 1
print("80점 이상=", count)