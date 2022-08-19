# Metodos para las listas
def listasm():
  lista = [123,456,789,321,654,987]
  #cuanta el numero de beses que se enecuenta "(busqueda) en la lista"
  print(lista.count(123))
  #insert nos ayuda a incertar un balo en la posision que deceemos
  lista.insert(1,'audifonos')
  lista.insert(0,'compus')
  print(lista)
  #nos permite eliminar elemtos en nustra lista con el indice
  lista.pop(2)
  #nos permite eliminar elemtos en nustra lista con el valor
  lista.remove("compus")
  # nos permite ordenar nuestra lista
  lista.sort(reverse = True)
  print(lista)
  #nos permite darle buelta los datos
  lista.reverse()
  print(lista)
  #tuplas
  semestre = (321,654,987,123,456,789)
  tupla = ("emtech",)
  print (tupla)
  #tuplas vasia es necesaria
  tupla_vacia = tuple()
  enero = ("computadoras",1850)
  print ("productos: ", enero[0])
  print ("totales exportadas: ", enero[1])
  valores = (1,2,3,2,1,2,3)
  print(valores.count(2))
  #conjuntos
  #declaracion de conjunto con asicnacion de losta o tupla
  conjunto = set(lista)
  #declaracion de conjunto desde asicnacion de datos
  conjunto_exp = {123,456,789,321,654,987,321}
  #para agregar datos aun conjunto
  conjunto.add('hola')
  print(conjunto)
  #eliminar aleatoreo se usa .pop
    #conjunto.pop()
  #eliminar con seleccion
    #conjunto.remove("123")
  # es para optener los elementos que no se encuentran en un top
  diferencia = conjunto.difference(lista)
  print (diferencia)
  # para sacar la interccescion se encuentran en ambos conjuntos