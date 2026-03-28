#27802
# def f(x, r):
#     if r == 3 and x < 68 :
#         return 0
#     elif r == 3 and x >= 68 :
#         return 1
#     elif r == 2 and x >= 68:
#         return 0
#     else:
#         return f(x + 1, r + 1) or f(x+4, r+1) or f(x*5, r+1)
#
#
# for s in range(1, 67):
#     if f(s, 1) == 1:
#         print(s)




#27808
# def f(x, r):
#     if r == 3 and x < 42: return 0
#     elif r == 3 and x >= 42: return 1
#     elif r == 2 and x >= 42: return 0
#     else: return f(x + 1, r + 1) or f(x + 3, r + 1) or f(x * 2, r + 1)
#
# for s in range(1, 41):
#     if f(s, 1) == 1:
#         print(s)



#38597
# def f(x, r):
#     if r == 3 and x < 29: return 0
#     elif r == 2 and x >= 29: return 0
#     elif r == 3 and x >= 29: return 1
#     else:
#         if r % 2 == 0:
#             return f(x+1, r+1) or f(x*2, r+1)
#         else:
#             return f(x+1, r+1) and f(x*2, r+1)
# for s in range(1, 29):
#     if f(s, 1) == 1:
#         print (s)




#40735
# def f(x, r, l):
#     if r == 3 and x < 33: return 0
#     elif r == 2 and x >= 33: return 0
#     elif r == 3 and x >= 33: return 1
#     else:
#         if r % 2 == 0:
#             if l == 1:
#                 return f(x+2, r+1, 2) or f(x*2, r+1,3)
#             elif l == 2:
#                 return f(x+1, r+1, 1) or f(x*2, r+1,3)
#             elif l == 3:
#                 return f(x+1, r+1, 1) or f(x+2, r+1,2)
#         else:
#             return f(x+1, r+1, 1) and f(x+2, r+1, 2) and f(x*2, r+1, 3)
#
# for s in range(1, 34):
#     if f(s, 1, 0) == 1:
#         print (s)




# 64904
# def f(x, r):
#     if r == 3 and x < 10: return 1
#     elif r == 3 and x >= 10: return 0
#     elif r == 2 and x < 10: return 0
#     else:
#         if r % 2 == 0:
#             if x % 3 == 0 and x % 2 == 0:
#                 return f(2*x/3, r+1) or f(x/2, r+1) or f(x-1, r+1)
#             elif x % 3 == 0:
#                 return f(2*x/3, r+1) or f(x-1, r+1)
#             elif x % 2 == 0:
#                 return f(x/2, r+1) or f(x-1, r+1)
#             else:
#                 return f(x-1, r+1)
#         else:
#             if x % 3 == 0 and x % 2 == 0:
#                 return f(2 * x / 3, r + 1) and f(x / 2, r + 1) and f(x - 1, r + 1)
#             elif x % 3 == 0:
#                 return f(2 * x / 3, r + 1) and f(x - 1, r + 1)
#             elif x % 2 == 0:
#                 return f(x / 2, r + 1) and f(x - 1, r + 1)
#             else:
#                 return f(x - 1, r + 1)
# for s in range(10, 100):
#     if f(s, 1) == 1:
#         print(s)




#ДЗ!

# 27820
# def f(x, r):
#     if r == 3 and x < 42: return 0
#     elif r == 2 and x >= 42: return 0
#     elif r == 3 and x >= 42: return 1
#     else:
#         if r % 2 == 0:
#             return f(x + 1, r + 1) or f(x + 2, r + 1) or f(x * 2, r + 1)
#         else:
#             return f(x + 1, r + 1) or f(x + 2, r + 1) or f(x * 2, r + 1)
# for s in range(1, 42):
#     if f(s, 1) == 1:
#         print(s)


#28105
# def f(x, r):
#     if r == 3 and x < 40: return 0
#     elif r == 2 and x >= 40: return 0
#     elif r == 3 and x >= 40: return 1
#     else:
#             return f(x+1, r+1) or f(x*3-2, r+1)
# for s in range(2, 40):
#     if f(s, 1) == 1:
#         print(s)



#73845
# def f(x, r):
#     if r == 3 and x > 19: return 0
#     elif r == 2 and x <= 19: return 0
#     elif r == 3 and x <= 19: return 1
#     else:
#         sp = []
#         sp.append(f(x - 5, r + 1))
#         if x % 2 == 0:
#             sp.append(f(x//2, r + 1))
#         if x % 3 == 0:
#             sp.append(f(x//3, r + 1))
#         if x % 3 != 0 and x % 2 != 0:
#             sp.append(f(x + 1, r + 1))
#
#         if r % 2 == 0:
#             return any(sp)
#         else:
#             return all(sp)
        # """if r % 2 == 0:
        #     if x % 2 == 0:
        #         return f(x/2, r + 1) or (x - 5, r +1)
        #     elif x % 3 == 0:
        #         return f(x/3, r + 1) or (x - 5, r +1)
        #     elif x % 2 != 0 and x % 3 != 0:
        #         return f(x+1, r+1) or (x - 5, r +1)
        # else:
        #     if x % 2 == 0:
        #         return f(x // 2, r + 1) and (x - 5, r +1)
        #     elif x % 3 == 0:
        #         return f(x // 3, r + 1) and (x - 5, r +1)
        #     elif x % 2 != 0 and x % 3 != 0:
        #         return f(x + 1, r + 1) and (x - 5, r +1)"""
#
# for s in range(19, 1000):
#     if f(s, 1) == 1:
#         print(s)




#27416
# def f(x, y, r):
#     if x + y >= 77 and r == 2: return 0
#     elif x + y < 77 and r == 3: return 0
#     elif x + y >= 77 and r == 3: return 1
#     else:
#         return f(x+1, y, r + 1) or  f(x, y+1, r + 1) \
#             or f(x*2, y, r+1) or f(x, y*2, r+1)
# for s in range(1, 70):
#     if f(7, s, 1) == 1:
#         print(s)


#55606
# minn = 100
# def f(x, y, r):
#     if x + y > 40 and r == 1: return 0
#     elif x + y <= 40 and r == 2: return 0
#     elif x + y > 40 and r == 2: return 1
#     else:
#         if x > y:
#             return f(x + 1, y, r + 1) or f(x + 2, y, r + 1) \
#                 or f(x + 3, y, r + 1) or f(x, y * 2, r + 1)
#         elif x < y:
#             return f(x, y + 1, r + 1) or f(x, y + 2, r + 1) \
#                 or f(x, y + 3, r + 1) or f(x * 2, y, r + 1)
#         elif x == y:
#             return f(x + 1, y, r + 1) or f(x + 2, y, r + 1) \
#                 or f(x + 3, y, r + 1) or f(x, y + 1, r + 1) \
#                 or f(x, y + 2, r + 1) or f(x, y + 3, r + 1)
# for s in range(1, 100):
#     for t in range(1, 100):
#         if f(s, t, 1) == 1:
#             if s + t < minn:
#                 minn = s + t
# print(minn)


#27817
# def f(x, r):
#     if x >= 69 and r == 2: return 0
#     elif x < 69 and r == 3: return 0
#     elif x >= 69 and r == 3: return 1
#     else:
#         return f(x+1, r + 1) or f(x+4, r + 1) or f(x*5, r + 1)
# for s in range(1, 69):
#     if f(s, 1) == 1:
#         print(s)


#27780
# def f(x, y, r):
#     if x + y >= 74 and r == 2: return 0
#     elif x + y < 74 and r == 3: return 0
#     elif x + y >= 74 and r == 3: return 1
#     else:
#         return f(x+1, y, r+1) or f(x*2, y, r+1) or f(x, y+1, r+1) or f(x, y*2, r+1)
# for s in range(1,62):
#     if f(12, s, 1) == 1:
#         print(s)


#58486
# minn = 1000
# def f(x, y, r):
#     if (x >=48 or y >= 48) and r == 2: return 1
#     elif r == 3: return 0
#     else:
#         if x > y:
#             return f(x+1, y, r+1) or f(x+2, y, r+1) or f(x+3, y, r+1) or f(x, y*2, r+1)
#         elif x < y:
#             return f(x, y+1, r + 1) or f(x, y+2, r + 1) or f(x, y + 3, r + 1) or f(x * 2, y, r + 1)
#         elif x == y:
#             return f(x, y + 1, r + 1) or f(x, y + 2, r + 1) or f(x, y + 3, r + 1) \
#         or f(x+1, y, r+1) or f(x+2, y, r+1) or f(x+3, y, r+1)
# for s in range(1, 100):
#     for t in range(1, 100):
#         if f(s, t,1) == 1:
#             minn = min(minn, s + t)
# print(minn)


#75256
# def f(x, r):
#     if x <= 15 and r == 3:
#         return 1
#     elif x > 15 and r == 3:
#         return 0
#     elif x <= 15 and r < 3:
#         return 0
#     else:
#         a = []
#         for k in range(2, 10):
#             if x % k == 0:
#                 a.append(k)
#         v = []  # [0,1,1,0,0]
#         for k in a:
#             v.append(f(x - k, r + 1))
#         if not a:
#             return f(x-1, r)
#         if r % 2 == 0:
#             return any(v)
#         else:
#             return all(v)
# for s in range(16, 1000):
#     if f(s, 1) == 1:
#         print(s)



