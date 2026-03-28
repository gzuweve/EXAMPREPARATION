#27819
# def f(x, r):
#     if x >= 69 and r == 2: return 0
#     elif x >= 69 and r == 4: return 0
#     elif x < 69 and r == 5: return 0
#     elif x >= 69 and r == 3: return 1
#     elif x >= 69 and r == 5: return 1
#     else:
#         if r % 2 == 0:
#             return f(x+1, r + 1) or f(x+4, r + 1) or f(x*5, r + 1)
#         else:
#             return f(x + 1, r + 1) and f(x + 4, r + 1) and f(x * 5, r + 1)
# for s in range(1, 69):
#     if f(s, 1) == 1:
#         print(s)
# print ('---')
# def f(x, r):
#     if x >= 69 and r == 2: return 0
#     elif x < 69 and r == 3: return 0
#     elif x >= 69 and r == 3: return 1
#     else:
#         if r % 2 == 0:
#             return f(x+1, r + 1) or f(x+4, r + 1) or f(x*5, r + 1)
#         else:
#             return f(x + 1, r + 1) and f(x + 4, r + 1) and f(x * 5, r + 1)
# for s in range(1, 69):
#     if f(s, 1) != 1:
#         print(s)
import sys

#75258
# def f(x, r):
#     if x <= 15 and r == 3:
#         return 1
#     elif x <= 15 and r == 5:
#         return 1
#     elif x <= 15 and r == 4:
#         return 0
#     elif x <= 15 and r == 2:
#         return 0
#     elif x > 15 and r == 5:
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
# for s in range(16, 100):
#     if f(s, 1) == 1:
#         print(s)
# print('---')
# def f(x, r):
#     if x <= 15 and r == 3:
#         return 1
#     elif x <= 15 and r == 2:
#         return 0
#     elif x > 15 and r == 3:
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
# for s in range(16, 100):
#     if f(s, 1) != 1:
#         print(s)



#27773 #???
# def f(x, y, r):
#     if x + y <= 20 and r == 3: return 1
#     elif x + y <= 20 and r == 5: return 1
#     elif x + y > 20 and r == 5: return 0
#     elif x + y <= 20 and r == 4: return 0
#     elif x + y <= 20 and r == 2: return 0
#     else:
#         if r % 2 == 0:
#             return f(x - 1, y, r + 1) or f(x, y - 1, r + 1) \
#                 or f(x//2, y, r + 1) or f(x, y//2, r + 1)
#         else:
#             return f(x - 1, y, r + 1) and f(x, y - 1, r + 1) \
#                 and f(x//2, y, r + 1) and f(x, y//2, r + 1)
# for s in range (10,50):
#     if f(10, s, 1) == 1:
#         print(s)
# print('---')
# def f(x, y, r):
#     if x + y <= 20 and r == 3: return 1
#     elif x + y <= 20 and r == 2: return 0
#     elif x + y > 20 and r == 3: return 0
#     else:
#         if r % 2 == 0:
#             return f(x - 1, y, r + 1) or f(x, y - 1, r + 1) \
#                 or f(x//2, y, r + 1) or f(x, y//2, r + 1)
#         else:
#             return f(x - 1, y, r + 1) and f(x, y - 1, r + 1) \
#                 and f(x//2, y, r + 1) and f(x, y//2, r + 1)
# for s in range (11,50):
#     if f(10, s, 1) != 1:
#         print(s)



# статград 301
# def f(x ,r):
#     if r == 3 and x <= 1207: return 1
#     elif r == 5 and x <= 1207: return 1
#     elif r == 2 and x <= 1207: return  0
#     elif r == 4 and x <= 1207: return 0
#     elif r == 5 and x > 1207: return 0
#     else:
#         if r % 2 == 0:
#             return f(x - 3, r + 1) or f(x - 5, r + 1) or f(x // 4, r + 1)
#         else:
#             return f(x - 3, r + 1) and f(x - 5, r + 1) and f(x // 4, r + 1)
#
# for s in range(1208, 10000):
#     if f(s, 1) == 1:
#         print(s)
# print('---')
# def f(x ,r):
#     if r == 3 and x <= 1207: return 1
#     elif r > 3 and x <= 1207: return 0
#     elif r == 3 and x > 1207: return 0
#     else:
#         if r % 2 == 0:
#             return f(x - 3, r + 1) or f(x - 5, r + 1) or f(x // 4, r + 1)
#         else:
#             return f(x - 3, r + 1) and f(x - 5, r + 1) and f(x // 4, r + 1)
#
# for s in range(1208, 10000):
#     if f(s, 1) != 1:
#         print(s)




