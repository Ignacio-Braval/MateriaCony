def elecciones1():
 votos_diego = 0
 votos_sandro = 0
 votos_luis = 0
 
 x = 5
 total = 0
 ganador = ""
 
 while x != "0":
  
  print ("SISTEMA DE ELECCIONES")
  print ("")
  print ("Seleccione el numero de candidato a votar, para salir digite 0")
  print ("")
  print ("1)Diego Caraballo")
  print ("2)Sandro Cruz")
  print ("3)Luis Perez")
  print ("")
  x = input("A quien vas a votar: ")
  print ("")
  if x == "1" or x == "2" or x == "3":
   total += 1
  
  
  if x != "0" and x != "1" and x != "2" and x !="3":
   print ("Opcion no valida, intete de nuevo...")
   time.sleep(1)
  elif x == "1":
   votos_diego += 1
  elif x == "2":
   votos_sandro += 1
  elif x == "3":
   votos_luis += 1

 
 if total == 0:
  print ("No hubieron votos...")
  print ("")
  time.sleep(2)
  return 0
 else:
  porcen_diego = float(100 * votos_diego) / float (total)
  porcen_sandro = float(100 * votos_sandro) / float (total)
  porcen_luis = float(100 * votos_luis) / float (total)
  
  if votos_diego > votos_sandro and votos_diego > votos_luis:
   ganador = "El ganador fue Diego Caraballo"  
  elif votos_sandro > votos_diego and votos_sandro > votos_luis:
   ganador = "El ganador fue Sandro Cruz"
  elif votos_luis > votos_diego and votos_luis > votos_sandro:
   ganador = "El ganador fue Luis Perez"
  elif votos_luis == votos_diego and votos_luis == votos_sandro:
   ganador = "Hubo un triple empate"
  elif votos_diego == votos_sandro and votos_diego > votos_luis:
   ganador = "Hubo un doble empate entre Diego Caraballo y Sandro Cruz"
  elif votos_sandro == votos_luis and votos_sandro > votos_diego:
   ganador = "Hubo un doble empate entre Sandro Cruz y Luis Perez"
  elif votos_luis == votos_diego and votos_luis > votos_sandro:
   ganador = "Hubo un doble empate entre Luis Perez y Diego Caraballo"
 
 print ("Cantidad de votos: ", total)
 print ("")
 print ("Cantidad de votos para Diego Caraballo: ", votos_diego, "--> %.2f" % porcen_diego + "%")
 print ("")
 print ("Cantidad de votos para Sandro Cruz: ", votos_sandro, "--> %.2f" % porcen_sandro + "%")
 print ("")
 print ("Cantidad de votos para Luis Perez: ", votos_luis, "--> %.2f" % porcen_luis + "%")
 print ("")
 print (ganador)
 print ("")
 
elecciones1()
