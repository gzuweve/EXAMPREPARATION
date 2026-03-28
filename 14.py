# def convert_base(num, from_base, to_base): # сначала переводим число в десятичную систему
#     dec = int(num, from_base) # потом из десятичной — в нужную систему
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if dec == 0:
#         return "0"
#     res = ""
#     while dec > 0:
#         res = digits[dec % to_base] + res
#         dec //= to_base
#     return res
#
# s = 9**8+3**5-9
# g = convert_base(str(s), 10, 3)
# print(g.count("2"))
import sys
from string import digits


# s = 125+25**3+5**9
# g = convert_base(str(s), 10, 3)
# print(len(g))


# 47218
# for x in ("0123456789ABCDE"):
#     a = f"123{x}5"
#     b= f"1{x}233"
#     g = convert_base(str(a), 15, 10)
#     h = convert_base(str(b), 15, 10)
#     if (int(g) + int(h)) % 14 == 0:
#         print((int(g) + int(h)) // 14)
#         break


# 59692
# for x in ("0123456789ABCDEFGHI"):
#     a = f"98{x}79641"
#     b = f"36{x}14"
#     c = f"73{x}4"
#     g = int(convert_base(str(a), 19, 10))
#     h = int(convert_base(str(b), 19, 10))
#     k = int(convert_base(str(c), 19, 10))
#     if (g + h + k) % 18 == 0:
#         print((g+h+k)//18)

# 61360
# l = []
# for x in range(0, 37):
#     for y in range(0, 37):
#         s = "12{x}643{y}7"
#         s =  1 * 37 ** 7 + 2 * 37 ** 6 + x * 37 ** 5+ 6 * 37 ** 4 + 4 * 37 ** 3 + 3 * 37 ** 2 + y * 37 ** 1 + 7 * 37 ** 0
#         if s % 36 == 0:
#             s = y * 37 ** 1 + x
#             l.append(s)
# print(max(l))





# 45248
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
# sys.set_int_max_str_digits(999999999)
# s = 7*512**1912+6*64**1954-5*8**1991-4*8**1980-2022
# # g = convert_base(str(s), 10, 8)
# g = oct(s)
# print(g.count("7"))




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
# sys.set_int_max_str_digits(999999999)
# x = "0123456789ABCDEFGHIJK"
# for i in range(len(x)):
#     s = f"2496{x[i]}2"
#     g = convert_base(str(s),21, 10)
#     ss = f"8{x[i]}223"
#     gg = convert_base(str(ss), 21, 10)
#     sss = f"2331768{x[i]}3"
#     ggg = convert_base(str(sss), 21, 10)
#     o = int(g) + int(gg) + int(ggg)
#     if o % 20 == 0:
#         print(o//20)


# 48384
# x = "012345678"
# y = "012345678"
# for i in range(len(x)):
#     for a in range(len(y)):
#         f = f"88{x[i]}4{y[a]}"
#         s = f"7{x[i]}44{y[a]}"
#         g = int(f, 9)
#         gg = int(s, 11)
#         o = int(g) + int(gg)
#         if o % 61 == 0:
#             print(o//61)

# 48387
# x = "0123456789A"
# y = "0123456789A"
# for i in range(len(x)):
#     for j in range (len(y)):
#         f = f'{x[i]}341{y[j]}'
#         s = f'56{x[i]}1{y[j]}'
#         g = int(f, 11)
#         gg = int(s, 19)
#         o = int(g) + int(gg)
#         if o % 305 == 0:
#             print(o//305)


# 63030
# for x in range(0, 40):
#     for y in range(0, 40):
#         f =  5 * 40 ** 8 + 7 * 40 ** 7 + x * 40 ** 6 + 6 * 40 ** 5 + 9 * 40 ** 4 + 2 * 40 ** 3 + y * 40 ** 2 + 1 * 40 + 9
#         ff = y * 40 + x
#         h = ff ** 0.5
#         if f % 39 == 0 and h == round(h):
#             print(ff)



# 76682
# for p in range(11, 36):
#     for z in range(1, p):
#         for x in range(1, p):
#             for y in range(0, p):
#                 ff = x * p ** 2 + y * p ** 1 + z * p ** 0
#                 a = z * p ** 1 + x * p ** 0
#                 b = x * p ** 1 + y * p ** 0
#                 c = z * p ** 2 + y * p ** 1 + 10 * p ** 0
#                 if a + b == c:
#                     print(ff)




# 73869
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
# sys.set_int_max_str_digits(999999999)
#
# for x in range(20000000,100000000):
#     s = 4 * 7 ** 24 + 6 * 7 ** 13 + 4 * 49 ** 4 + 5 * 343 ** 2 + 20 - x
#     ss = convert_base(s, 10, 7)
#     if ss.count("6") > ss.count("0"):
#         print(int(x))




#73840
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
# sys.set_int_max_str_digits(999999999)
# for x in range (10**7,10**8):
#     s = 4 * 7 ** 24 + 6 * 7 ** 13 + 5 * 49 ** 4 + 2 * 343 ** 2 + 10 - x
#     ss = convert_base(s , 10, 7)
#     if ss.count('6') > ss.count('0'):
#         print(int(x))


# 55601
# digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for p in range(7, len(digits)):
#     for x in digits [1:p:]:
#         for y in digits [1:p:]:
#             for z in digits[:p:]:
#                 f = f"{y}4{y}"
#                 s = f"{y}65"
#                 t = f"{x}{z}23"
#                 if int(f, p) + int(s, p) == int(t, p):
#                     print(int(f"{x}{y}{z}", p))


#48391
# digits = "0123456789AB"
# for x in digits:
#     for y in digits:
#         f = f"{y}AA{x}"
#         s = f"{x}02{y}"
#         ff = int(f, 12)
#         ss = int(s, 14)
#         t = ff + ss
#         if t % 80 == 0:
#             print(t//80)


#72572
# for x in range(0, 37):
#     f = 15 * 37 ** 8 + 2 * 37 ** 7 + 9 * 37 ** 6 + x * 37 ** 5 + 8 * 37 ** 4 + 14 * 37 ** 3 + 10 * 37 ** 2 + 13 * 37 ** 1 + 6 * 37 ** 0
#     s = 11 * 37 ** 8 + 10 * 37 ** 7 + x * 37 ** 6 + 13 * 37 ** 5 + 14 * 37 ** 4 + 0 * 37 ** 3 + 12 * 37 ** 2 + 1 * 37 ** 1 + 11 * 37 ** 0
#     t = f * s
#     if t % 36 == 0:
#         print(1 * 37 ** 2 + x * 37 ** 1 + 2 * 37 ** 0)
