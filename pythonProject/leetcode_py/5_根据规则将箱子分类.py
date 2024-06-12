def categorizeBox(length, width, height, mass):
    """
    :type length: int
    :type width: int
    :type height: int
    :type mass: int
    :rtype: str
    """
    str1 = 'Neither'
    flag1 = False
    flag2 = False
    categor_1 = length * width * height
    if categor_1 >= 10 ** 9 or width >= 10 ** 4 or length >= 10 ** 4 or height >= 10 ** 4:
        str1 = "Bulky"
        flag1 = True
    if mass >= 100:
        str1 = "Heavy"
        flag2 = True
    if flag1 and flag2:
        str1 = "Both"
    return str1


str2 = categorizeBox(length=10000, width=3968, height=3272, mass=727)
print(str2)
print(10**4)

#  idea 2
#     def categorizeBox(self, length, width, height, mass):
#         maxd = max(length, width, height)
#         vol = length * width * height
#         isBulky = maxd >= 10000 or vol >= 10**9
#         isHeavy = mass >= 100
#         if isBulky and isHeavy:
#             return 'Both'
#         if isBulky:
#             return 'Bulky'
#         if isHeavy:
#             return 'Heavy'
#         return 'Neither'
#
