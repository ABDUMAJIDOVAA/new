# 7-dars uyga vazifa
# vazifa1
# son = [1,2,3,4,5,6,7,8,9,10]

# def juft(x):
#      return x % 2 == 0

# result =list(filter(juft,son))

# print(result)

# vazifa2
# son = [1,2,3,4,5,6,7,8,9,10]

# def juft(x):
#      return x % 2 == 1

# result =list(filter(juft,son))

# print(result)

# vazifa3
# ismlar = ['Diyorbek','Fotimaxon','Aliyorbek','Nargizaxon']

# natija = list(filter(lambda ism: "jon" in ism.lower() or "bek" in ism.lower() or "qo`shimcha" in ism.lower(), ismlar))

# print(natija)

# vazifa4
# son = [1,6,4,9,0,10]
# son.sort(reverse=True)
# s = son[1]
# print(s)

# vazifa5
# def unli_va_undoshga_ajratish(word) :
#     unli = 0
#     undosh = 0:
#     for harf in word:
#         if harf.lower() in 'aeuoi' :
#             unli += 1
#         elif harf.isalpha() :
#             undosh += 1

#     return unli, undosh

# word = 'GM unliharf yoq'
# unli, undosh = unli_va_undoshga_ajratish(word)

# print('Unli harflar= ', unli )
# print('Undosh harflar= ', undosh)

# vazifa6
# ismlar = ['Madina','Hilol','Aliyor','Diyor','Madina']

# def ismlar_bi_xilligiga_tekshirish(ismlar) :
#     if len(ismlar) > 1 
#         return True
#     else :
#         return ismlar[0] == ismlar[-1]

# result = ismlar_bi_xilligiga_tekshirish(ismlar)
# print(result)