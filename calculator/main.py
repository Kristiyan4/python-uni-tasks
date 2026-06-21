import kalkulator as k
a = float(input("Vuvedete chislo: "))
b = float(input("Vuvedete chislo: "))
deistvie = input("Vuvedete deistvieto: ")
if deistvie=="Subirane":
    k.subirane(a,b)
elif deistvie =="Izvajdane":
    k.izvajdane(a,b)
elif deistvie =="Umnojenie":
    k.umnojenie(a,b)
elif deistvie == "Delenie":
    k.delene(a,b)
else:
    print("Greshna informaciq")