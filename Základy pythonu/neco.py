# Váš kód sem 👇
dalnice = 130
mimo_obec = 90
obec = 50

X = "OK"
Y = "Vysoká rychlost"
Z = "Martin je cokl posrany"

pos = input ("Kde se nacházíte?")
vel = int (input ("Jak rychle jedete?"))

if pos == "obec":
    if vel <= obec:
        print (X)
    else:
        print(Y)

elif pos == "mimo obec":
    if vel <= mimo_obec:
        print (X)
    else:
        print(Y)

elif pos == "dalnice":
    if vel <= dalnice:
        print (Z)
    else:
        print(Z)
D