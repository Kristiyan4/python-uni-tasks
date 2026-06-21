import formuli as f
figura = input("Vuvedi geometrichnata figura: ")
if figura =="Triugulnik":
    figure = f.Triugulnik()
elif figura == "Kvadrat":
    figure = f.Kvadrat()
elif figura == "Pravougulnik":
    figure = f.Pravougulnik()
elif figura == "Romb":
    figure = f.Romb()
elif figura == "Trapec":
    figure = f.Trapec()
else: 
    print("Greshno vuvedeni danni!")