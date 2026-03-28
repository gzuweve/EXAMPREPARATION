# 7763
# P = list(range(5,31))
# Q = list(range(14,24))
# m = 0
# for a1 in range (1, 100):
#     for a2 in range (a1 + 1, 100):
#         check = True
#         A = list(range(a1, a2+1))
#         for x in range(1,100):
#             f = ((x in P) == (x in Q)) <=( not (x in A))
#             if not f:
#                 check = False
#                 break
#         if check:
#             m = max(m , a2-a1)
# print(m)
from turtle import TurtleGraphicsError


#8666
# P = list(range(25, 51))
# Q = list(range(32, 48))
# m = 0
# for a1 in range(1, 100):
#     for a2 in range (a1 + 1, 100):
#         check = True
#         A = list(range(a1, a2+1))
#         for x in range (1, 100):
#             f = ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))
#             if not f:
#                 check = False
#                 break
#         if check:
#             m = max(m, a2-a1)
# print(m)




#9653
# P = list(range(10, 30))
# Q = list(range(13, 19))
# m = 0
# for a1 in range(1, 100):
#     for a2 in range (a1 + 1, 100):
#         check = True
#         A = list(range(a1, a2+1))
#         for x in range (1, 100):
#             f = ((x in A) <= (x in P)) or (x in Q)
#             if not f:
#                 check = False
#                 break
#         if check:
#             m = (max(m, a2-a1))
# print(m)




#13745
# m = 0
# for a in range(1, 100):
#     check = True
#     for x in range (1,100):
#         for y in range (1, 100):
#             f = ((x <= 9)<= (x*x<=a)) and ((y*y<=a) <= (y<=9))
#             if not f:
#                 check = False
#                 break
#         m = max(m, a)
# print (m)



#15928 (отриц числа)
# m = 0
# for a1 in range (-50, 50):
#     for a2 in range (a1 + 1, 50):
#         check = True
#         A = list(range(a1, a2+1))
#         for x in range (-50,50):
#             for y in range (-50, 50):
#                 f = ((x in A) <= (x**2<=81)) and ((y**2 <= 36) <= (y in A))
#                 if not f:
#                     check = False
#                     break
#         if check:
#             m = max(m, a2-a1)
# print (m)



#34517
# m=0
# for a in range (1,100):
#     check = True
#     for x in range(1,100):
#         f = ((x&a != 0) <= ((x&10 == 0) <= (x&3 != 0)))
#         if not f:
#             check = False
#             break
#     if check:
#         m = max(m,a)
# print(m)


# Вариант ИН2510301
# m = 1000000000
# for a in range(80000,100000):
#     check = True
#     for x in range(1,100000):
#         for y in range(1,100000):
#             if ((y<a)and(x<a)or(89241<(5*y+x))) == False:
#                 check = False
#                 break
#     if check:
#         # m = min(m, a)
#         print(a)
# print(m)

# 18797
# m = 0
# for a in range(1,1000):
#     check = True
#     for x in range(1,100):
#         for y in range(1,100):
#             if ((x>a)or(y>x)or(2*y+x<110)) == False:
#                 check = False
#     if check:
#         m = max(m, a)
# print(m)


# 13745
# m = 0
# for a in range(1,1000):
#     check = True
#     for x in range(1,100):
#         for y in range(1,100):
#             if (((x <= 9) <= (x * x <= a)) and ((y * y <= a)) <= (y <= 9)) == False:
#                 check = False
#     if check:
#         m = max(m, a)
# print(m)


# 7763
# m = 0
# p = range(5, 31)
# q = range(14, 24)
# for a1 in range(1,100):
#     for a2 in range(a1 + 1,100):
#         check = True
#         a = range(a1, a2)
#         for x in range(1,100):
#             if (((x in p) == (x in q)) <= (not(x in a))) == False:
#                 check = False
#         if check:
#             m = max(m, len(a))
# print(m)


# 11119
# m = 10000
# p = range(20,51)
# q = range(30,66)
# d = None
# for a1 in range(1, 1000):
#     for a2 in range(a1 + 1, 1000):
#         check = True
#         a = range(a1, a2)
#         for x in range(1, 100):
#             if ((not(x in a)) <= ((x in p) <= (not(x in q)))) == False:
#                 check = False
#         if check:
#             m = min(m, len(a))
# print(m)



# m = 1000
# s = range(212, 315)
# t = range(287, 412)
# for a1 in range(200, 500):
#     for a2 in range(a1 + 1, 500):
#         check = True
#         a = range(a1, a2)
#         for x in range(0, 1000):
#             if ((not(x in a)) <= ((x in t) == (x in s))) == False:
#                 check = False
#         if check:
#             m = min(m, len(a))
# print(m)


# 9804
# m = 10000
# for a in range(0,1000):
#     check = True
#     for x in range(0, 1000):
#         if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))) == False:
#             check = False
#     if check:
#         m = min(m,a)
# print(m)



# 8106
# def Del(n, m):
#     if n % m == 0:
#         return True
#     else:
#         return False
# m = 0
# for a in range(1,1000):
#     check = True
#     for x in range(1, 1000):
#         if ((not(Del(x, a))) <= ((Del(x, 6)) <= (not(Del(x,4))))) == False:
#             check = False
#     if check:
#         m = max(m,a)
# print(m)



# ДЗ

# 34513
# m = 1000
# for a in range(1,1000):
#     check = True
#     for x in range(1,100):
#         if ((x & 33 == 0) <= ((x & 45 != 0) <= (x & a != 0))) == False:
#             check = False
#     if check:
#         m = min(m, a)
# print (m)

# 34544 неправильно
# m = 1000
# p = range(10,40)
# q = range(23,59)
# for a1 in range(5,60):
#     for a2 in range(a1 + 1, 60):
#         check = True
#         a = range(a1, a2)
#         for x in range(0,1000):
#             if ((((x in p) and (x in q))) <= (((x in q) and (x in a)))) == False:
#                 check = False
#         if check:
#             m = min(m, len(a))
# print(m)

# 18720
# m = 1000
# for a in range(1, 1000):
#     check = True
#     for x in range (1,100):
#         for y in range(1, 100):
#             if ((x * y < a) or (x < y) or (x >= 12)) == False:
#                 check = False
#     if check:
#         m = min(m, a)
# print(m)




# 35473
# def Del(n, m):
#     if n % m == 0:
#         return True
#     else:
#         return False
# m = 1000
# for a in range (1,1000):
#     check = True
#     for x in range(1, 100):
#         if (Del(a, 45) and ((Del(750, x)) <= ((not(Del(a, x))) <= ((not(Del(120,x))))))) == False:
#             check = False
#     if check:
#         m = min(m, a)
# print(m)


# 58217
# sminn = 0
# def Treug(n,m,k):
#     sminn = sum([n,m,k]) - max(n,m,k) - min(n,m,k)
#     if max(n,m,k) < min(n,m,k) + sminn:
#         return True
#     else:
#         return False
# m = 0
# for a in range(1,1000):
#     check = True
#     for x in range(1,1000):
#         f = not((Treug(x,11,16) == (not(max(x,5) > 10))) and Treug(4, a, x))
#         if f == False:
#             check = False
#     if check:
#         m = max(m, a)
# print(m)





# 1 неправильно
# m = 1000
# p = range(15, 41)
# q = range(21, 64)
# l = None
# for a1 in range(10, 100):
#     for a2 in range(a1 + 1, 100):
#         check = True
#         a = range(a1, a2)
#         for x in range(1, 1000):
#             f = (x in p) <= (((x in q) and (not(x in a))) <= (not(x in p)))
#             if f == False:
#                 check = False
#         if check:
#             if len(a) < m:
#                 l = a
#             m = min(m, len(a))
# print(l)
# print(m-1)


# 8
# m = 1000
# p = range(8, 40)
# q = range(23, 59)
# for a1 in range(5 ,65):
#     for a2 in range(a1 + 1 ,65):
#         check = True
#         a = range(a1, a2+1)
#         for x in range(1,1000):
#             f = ((x in p) or (x in a)) <= ((x in q) or (x in a))
#             if f == False:
#                 check = False
#         if check:
#             m = min(m, len(a))
# print(m)


# 4 неправильно
# m = 1000
# p = range(17, 55)
# q = range(37, 84)
# l = None
# for a1 in range(0 ,200):
#     for a2 in range(a1 + 1 ,200):
#         check = True
#         a = range(a1, a2+1)
#         for x in range(0,1000):
#             f = (x in p) <= (((x in q) and (not(x in a))) <= (not(x in p)))
#             if f == False:
#                 check = False
#         if check:
#             if len(a) < m:
#                 l = a
#             m = min(m, len(a))
# print(l)
# print(m)






