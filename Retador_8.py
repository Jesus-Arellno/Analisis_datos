#base de datos precargada
Clientes = {
  '45471':['Luis perez',45,'BJX',True],
  '8944411':['Fernanda Garcia',25,'JAL',True],
  '15223':['Alejandara ortiz',33,'JDL',True]
}
#Funcion para Agregar Clientes
def AddClientes():
  while True:
    ID = input(" Ingresa el ID de su INE/IFE: ")
    Nombre = input(" Ingrese su nombre: ")
    Edad = input(" Ingrese su edad: ")
    Destino = input(" Ingrese su Destino: ")
    Cliente_vip = input(" Cliente VIP Si/No: ")
    exit = input(" pres X para salir: ")
    print("")
    Clientes[ID] = [Nombre,Edad,Destino,Cliente_vip == 'si' if True else False]
    if exit == 'x' or exit == 'X':
      break
  print(" ")
#Funcion para Eliminar a un cliente
def RemoveClientes():
  while True:
    print(" Bienbenido cual es el cliente que deceea eliminar ")
    Dato = input(" Inserte Id que decea eliminar ")
    Clientes.pop(Dato)
    ext = input(" Decea eliminar otro cliente s/n: ")
    if ext == "n" or ext == "N":
      break
  print(" ")
#Funcion para calcular la edad promedio de nuestros clientes
def EdadPromedio():
  contador = 0
  Edades = 0
  ProEdad = 0
  for key, datos in Clientes.items():
    Edades += datos[1]
    contador += 1 
  ProEdad = (Edades/contador)
  print(" La Edad promedio de nuestros Clientes es de: ",ProEdad)
  print(" ")
#funcion solo para mostara los nombres de uestros vclientes
def MostarClientes():
  print("Nuestros Clientes son: ")
  for key in Clientes:
    print(" ",Clientes[key][0])
  print(" ")
#funcion principal donde se mandan llmar las demas funciones
def Reto8():
  Selct = " "
  print("Bienbenido al egercicio retador #8")
  while True:
    print(" Accion que decea realisar ")
    print("  Agregar Clientes:  #1 ")
    print("  Eliminar Clientes: #2 ")
    print("  Edad Promedio:     #3 ")
    print("  Lista de clientes: #4 ")
    Selct = input(" Inserte su opcion o x para salir ")
    print(" ")
    if Selct == "1":
      AddClientes()
    elif Selct == "2":
      RemoveClientes()
    elif Selct == "3":
      EdadPromedio()
    elif Selct == "4":
      MostarClientes()
    elif Selct == "x" or Selct == "X":
      break
    else:
      print(" Inserte una opcion valida ")