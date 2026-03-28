# 8230 POL
# file = open ("24-359.txt").read().strip()
# l = 0
# y = 0
# chislo_2025 = 0
# maxposl = 0
# for r in range (len(file)):
#     if file[r] == "Y":
#         y += 1
#     if r >= 3 and file[r-3:r+1] == "2025":
#         chislo_2025 += 1
#     while y > 80:
#         if file[l] == "Y":
#             y -= 1
#         if file[l:l+4] == "2025":
#             chislo_2025 -= 1
#         l += 1
#     if y == 80 and chislo_2025 >= 90:
#         maxposl = max(maxposl, r - l + 1)
# print (maxposl)



#8229 POL
# file = open ("24-358.txt").read().strip()
# l = 0
# y = 0
# chetchislo = 0
# maxposl = 0
# for r in range (len(file)):
#     if file[r] == "Y":
#         y += 1
#     if file[r] in ["0", "2", "4",  "6",  "8"]:
#         maxposl += 1
# print (maxposl)
