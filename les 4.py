s = 'pythonist'
dic = dict()
coun = 0


for i in range(len(s)):
    for x in s:
        if x in s[i]:
            coun += 1
    dic[s[i]] = coun
    coun = 0

print(dic)

# 2

f = open('/home/user/Рабочий стол/files py./файл.txt')

#line = ''
#for line in f:
#    line
#print(line)