def Reto7():
  print("Bienbenido al egercicio retador #7")

  Clientes = {}
  Seleccion = " "
  N = 0
  #ciclo para impreccion y seleccion
  while True:
    #imprecion del menu
    print(" FlyUs-México MENU ")
    print(" Añador Cliente              #1 ")
    print(" Listar Clientes             #2 ")
    print(" Listar clientes Preferentes #3 ")
    print(" Salir                       #4 ")
    #seleccion de opcion
    Seleccion = input(" Dijite una opcion: ")
    print()
    #comparacion de opcion
    if Seleccion == '1':
      #llenado de diccionario
      ID = input(" Ingresa el ID de su INE/IFE: ")
      Nombre = input(" Ingrese su nombre: ")
      Edad = input(" Ingrese su edad: ")
      Destino = input(" Ingrese su Destino: ")
      Cliente_vip = input(" Cliente VIP Si/No: ")
      print(" ")
      #asicnacion de  true o false vip
      Clientes[ID] = [Nombre,Edad,Destino,Cliente_vip == 'si' if True else False]
      
    elif Seleccion == '2':
      for customers in Clientes.items():
        print(customers)
        print(" ")
    elif Seleccion == '3':
      print(" Lista de clientes preferentes: ")
      for customers, datos in Clientes.items():
        if datos[3]:
          print("  ",N,"#"," ",datos)
          N += 1
    elif Seleccion == '4':
      print(" Asta pronto: ")
      break
    else:
      print("Disculpe esta opcion no esta en nuestro menu")
    