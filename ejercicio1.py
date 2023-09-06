productos = {'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input("¿Qué fruta quieres? ").title()
cantidad = int(input("Cuanto quieres? "))
if fruta in productos:
    print("{0} de {1} cuestan {2}$".format(cantidad, fruta, round(productos[fruta] * cantidad, 2)))
else: 
    print("Lo siento, la fruta {0} no está disponible.".format(fruta))