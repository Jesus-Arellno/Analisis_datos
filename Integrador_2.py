from dict_aeropuertos import datos
import operator
airport = []
state = datos['Estado']
city = datos['Ciudad']
codes = datos['Codigo_IATA']
totalpasageros = datos['Pasajeros']
totalVuelos = datos['Vuelos_Sinaloa']

maxpasajeros = []
vuelosmenores = {}

def Dta_organize():
  for Q in range(0,len(state)):
    airport.append({Q:[state[Q],city[Q],codes[Q],totalpasageros[Q],totalVuelos[Q]]})

#no escribe nada
def MaxPasageros():
  index = 0
  temporary = []
  for aeropuerto in airport:
    temporary.append(aeropuerto[index][3])
    index += 1
  index = 0
  for Q in range(0,5):
    
    maxpasaje = max(temporary)
    for all in temporary:
      if maxpasaje == all:
        maxpasajeros.append(maxpasaje) 
        temporary.pop(temporary.index(maxpasaje))
  print("Los 5 aeropuestos con mas mayor cantidad de pasajeros que viajan asinaloa son: ")
  for cox in maxpasajeros:
    print(airport[totalpasageros.index(cox)])
  print("")
def PasajerosPromedio():
  index = 0
  Promedio = 0
  temp = 0
  for aeropuerto in airport:
    index += 1
    temp += int(aeropuerto[index-1][3])
  Promedio = int(temp / index)
  print("El promedio de pasajeros en todos los aeropuertos es de : "+str(Promedio)+" pasajeros ")
  print(" ")

def minVuelo():
  index = 0
  temporary = {}
  for aeropuerto in airport:
    index += 1
    if aeropuerto[index-1][4] !=0:
      temporary[index - 1] = aeropuerto[index -1][4]
  for Q in range(0,5):
    minvuelos = min(temporary.items(),key=operator.itemgetter(1))
    vuelosmenores[minvuelos[0]] = minvuelos[1]
    temporary.pop(minvuelos[0])
  print("los 5 aeropuertos con menores vuelos a sinaloa son: ")
  for n in vuelosmenores:
    print(airport[n])
  print(" ")
def General ():
  for Q in vuelosmenores:
    maxpasajeros.append(airport[Q][Q][3])
  index = 0
  promedio = 0
  for contado in maxpasajeros:
    index += 1
    promedio += int(contado)
  promedio = int(promedio/ index)
  print("Promdeio de pasajeros obtenidos de los puntos 1 & 3:  "+str(promedio)+" pasajeros")
    
def Integer2 ():
  print("Bienbenido al egercicio integrador #2")
  Dta_organize()
  MaxPasageros()
  PasajerosPromedio()
  minVuelo()
  General()