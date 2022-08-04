print("|------------------------------------------|")
print("|Bienvenidos al conversor, elija un numero |")
print("|- 1=Euro, 2=Dolar, 3=Won, 4=Rupia, 5=Yen -|")
print("|------------------------------------------|")
Moneda=int(input("Elija el tipo de moneda: "))
if Moneda==1:
    N1=float(input("Introduzca su Cantidad a convertir = "))
    Do=1.02
    Won=1335.79
    Ru=81.15
    Yen=136.29
    Result1=N1*Do
    Result2=N1*Won
    Result3=N1*Ru
    Result4=N1*Yen
    print("Tu conversion a otras monedas es:")
    print("Tu conversion a Dolar es = ",Result1)
    print("Tu conversion a Won es = ",Result2)
    print("Tu conversion a Rupia es = ",Result3)
    print("Tu conversion a Yen es = ",Result4)
if Moneda==2:
    N1=float(input("Introduzca su Cantidad a convertir = "))
    Euro=0.98
    Won=1302.03
    Ru=79.16
    Yen=132.93
    Result1=N1*Euro
    Result2=N1*Won
    Result3=N1*Ru
    Result4=N1*Yen
    print("Tu conversion a otras monedas es:")
    print("Tu conversion a Euro es = ",Result1)
    print("Tu conversion a Won es = ",Result2)
    print("Tu conversion a Rupia es = ",Result3)
    print("Tu conversion a Yen es = ",Result4)
if Moneda==3:
    N1=float(input("Introduzca su Cantidad a convertir = "))
    Euro=0.00075
    Do=0.00077
    Ru=0.061
    Yen=0.10
    Result1=N1*Euro
    Result2=N1*Do
    Result3=N1*Ru
    Result4=N1*Yen
    print("Tu conversion a otras monedas es:")
    print("Tu conversion a Euro es = ",Result1)
    print("Tu conversion a Dolar es = ",Result2)
    print("Tu conversion a Rupia es = ",Result3)
    print("Tu conversion a Yen es = ",Result4)
if Moneda==4:
    N1=float(input("Introduzca su Cantidad a convertir = "))
    Euro=0.012
    Do=0.013
    Won=16.46
    Yen=1.68
    Result1=N1*Euro
    Result2=N1*Do
    Result3=N1*Won
    Result4=N1*Yen
    print("Tu conversion a otras monedas es:")
    print("Tu conversion a Euro es = ",Result1)
    print("Tu conversion a Dolar es = ",Result2)
    print("Tu conversion a Won es = ",Result3)
    print("Tu conversion a Yen es = ",Result4)
if Moneda==5:
    N1=float(input("Introduzca su Cantidad a convertir = "))
    Euro=0.0073
    Do=0.0075
    Won=9.81
    Ru=0.60
    Result1=N1*Euro
    Result2=N1*Do
    Result3=N1*Won
    Result4=N1*Ru
    print("Tu conversion a otras monedas es:")
    print("Tu conversion a Euro es = ",Result1)
    print("Tu conversion a Dolar es = ",Result2)
    print("Tu conversion a Won es = ",Result3)
    print("Tu conversion a Rupia es = ",Result4)