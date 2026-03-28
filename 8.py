#7667
# import itertools
# a = itertools.product("ЕГЭ", repeat = 5)
# s = 0
# for x in a:
#     if x[0] == "Е" or x[0] == "Э":
#         s += 1
# print (s)

#7986
# import itertools
# a = itertools.product("ЗИМА", repeat = 5)
# s = 0
# for x in a:
#     if (x[0] == "И" or x[0] == "А") and (x[4] == "И" or x[4] == "А"):
#         s += 1
# print (s)


#8098
# import itertools
# a = itertools.product("СЛОН", repeat = 5)
# s = 0
# for x in a:
#     if x.count("С") == 1:
#         s += 1
# print(s)

#7636 POL
# import itertools
# a = itertools.product("0123456789AB", repeat = 5)
# s = 0
# for x in a:
#     if x[0] != "0" and x.count("7") == 1 \
#             and x.count("9") + x.count("A") + x.count("B") <= 3:
#         s += 1
# print (s)


#29195
# import itertools
# a = itertools.product("РЕГИНА", repeat =  5)
# s = 0
# for x in a:
#     if x.count("Р") == 1 and x.count("Г") == 1 and x.count("Н") <= 1:
#         s += 1
# print (s)


