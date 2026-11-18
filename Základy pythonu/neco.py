a = int(input("Zadejte cislo 1 "))
b = int(input("Zadejte cislo 2 "))

while not(a == 0 or b == 0):
    if a > b:
        c = a//b
        a = a -(b * c)