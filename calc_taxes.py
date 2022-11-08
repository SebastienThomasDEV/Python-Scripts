def percent(a):
    while True:
        try:
            a = int(a)
            return a
        except ValueError:
            a = a.split(",")
            a = ".".join(a)
            a = float(a)
            return a


def fpercent(a):
    while True:
        a = a / 100
        return a


def calc(a, b, c):
    while True:
        c = (a * b)
        return c


volume = int(input("quel est le volume de l'article acheté"))
price = input("quel est le prix de votre article?")
tva = input("quel est le pourcentage de la tva?")
frport = input("Veuillez renseigner le pourcentage des frais de port")
douane = input("quel est le prix des droits de douane")
tva, frport, douane, price = percent(tva), percent(frport), percent(douane), percent(price)
tva, frport, douane = fpercent(tva), fpercent(frport), fpercent(douane)
htaxe = price * volume
tvaf = douanef = frportf = 0
tvaf = calc(htaxe, tva, tvaf)
frportf = calc(htaxe, frport, frportf)
douanef = calc(htaxe, douane, douanef)
taxe = tvaf + frportf + douanef
ataxe = htaxe + taxe
print(100* "\n")
print(f"Votre article au prix de {price}eu avec un volume de {volume} sera au prix de {htaxe}eu hors taxes contre {ataxe}eu taxes comprises")
