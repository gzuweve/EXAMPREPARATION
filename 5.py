#15622
# for n in range(1,1000):
#     a = bin(n)[2::]
#     s = 0
#     for i in range(len(a)):
#         s += int(a[i])
#     if s % 2 != 0:
#         a += "11"
#     else:
#         a += "00"
#     r = int(a, 2)
#     if r > 114:
#         print(r)


#16381
# for n in range(1, 10000):
#     b = bin(n) [2:-1:]
#     if n % 2 != 0:
#         b += "10"
#     else:
#         b += "01"
#     i = int(b, 2)
#     if i == 2018:
#         print(n)


#18487
# for n in range(1, 1000):
#     b = bin(n) [2::]
#     v = b[::-1]
#     r = int(v, 2)
#     if n<100 and r ==13:
#         print(n)





#8094
# for n in range (1,100):
#     a = bin(n) [2::]
#     s = 0
#     for i in range(len(a)):
#          s += int(a[i])
#     b = s % 2
#     a += str(b)
#     s = 0
#     for i in range(len(a)):
#          s += int(a[i])
#     b = s % 2
#     a += str(b)
#     r = int(a, 2)
#     if r > 43:
#         print(r)




#18785
# for n in range(1,100):
#     b = bin(n) [2::]
#     a = 0
#     for i in range (len(b)):
#         a += int(len(b))
#     if b[-1]=='0':
#         b = "1" + b + "0"
#     else:
#         b = "11" + b + "11"
#     i = int(b,2)
#     if i > 52:
#         print (n)


#18708
# for n in range (1,100):
#     b = bin(n) [2::]
#     a = 0
#     for i in range (len(b)):
#         a += int(b[i])
#     b += str(a % 2)
#     a = 0
#     for i in range(len(b)):
#         a += int(b[i])
#     b += str(a % 2)
#     r = int(b, 2)
#     if r > 85:
#         print(n)

# Вариант ИН2510301
# def convert_base(num: str, from_base : int, to_base : int): # сначала переводим число в десятичную систему
#     if from_base != 10:
#         dec = int(num, from_base) # потом из десятичной — в нужную систему
#     else:
#         dec = int(num)
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if dec == 0:
#         return "0"
#     res = ""
#     while dec > 0:
#         res = digits[dec % to_base] + res
#         dec //= to_base
#     return res
# for n in range (1,100):
#     b = convert_base(str(n), 10, 3)
#     if n % 3 == 0:
#         w = b[-1]
#         u = b[-2]
#         a = b + u + w
#     else:
#          yu = 0
#          for s in range (len(b)):
#              yu += int(b[s])
#          k = yu * 3
#          l = convert_base(str(k), 10, 3)
#          a = b + l
#     r = convert_base(a, 3 , 10)
#     r = int(r)
#     if r > 800 and r < 852:
#         print(r)




# 8094
# kolvo = 0
# kolvo2 = 0
# for n in range(1, 1000):
#     n = bin(n)[2::]
#     kolvo = n.count("1")
#     ost = kolvo % 2
#     s = n + str(ost)
#     kolvo2 = s.count("1")
#     ost2 = kolvo2 % 2
#     ss = s + str(ost2)
#     t = int(ss, 2)
#     if 43 < t:
#         print(t)

# 64890 скип
# h = 0
# for n in range(1, 2000000000):
#     nn = bin(n)[2::]
#     nn += str(bin(n % 4))[2::]
#     nn = int(nn, 2)
#     if nn >= 1000000000 and nn <= 17894556123:
#         h += 1
# print(h)

# 73831
# for n in range(1,1000000000):
#     d = bin(n)[2::]
#     h = d.count('1')
#     j = d.count('0')
#     h = bin(h)[2::]
#     j = bin(j)[2::]
#     m = h + j
#     m = int(m,2)
#     if m == 214:
#         print(n)

# 7751
# for x in range(1000,10000):
#     k = str(x)
#     f = int(k[0]) + int(k[1])
#     s = int(k[2]) + int(k[3])
#     if f > s:
#         m = str(s) + str(f)
#     else:
#         m = str(f) + str(s)
#     if int(m) == 117:
#         print(x)







