#27818
# def f(x, r):
#     if x >= 69 and r == 3: return 0
#     elif x < 69 and r == 4: return 0
#     elif x >= 69 and r == 4: return 1
#     else:
#         if r % 2 != 0:
#             return f(x+1, r + 1) or f(x+4, r + 1) or f(x*5, r + 1)
#         else:
#             return f(x+1, r + 1) and f(x+4, r + 1) and f(x*5, r + 1)
# for s in range(1, 69):
#     if f(s, 1) == 1:
#         print(s)

#45254
# def f(x, y, r):
#     if x + y >= 231 and r == 2: return 0
#     elif x + y >= 231 and r == 3: return 0
#     elif x + y < 231 and r == 4: return 0
#     elif x + y >= 231 and r == 4: return 1
#     else:
#         if r % 2 != 0:
#             return f(x+1, y, r+1) or f(x*2, y, r+1) or f(x, y+1, r+1) or f(x, y*2, r+1)
#         else:
#             return f(x + 1, y, r + 1) and f(x * 2, y, r + 1) and f(x, y + 1, r + 1) \
#                 and f(x, y * 2, r + 1)
# for s in range (1, 214):
#     if f(17, s, 1) == 1:
#         print(s)



#27812
# def f(x, r):
#     if x >= 48 and r == 2: return 0
#     elif x >= 48 and r == 3: return 0
#     elif x < 48 and r == 4: return 0
#     elif x >= 48 and r == 4: return 1
#     else:
#         if r % 2 != 0:
#             return f(x+1, r+1) or f(x+4, r+1) or f(x*2, r+1)
#         else:
#             return f(x+1, r+1) and f(x+4, r+1) and f(x*2, r+1) #?
# for s in range (1, 48):
#     if f(s, 1) == 1:
#         print (s)


#75258
# def f(x, r):
#     if x <= 15 and r == 4:
#         return 1
#     elif x <= 15 and r < 4:
#         return 0
#     elif x > 15 and r == 4:
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
#         if r % 2 != 0:
#             return any(v)
#         else:
#             return all(v)
# for s in range(16, 1000):
#     if f(s, 1) == 1:
#         print(s)





