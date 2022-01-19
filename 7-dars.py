# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 17:20:43 2022

@author: Siroj_hacker
"""

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narhlar = [12000, 18000, 10900, 22000, -25, 66.66]
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = ['siroj', 'alli', 'believer']
cars = []

print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[2])

bozorlik = ['un', 'kartoshka', 'piyoz', 'banan', 'olma']
mahsulot = bozorlik.pop(3)

print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)

ismlar_new = ["Islom", "Yusuf", "Rajab"]
print(ismlar_new)

ism1 = ismlar_new.pop(0)
print("Salom " + ism1 + " bugun futbolga boramizmi?")

ism2 = ismlar_new.pop(1)
print( ism2 + " kutubxonaga borasanmi?")

ism3 = ismlar_new.pop(-1)
print(ism3 + " darslaringni qildingmi?")

sonlaar = [10, -7, 5.5, 100]

t_shaxslar = ['Gazzoliy', 'Umar ibn Xattob', 'Umar ibn Abdulaziz']
z_shaxslar = ['Ilon Mask', 'Zuckerberg', 'Nouman Ali Khan']

t_1 = t_shaxslar.pop(1)
print("Men tarixiy shaxslardan " + t_1 + " bilan suhbat qilishni istar edim")

z_1 = z_shaxslar.pop(2)
print("Men zamonaviy shaxslardan " + z_1 + " bilan suhbat qilishni istar edim")

print("Men tarixiy shaxslardan " + t_1 " bilan, zamonaviy shaxslardan esa" + z_1 + " bilan suhbat qilishni istar edim")

friends = []
friends.append('Bahodir')
friends.append('Javohir aka')
friends.append('Mehriddin')
friends.append('Abdulhodiy')
print(friends)

mehmonlar = ['Saloh', 'Shaxrizod', '' ]
mehmonlar = ['Saloh', 'Shaxrizod', 'Ubay', 'Jasur', 'Iskandar', 'Xurshid']
kelganlar = mehmonlar.pop(0)(1)(-1)
print("Mehmonga " + kelganlar + "lar keldi")
print("Kelmaganlar: ", mehmonlar)

























