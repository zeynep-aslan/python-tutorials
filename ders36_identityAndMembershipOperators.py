# -------- Identity Operator = is --------
# referanstaki adres bilgisini karşılaştırır

# x = y = [1,2,3]  # x ve y aynı adreste tutulur
# z = [1,2,3]

# print(x==y)     # değer kontrolü
# print(x==z)
# print(x is y)   # x ve y aynı adresteler mi
# print(x is z)   # adres kontrolü

# --------

# x = [1,2,3]
# y = [2,4]

# del x[2]
# y[1] = 1
# y.reverse()  # 2 listenin değerleri aynı
# print(x == y)
# print(x is y) # ama adresleri gene de farklı
# print(x is not y)   # bu şekilde de sorabilirsin


# -------- Membership Operator = in --------
# içinde var mı

# x = ['banana', 'apple']
# print('banana' in x)   # listenin içinde var mı

# name = 'Zeynep'
# print('e' in name)
