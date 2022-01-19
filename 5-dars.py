# 5-dars. STRING (MATN)
# Sana: 3/01/2022
# Bajaruvchi: Sirojiddin

ism = "Sirojiddin"
print(ism)

shahar = "Kamashi"
print(shahar)

viloyat = "Kashkadarya"
print(viloyat)

ana_endi_yigla = "😅"
print(ana_endi_yigla)

matn = "Men yangi 📱 sotib oldim"
print(matn)

# STRING USTIDA AMALLAR BAJARAMIZ

ism = "Siroj"
print("Mening ismim " + ism)

ism = 'Siroj'
familiya = 'Samadov'
print(ism + familiya)
print(ism + ' ' + familiya)

# F- STRING USUL
ism = "Siroj"
familiya = "Samadov"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "David"
familiya = "Believer"
print(f"Salom, mening ismim {familiya}. {ism} {familiya}")

# MAHSUS BELGILAR

print('Hello world')
print('Hello \tworld')
print('Hello \nworld')


# STRING METODLAR

ism = "david"
familiya = "james"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
ism_sharif = ism_sharif.upper()
print(ism_sharif.capitalize())

meva = "   olma   "
print("Men " + meva.lstrip() + "yaxshi ko'raman")
print(meva)
print("Men " + meva.rstrip() + "yaxshi ko'raman")

print("Men " + meva.strip() + "yaxshi ko'raman")

print("Men " + meva + "yaxshi ko'raman")

# INPUT

ism = input("Ismingiz nima?")
print("Assalomu alaykum, " + ism)

ism = input("Ismingiz nima?\n")
print("Assalomu alaykum, " + ism.title())

# AMALIYOT-5. UYGA TOPSHIRIQ

kocha="bogbon"
mahalla="sogbon"
tuman="bodomzor"
viloyat="samarkand"
print(f"Mening manzilim {kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")


kocha = input("ko'chang qayerda?\n")
print("Assalomu alaykum, " + kocha.title())


              




























