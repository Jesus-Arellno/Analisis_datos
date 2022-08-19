# Bienbenido al ejercicio retardor numero #6
def Reto6():
  print("hola este es el ejerccio retador numero #6")
  # vareable y areglos necesareos
  nombre = " "
  edad = " "
  destino = " "
  pasajeros = []
  BXJ = 0
  GDL = 0
  JAL = 0
  edadpromediobxj = 0
  edadpromediogdl = 0
  edadpromediojal = 0
  DetallesVuelos = []
  edadespromedio = []
  BXJL = []
  GDLL = []
  JALL = []
  BXJD = ()
  GDLD = ()
  JALD = ()
  epbxj = []
  epgdl = []
  epjal = []
  epbxjt = ()
  epgdlt = ()
  epjalt = ()
  
  
  # recoleccion de datos
  while True:
      print(" Bienbenido a FlyUs-México para salir presiona la letra 'X' ")
      nombre = input("Nombre: ")
      if nombre.upper() != 'X':
          edad = input(" Edad: ")
          destino = input(" Destino: ")
          pasajeros.append((nombre.upper(), edad, destino.upper()))
      else:
          break
  #
  for viajero in pasajeros:
    if viajero[2] == 'BXJ':
      BXJ += 1
      edadpromediobxj += int(viajero[1])
      edadpromediobxj = edadpromediobxj / BXJ
    elif viajero[2] == 'GDL':
      GDL += 1
      edadpromediogdl += int(viajero[1])
      edadpromediogdl = edadpromediogdl / GDL
    elif viajero[2] == 'JAL':
      JAL += 1
      edadpromediojal += int(viajero[1])
      edadpromediojal = edadpromediojal / JAL
      
  BXJL.insert(0,"BXJ")
  BXJL.insert(1,BXJ)
  GDLL.insert(0,"GDL")
  GDLL.insert(1,GDL)
  JALL.insert(0,"JAL")
  JALL.insert(1,JAL)
  BXJD = BXJL
  GDLD = GDLL
  JALD = JALL
  epbxj.insert(0,"BXJ"),epbxj.insert(1,edadpromediobxj)
  epgdl.insert(0,"GDl"),epgdl.insert(1,edadpromediogdl)
  epjal.insert(0,"JAL"),epjal.insert(1,edadpromediojal)
  epbxjt = epbxj
  epgdlt = epgdl
  epjalt = epjal
  edadespromedio.insert(0,epbxjt)
  edadespromedio.insert(1,epgdlt)
  edadespromedio.insert(2,epjalt)
  if BXJ > GDL and BXJ > JAL:
    DetallesVuelos.insert(0,BXJD)
    DetallesVuelos.insert(1,GDLD)
    DetallesVuelos.insert(2,JALD)
  elif GDL > BXJ and GDL > JAL:
    DetallesVuelos.insert(1,BXJD)
    DetallesVuelos.insert(0,GDLD)
    DetallesVuelos.insert(2,JALD)
  elif JAL > BXJ and JAL > GDL:
    DetallesVuelos.insert(2,BXJD)
    DetallesVuelos.insert(1,GDLD)
    DetallesVuelos.insert(0,JALD)
  else:
    DetallesVuelos.insert(0,BXJD)
    DetallesVuelos.insert(1,GDLD)
    DetallesVuelos.insert(2,JALD)

  print("A) Detalles de Vuelos: ",DetallesVuelos)
  print("B) Edades promedio por vuelo: ",edadespromedio)