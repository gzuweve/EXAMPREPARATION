# 11358
# def f(n, k):
#    if n > k:
#        return 0
#    elif n == k:
#        return 1
#    else:
#         return f(n + 1, k) + f(n + 2, k) + f(n * 2, k)
# print(f(3, 10) * f(10, 12))



# 27248
# def f(n, h):
#     if h > 5:
#         sp.add(n)
#         return 0
#     else:
#         sp.add(n)
#         return f(n + 1, h + 1) + f(n * 2, h + 1)
# sp = set()
# f(1, 1)
# print(sorted(sp))

# 13418
# def f(n, k):
#     if n > k:
#         return 0
#     elif n == k:
#         return 1
#     elif n == 26:
#         return 0
#     else:
#         return f(n + 1, k) + f(2 * n + 1, k)
# print(f(1, 27))


# 75287
# def f(n, k):
#     if k > n:
#         return 0
#     elif n == 10:
#         return 0
#     elif n == k:
#         return 1
#     else:
#         if n % 3 == 0:
#             return f(n - 2, k) + f(n // 3, k)
#         else:
#             return f(n - 2, k) + f(n - 4, k)
# print(f(38, 6))



# 18598
# def f(n, k):
#     if n > k:
#         return 0
#     elif n == 14:
#         return 0
#     elif n == k:
#         return 1
#     else:
#         return f(n + 1, k) + f(n * 2, k) + f(n * 3, k)
# print(f(1, 12) * f(12, 40))
