vek = int(input("Zadej svuj vek: "))

if vek >= 18 and vek <= 99:
    print("jsi dospely")
elif vek >= 15 and vek <= 17:
    print("jsi dospivajici")
elif vek >= 0 and vek <= 14:
    print("jsi dite")
else:
    print("neplatny vek")