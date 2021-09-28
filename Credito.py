import os, math

print("*Bienvenido al sistema de calculo de tu credito*")
print("")
print("Datos a tomar en cuenta:")
print("")
print("Semestres totales = 12 0 16")
print("")
print("Arancel referencial de tu carrera = $2.000.000 CLP")
print("")
print("Arancel real de la carrera = $4.000.000 CLP")

MontoCredito = 2000000
TasaInteresSimple = float(3.5)
TasaInteresCompuesto = float(2.0)
arancelreal = 4000000
ValorCom6 = 0
ValorCom8 = 0
ValoraPagar6 = 0
ValoraPagar8 = 0

print("1)Interes Simple")
print("2)Interes Compuesto")
print("3)Ambas simulaciones")
OpcionCredito = input("Cual sera tu eleccion de credito: ")

if OpcionCredito == "1":

   formulaSimple6 = (MontoCredito + TasaInteresSimple + 6 )/ 100
   MontoFinalSimple6 = formulaSimple6 + MontoCredito
   ValoraPagar6= int(MontoFinalSimple6 - arancelreal * 6)
   formulaSimple8 = (MontoCredito + TasaInteresSimple + 8 )/ 100
   MontoFinalSimple8 = formulaSimple8 + MontoCredito
   ValoraPagar8 = int(MontoFinalSimple8 - arancelreal * 8)

if OpcionCredito == "2":

   formulaCompuesto6=math.pow(1.0+TasaInteresCompuesto/100,6)*MontoCredito
   formulaCompuesto8=math.pow(1.0+TasaInteresCompuesto/100,8)*MontoCredito
   interesCompuesto6 = formulaCompuesto6 - MontoCredito
   interescompuesto8 = formulaCompuesto8 - MontoCredito
   ValorCom6 = int(interesCompuesto6 - arancelreal * 6)
   ValorCom8 = int(interescompuesto8 - arancelreal * 8)

if OpcionCredito == "3":

   formulaSimple6 = (MontoCredito + TasaInteresSimple + 6 )/ 100
   MontoFinalSimple6 = formulaSimple6 + MontoCredito
   ValoraPagar6= int(MontoFinalSimple6 - arancelreal * 6)
   formulaSimple8 = (MontoCredito + TasaInteresSimple + 8 )/ 100
   MontoFinalSimple8 = formulaSimple8 + MontoCredito
   ValoraPagar8 = int(MontoFinalSimple8 - arancelreal * 8)

   formulaCompuesto6=math.pow(1.0+TasaInteresCompuesto/100,6)*MontoCredito
   formulaCompuesto8=math.pow(1.0+TasaInteresCompuesto/100,8)*MontoCredito
   interesCompuesto6 = formulaCompuesto6 - MontoCredito
   interescompuesto8 = formulaCompuesto8 - MontoCredito
   ValorCom6 = int(interesCompuesto6 - arancelreal * 6)
   ValorCom8 = int(interescompuesto8 - arancelreal * 8)

else:
   print('Debe seleccionar una opcion valida!!!')

print("*El calculo final es*")
print("")
print("Credito con intereses simple a 6 años de carrera universitaria: ")
print(abs(ValoraPagar6))
print("")
print("Credito con intereses simple a 8 años de carrera universitaria: ")
print(abs(ValoraPagar8))
print("")
print("Credito con intereses compuesto a 6 años de carrera universitaria: ")
print(abs(ValorCom6))
print("")
print("Credito con intereses compuesto a 8 años de carrera universitaria: ")
print(abs(ValorCom8))
print("")





