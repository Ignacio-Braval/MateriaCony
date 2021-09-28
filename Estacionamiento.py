print("Hola bienvenidos al sistema de estacionamientos".center(50, '*'))
print("")
print("Datos a considerar".center(50, '*'))
print("")
print("El 50 porciento del total de vehiculos estuvo 2,5 horas, el 35 porciento estuvo 3,2, el 10 porciento estuvo 1,45 y el 10 porciento solo 1 hora")
print("")

def calculoEstacionamiento():
    vehiculos = int(input("Ingrese el total de vehiculos estacionados: "))
    vehiculos50= (50*vehiculos) / 100
    vehiculos35= (35*vehiculos) / 100
    vehiculos10= (10*vehiculos) / 100
    vehiculos5=  (5*vehiculos)  / 100

    vehiculos50total= vehiculos50*2500
    vehiculos35total= vehiculos35*2332
    vehiculos10total= vehiculos10*1448
    vehiculos5total= vehiculos5*1000

    gananciastotalesxdia= vehiculos50total + vehiculos35total + vehiculos10total + vehiculos5total
    print("Sus ganacias totales equivalen a: ","$", gananciastotalesxdia)

calculoEstacionamiento()
