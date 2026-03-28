#59695
# maxx = 0
# maxxa = 0
# summ = 0
# kolvo = 0
# f = open(r"C:\Users\hzeww\Downloads\17.txt")
# a = []
# for i in f:
#     a.append(int(i))
#     s = i.strip()
#     if s[-1] == "5" and s[-2] == "1":
#         maxx = max(maxx, int(s))
# for x in range (len(a)-2):
#     j = a[x]
#     k = a[x+1]
#     l = a[x+2]
#     if (len(str(j)) == 4 and len(str(k)) != 4 and len(str(l)) != 4
#             or len(str(j)) != 4 and len(str(k)) == 4 and len(str(l)) != 4
#             or len(str(j)) != 4 and len(str(k)) != 4 and len(str(l)) == 4):
#         if maxx <= sum([j, k, l]):
#             kolvo += 1
#             maxxa = max(maxxa, sum([j, k, l]))
# print(kolvo, maxxa)



#37336
# maxx = 0
# summ = 0
# kolvo = 0
# f = open(r"C:\Users\hzeww\Downloads\17 (1).txt")
# a = []
# for i in f:
#     a.append(int(i))
# for x in range(len(a)-1):
#     j = a[x]
#     k = a[x+1]
#     if j % 3 == 0 or k % 3 == 0:
#         maxx = max(maxx, j + k)
#         kolvo+= 1
# print(kolvo, maxx)



#37337
# kolvo = 0
# maxx = 0
# a = []
# f = open(r"C:\Users\hzeww\Downloads\17 (3).txt")
# for i in f:
#     a.append(int(i))
# for x in range(len(a)-1):
#     for y in range(x + 1, len(a)):
#         p = a[x]
#         o = a[y]
#         j = p % 160
#         k = o % 160
#         if j != k and (p % 7 == 0 or o % 7 == 0):
#             kolvo +=1
#             maxx = max(maxx, (p+o))
# print(kolvo, maxx)



#47221
# kolvo = 0
# maxxa = 0
# maxx = 0
# a = []
# f = open(r"C:\Users\hzeww\Downloads\17 (4).txt")
# for i in f:
#     ii = int(i)
#     a.append(ii)
#     if ii % 10 == 3:
#         maxxa = max(maxxa, ii)
# for x in range(len(a)-1):
#     j = abs(a[x])
#     k = abs(a[x+1])
#     if ((j % 10 == 3 and k % 10 != 3) or (j % 10 != 3 and k % 10 == 3)) and \
#             (j**2 + k**2) >= maxxa**2:
#         kolvo += 1
#         p = j**2 + k**2
#         maxx = max (maxx, p)
# print(kolvo, maxx)





#37344
# kolvo = 0
# maxx = 0
# a = []
# f = open(r"C:\Users\hzeww\Downloads\17 (5).txt")
# for i in f:
#     ii = int(i)
#     a.append(ii)
# for x in range(len(a) -1):
#     for y in range(x + 1, len(a)):
#         j = a[x]
#         k = a[y]
#         if j * k % 10 == 0:
#             kolvo += 1
#             maxx = max(maxx, j + k)
# print(kolvo, maxx)




# 37336
# kolvo = 0
# maxx = -99999999999
# f = open(r"C:\Users\Ульянка\Downloads\17.txt")
# l = f.readlines()
# for i in range(len(l)-1):
#     m = int(l[i])
#     mm = int(l[i+1])
#     if m % 3 == 0 or mm % 3 == 0:
#         kolvo += 1
#         summ = mm + m
#         maxx = max(maxx, summ)
# print(kolvo, maxx)

# 37337
# kolvo = 0
# maxx = 0
# f = open(r"C:\Users\Ульянка\Downloads\17 (1).txt")
# l = f.readlines()
# for i in range(len(l)-1):
#     m = int(l[i])
#     for j in range(i+1, len(l)):
#         mm = int(l[j])
#         o = m % 160
#         p = mm % 160
#         if o != p and (m % 7 == 0 or mm % 7 == 0):
#             kolvo += 1
#             summ = m + mm
#             maxx = max(maxx, summ)
# print(kolvo, maxx)


# 39763
# kolvo = 0
# maxx = 0
# o = open(r"C:\Users\Ульянка\Downloads\17 (2).txt")
# l = o.readlines()
# for i in range(len(l)-2):
#     f = int(l[i])
#     s = int(l[i+1])
#     t = int(l[i+2])
#     avar = sum([f, s, t]) - (max(f, s, t) + min(f, s, t))
#     if max(f, s ,t)**2 < min(f, s, t)**2 + avar**2:
#         kolvo += 1
#         summ = f + s + t
#         maxx = max(maxx, summ)
# print(kolvo, maxx)


# 40733
# kolvo = 0
# maxx = 0
# summavar = 0
# kolvochet = 0
# o = open(r"C:\Users\Ульянка\Downloads\17 (3).txt")
# l = o.readlines()
# for j in range(len(l)):
#     if int(l[j]) % 2 == 0:
#         summavar += int(l[j])
#         kolvochet += 1
# avar = summavar / kolvochet
# for i in range(len(l)-1):
#     f = int(l[i])
#     s = int(l[i+1])
#     if (f % 3 == 0 or s % 3 == 0) and (f < avar or s < avar):
#         kolvo += 1
#         summ = f + s
#         maxx = max(maxx, summ)
# print(kolvo, maxx)



# stat301
# kolvo = 0
# maxx = -99999999
# maxxx = -99999999
# o = open(r"C:\Users\Ульянка\Downloads\17 (3).txt")
# l = o.readlines()
# for j in range(len(l)):
#     if int(l[j]) % 100 == 70:
#         h = int(l[j])
#         maxxx = max(maxxx, h)
# for i in range(len(l)-2):
#     f = int(l[i])
#     s = int(l[i+1])
#     t = int(l[i+2])
#     if f >= 0 and s >= 0 and t >= 0 and sum([f, s, t]) <= maxxx:
#         kolvo += 1
#         summ = sum([f, s, t])
#         maxx = max(maxx, summ)
# print(kolvo, maxx)

# if s in range(..):
#     k += 1
# if t in range(...):
#     k += 1
# if f in range(..):
#     k += 1
#
# if k == 2






































