import time
import random

Money1 = 0

print("""   История обновлений игры Shop всего
 08.04.2024 - добовление списка обновления и улучшения бота продуктов
 15.04.2024 - Улучшение бота продуктов и подготовный секретный купон
   До новых обновлений :)
   """)

a1 = "Хлеб"
a2 = "Молоко"
a3 = "Яйца"
a4 = "Сахар"
a5 = "Соль"
a6 = "Сметана 15%"
a7 = "Морковь 1кг"
a8 = "Картофель в сетке"
a9 = "Гречка круппа 1кг"
a10 = "Молочная колбаса"

a1a = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
if a1a == a1:
    a2a = "Скидка на хлеб 25 рублей. Итог: 25 рублей"
elif a1a == a2:
    a2a = "Скидка на молоко 40 рублей. Итог: 40 рублей"
elif a1a == a3:
    a2a = "Скидка на яйца 70 рублей. Итог: 70 рублей"
elif a1a == a4:
    a2a = "Скидка на сахар 30 рублей. Итог: 30 рублей"
elif a1a == a5:
    a2a = "Скидка на соль 20 рублей. Итог: 20 рублей"
elif a1a == a6:
    a2a = "Скидка на сметану 40 рублей. Итог: 40 рублей"
elif a1a == a7:
    a2a = "Скидка на Морковь 1кг 20 рублей. Итог: 20 рублей"
elif a1a == a8:
    a2a = "Скидка на картофель в сетке 20 рублей. Итог: 20 рублей"
elif a1a == a9:
    a2a = "Скидка на гречка круппа 1кг 20 рублей. Итог: 20 рублей"
elif a1a == a10:
    a2a = "Скидка на молочная колбаса 150 рублей. Итог: 150 рублей"

Money = 3
print("Ваш баланс:", Money)

prodycts = random.randint(1, 10)

aa = a = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
bb = b = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
cc = c = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
dd = d = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
ee = e = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
ff = f = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
gg = g = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
hh = h = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
ii = i = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))
kk = k = random.choice((a1, a2, a3, a4, a5, a6, a7, a8, a9, a10))

if prodycts == 1:
    aa
    print("Ваши продукты:", a, sep="")
elif prodycts == 2:
    aa
    bb
    print("Ваши продукты:", a, ",", b, sep="")
elif prodycts == 3:
    aa
    bb
    cc
    print("Ваши продукты:", a, ",", b, ",", c, sep="")
elif prodycts == 4:
    aa
    bb
    cc
    dd
    print("Ваши продукты:", a, ",", b, ",", c, ",", d, sep="")
elif prodycts == 5:
    aa
    bb
    cc
    dd
    ee
    print("Ваши продукты:", a, ",", b, ",", c, ",", d, ",", e, sep="")
elif prodycts == 6:
    aa
    bb
    cc
    dd
    ee
    ff
    print("Ваши продукты:", a, ",", b, ",", c, ",", d, ",", e, ",", f, sep="")
elif prodycts == 7:
    aa
    bb
    cc
    dd
    ee
    ff
    gg
    print("Ваши продукты:", a, ",", b, ",", c, ",", d, ",", e, ",", f, ",", g, sep="")
elif prodycts == 8:
    aa
    bb
    cc
    dd
    ee
    ff
    gg
    hh
    print("Ваши продукты:", a, ",", b, ",", c, ",", d, ",", e, ",", f, ",", g, ",", h, sep="")
elif prodycts == 9:
    aa
    bb
    cc
    dd
    ee
    ff
    gg
    hh
    ii
    print("Ваши продукты:", a, ",", b, ",", c, ",", d, ",", e, ",", f, ",", g, ",", h, ",", i, sep="")
elif prodycts == 10:
    aa
    bb
    cc
    dd
    ee
    ff
    gg
    hh
    ii
    kk
    print("Ваши продукты:", a, ",", b, ",", c, ",", d, ",", e, ",", f, ",", g, ",", h, ",", i, ",", k, sep="")

time.sleep(2)
print("\n \n Магазин")
time.sleep(1)
print(
    "\n 1) Хлеб - 50 рублей \n 2) Молоко - 80 рублей \n 3) Яйца - 140 рублей \n 4) Сахар - 60 рублей \n 5) Соль - 40 рублей \n 6) Сметана 15% - 80 рублей \n 7) Морковь 1кг - 40 рублей \n 8) Картофель в сетке - 40 рублей \n 9) гречка круппа 1кг - 40 рублей \n 10) Колбаса молочная - 300 рублей \n")
print("Вы получили секретный купон, на уменьшение цены на 50%!!!")
print("как только закончился ваш выбор, напишите -")
prod = input("Ведите номер продукта, которое нужно купить:")
prod2 = input("Ведите номер продукта, которое нужно купить:")
prod3 = input("Ведите номер продукта, которое нужно купить:")
prod4 = input("Ведите номер продукта, которое нужно купить:")
prod5 = input("Ведите номер продукта, которое нужно купить:")
prod6 = input("Ведите номер продукта, которое нужно купить:")
prod7 = input("Ведите номер продукта, которое нужно купить:")
prod8 = input("Ведите номер продукта, которое нужно купить:")
prod9 = input("Ведите номер продукта, которое нужно купить:")
prod10 = input("Ведите номер продукта, которое нужно купить:")

K = prod or prod2 or prod3 or prod4 or prod5 or prod6 or prod7 or prod8 or prod9 or prod10

if "10" in prod:
    Money1 += 300
    OT = "Молочная колбаса - 300   всего: 300"
elif "1" in prod:
    Money1 += 50
    OT = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod:
    Money1 += 80
    OT = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod:
    Money1 += 140
    OT = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod:
    Money1 += 60
    OT = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod:
    Money1 += 40
    OT = "Соль - 40 рублей   Всего: 40"
elif "6" in prod:
    Money1 += 80
    OT = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod:
    Money1 += 40
    OT = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod:
    Money1 += 40
    OT = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod:
    Money1 += 40
    OT = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT = ""

if "10" in prod2:
    Money1 += 300
    OT2 = "Молочная колбаса - 300   всего: 300"
elif "1" in prod2:
    Money1 += 50
    OT2 = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod2:
    Money1 += 80
    OT2 = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod2:
    Money1 += 140
    OT2 = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod2:
    Money1 += 60
    OT2 = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod2:
    Money1 += 40
    OT2 = "Соль - 40 рублей   Всего: 40"
elif "6" in prod2:
    Money1 += 80
    OT2 = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod2:
    Money1 += 40
    OT2 = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod2:
    Money1 += 40
    OT2 = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod2:
    Money1 += 40
    OT2 = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT2 = ""

if "10" in prod3:
    Money1 += 300
    OT3 = "Молочная колбаса - 300   всего: 300"
elif "1" in prod3:
    Money1 += 50
    OT3 = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod3:
    Money1 += 80
    OT3 = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod3:
    Money1 += 140
    OT3 = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod3:
    Money1 += 60
    OT3 = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod3:
    Money1 += 40
    OT3 = "Соль - 40 рублей   Всего: 40"
elif "6" in prod3:
    Money1 += 80
    OT3 = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod3:
    Money1 += 40
    OT3 = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod3:
    Money1 += 40
    OT3 = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod3:
    Money1 += 40
    OT3 = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT3 = ""

if "10" in prod4:
    Money1 += 300
    OT4 = "Молочная колбаса - 300   всего: 300"
elif "1" in prod4:
    Money1 += 50
    OT4 = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod4:
    Money1 += 80
    OT4 = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod4:
    Money1 += 140
    OT4 = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod4:
    Money1 += 60
    OT4 = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod4:
    Money1 += 40
    OT4 = "Соль - 40 рублей   Всего: 40"
elif "6" in prod4:
    Money1 += 80
    OT4 = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod4:
    Money1 += 40
    OT4 = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod4:
    Money1 += 40
    OT4 = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod4:
    Money1 += 40
    OT4 = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT4 = ""

if "10" in prod5:
    Money1 += 300
    OT5 = "Молочная колбаса - 300   всего: 300"
elif "1" in prod5:
    Money1 += 50
    OT5 = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod5:
    Money1 += 80
    OT5 = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod5:
    Money1 += 140
    OT5 = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod5:
    Money1 += 60
    OT5 = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod5:
    Money1 += 40
    OT5 = "Соль - 40 рублей   Всего: 40"
elif "6" in prod5:
    Money1 += 80
    OT5 = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod5:
    Money1 += 40
    OT5 = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod5:
    Money1 += 40
    OT5 = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod5:
    Money1 += 40
    OT5 = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT5 = ""

if "10" in prod6:
    Money1 += 300
    OT6 = "Молочная колбаса - 300   всего: 300"
elif "1" in prod6:
    Money1 += 50
    OT6 = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod6:
    Money1 += 80
    OT6 = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod6:
    Money1 += 140
    OT6 = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod6:
    Money1 += 60
    OT6 = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod6:
    Money1 += 40
    OT6 = "Соль - 40 рублей   Всего: 40"
elif "6" in prod6:
    Money1 += 80
    OT6 = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod6:
    Money1 += 40
    OT6 = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod6:
    Money1 += 40
    OT6 = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod6:
    Money1 += 40
    OT6 = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT6 = ""

if "10" in prod7:
    Money1 += 300
    OT7 = "Молочная колбаса - 300   всего: 300"
elif "1" in prod7:
    Money1 += 50
    OT7 = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod7:
    Money1 += 80
    OT7 = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod7:
    Money1 += 140
    OT7 = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod7:
    Money1 += 60
    OT7 = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod7:
    Money1 += 40
    OT7 = "Соль - 40 рублей   Всего: 40"
elif "6" in prod7:
    Money1 += 80
    OT7 = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod7:
    Money1 += 40
    OT7 = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod7:
    Money1 += 40
    OT7 = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod7:
    Money1 += 40
    OT7 = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT7 = ""

if "10" in prod8:
    Money1 += 300
    OT8 = "Молочная колбаса - 300   всего: 300"
elif "1" in prod8:
    Money1 += 50
    OT8 = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod8:
    Money1 += 80
    OT8 = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod8:
    Money1 += 140
    OT8 = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod8:
    Money1 += 60
    OT8 = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod8:
    Money1 += 40
    OT8 = "Соль - 40 рублей   Всего: 40"
elif "6" in prod8:
    Money1 += 80
    OT8 = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod8:
    Money1 += 40
    OT8 = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod8:
    Money1 += 40
    OT8 = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod8:
    Money1 += 40
    OT8 = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT8 = ""

if "10" in prod9:
    Money1 += 300
    OT9 = "Молочная колбаса - 300   всего: 300"
elif "1" in prod9:
    Money1 += 50
    OT9 = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod9:
    Money1 += 80
    OT9 = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod9:
    Money1 += 140
    OT9 = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod9:
    Money1 += 60
    OT9 = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod9:
    Money1 += 40
    OT9 = "Соль - 40 рублей   Всего: 40"
elif "6" in prod9:
    Money1 += 80
    OT9 = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod9:
    Money1 += 40
    OT9 = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod9:
    Money1 += 40
    OT9 = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod9:
    Money1 += 40
    OT9 = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT9 = ""

if "10" in prod10:
    Money1 += 300
    OT10 = "Молочная колбаса - 300   всего: 300"
elif "1" in prod10:
    Money1 += 50
    OT10 = "Хлеб - 50 рублей   Всего: 50"
elif "2" in prod10:
    Money1 += 80
    OT10 = "Молоко - 80 рублей   Всего: 80"
elif "3" in prod10:
    Money1 += 140
    OT10 = "Яйца - 140 рублей   Всего: 140"
elif "4" in prod10:
    Money1 += 60
    OT10 = "Сахар - 60 рублей   Всего: 60"
elif "5" in prod10:
    Money1 += 40
    OT10 = "Соль - 40 рублей   Всего: 40"
elif "6" in prod10:
    Money1 += 80
    OT10 = "Сметана 15% - 80 рублей   Всего: 80"
elif "7" in prod10:
    Money1 += 40
    OT10 = "Морковь 1кг - 40 рублей   Всего: 40"
elif "8" in prod10:
    Money1 += 40
    OT10 = "Картофель в сетке - 40 рублей   Всего: 40"
elif "9" in prod10:
    Money1 += 40
    OT10 = "Гречка круппа 1кг - 40 рублей   Всего: 40"
else:
    Money1 += 0
    OT10 = ""

print("Ваш чек!!!")
print("\n", OT, "\n", OT2, "\n", OT3, "\n", OT4, "\n", OT5, "\n", OT6, "\n", OT7, "\n", OT8, "\n", OT9, "\n", OT10,
      "\n\n", "Итог:", Money1)
if K == "1":
    print("Вам выпало:", a2a)
    Money1 = -25
elif K == "2":
    print("Вам выпало:", a2a)
    Money1 = -40
elif K == "3":
    print("Вам выпало:", a2a)
    Money1 = -70
elif K == "4":
    print("Вам выпало:", a2a)
    Money1 = -30
elif K == "5":
    print("Вам выпало:", a2a)
    Money1 = -20
elif K == "6":
    print("Вам выпало:", a2a)
    Money1 = -40
elif K == "7":
    print("Вам выпало:", a2a)
    Money1 = -20
elif K == "8":
    print("Вам выпало:", a2a)
    Money1 = -20
elif K == "9":
    print("Вам выпало:", a2a)
    Money1 = -20
elif K == "10":
    print("Вам выпало:", a2a)
    Money1 = -150
