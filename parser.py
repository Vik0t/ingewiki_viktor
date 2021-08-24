
#s = 'pythonist'
#dic = dict()
#coun = 0
#
#
#for i in range(len(s)):
#    for x in s:
#        if x in s[i]:
#            coun += 1
#    dic[s[i]] = coun
#    coun = 0
#
#print(dic)

# 2

# Task 2
stri1 = []
stri2 = []

with open('/home/user/Загрузки/Telegram Desktop/apriltagsDB.yaml') as f:
    d = {}
    a = f.readlines()
    for i in range(len(a)):
        if a[i] == '\n':
            continue
        else:
            a[i] = a[i].strip()
            b = a[i].split(':')
            if b[0] == '- tag_id':
                stri1.append(b[1])


            if b[1] != int and b[0] != 'traffic_sign_type':
                pass
            else:
                stri2.append(b[1])

stri1 = [int(item) for item in stri1]


final = dict(zip(stri1, stri2))
print(final)




