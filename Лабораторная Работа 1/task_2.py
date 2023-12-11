# TODO Найдите количество книг, которое можно разместить на дискете

vol = 1.44  # объем дискеты
page = 100
strings = 50
sym = 25
onesym = 4

countb = 4 * sym * strings * page
siseb = int(vol * 1024 * 1024)

print("Количество книг, помещающихся на дискету:", siseb // countb)
