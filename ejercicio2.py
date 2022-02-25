print("Que palabra, frase o número quieres comprobar para ver si es un palíndromo?")
dato=input()

i,j = "áéíóúñÁÉÍÓÚÑ" , "aeiounAEIOUN"
acento=str.maketrans(i,j)
dato=dato.translate(acento)
dato=dato.lower() #Se transforma todo en minúsculas
dato=dato.replace(" ", "") #Se quitan los espacios para que sea más sencillo
lista = list(dato)
listafinal= list(reversed(dato))
def comprobar_palindromo():
  if len(dato) < 1:
    print("Es un palíndromo") #Caso para una sola letra o número
  else:
    if dato[0] == dato [-1]:
      print(comprobar_palindromo(dato[1:-1]))
    else:
      print(f"{dato} no es un palíndromo")
comprobar_palindromo()

