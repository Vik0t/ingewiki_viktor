# 1 задача
a = input()
i, j = 0, 0
for i in a:
    j += int(i)
print(j)
print()
print()
print()

# 2 задача
print("2 задача")
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for k in lst:
    if int(k) < 30 and int(k) % 2 == 0:
        print(k, end=" ")
print()

print("2 условие")
for k in lst:
    if int(k) % 3 == 0:
        print(k, end=" ")
print()

# 3 задачаj
a = input()
print("Да" if a == a[::-1] else "Нет" )
print()

# 4 задача
lf = input().split()
ls = input().split()
dic = dict()

for m in range(len(lf)):
    dic[lf[m]] = ls[m]
print(dic)
print()

# 5 задача
dc = input()
for lp in range(len(dc) - 1, -1, -1):
    print(dc[lp])
print()

# 6 задача

ssn = {1 : "Jan", 2 : "Feb", 3 : "May", 4 : "Apr", 5 : "May", 6 : "Jun", 7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov", 12 : "Dec"}
klp = int(input())
print(ssn.get(klp))