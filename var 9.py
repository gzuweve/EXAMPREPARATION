#2 69880
# print ("x y z w")
# for x in range (0, 2):
#     for y in range (0, 2):
#         for z in range (0, 2):
#             for w in range(0, 2):
#                 if (((x <= y) <= z) or not(w)) == False:
#                     print(x, y, z, w)

#5 8654
# for x in range(1000, 10000):
#     a = str(x)
#     b = int(a[0]) * int(a[1])
#     c = int(a[2]) * int(a[3])
#     if b > c:
#         k = str(b) + str(c)
#     else:
#         k = str(c) + str(b)
#     if k == str(124):
#         print (x)




#8 8658
# import itertools
# a = itertools.product("АНП", repeat = 5)
# s = 0
# for x in a:
#     s += 1
#     if s == 201:
#         print(x)


#14 61360
l = []
for x in range(0, 37):
    for y in range(0, 37):
        s = "12{x}643{y}7"
        s =  1 * 37 ** 7 + 2 * 37 ** 6 + x * 37 ** 5+ 6 * 37 ** 4 + 4 * 37 ** 3 + 3 * 37 ** 2 + y * 37 ** 1 + 7 * 37 ** 0
        if s % 36 == 0:
            s = y * 37 ** 1 + x
            l.append(s)
print(max(l))






