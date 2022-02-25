print("Que palabra, frase o número quieres comprobar para ver si es un palíndromo?")
dato=input()
def preparacion_palabra():
  i,j = "áéíóúñÁÉÍÓÚÑ" , "aeiounAEIOUN"
  acento=str.maketrans(i,j)
  dato=dato.translate(acento)
  dato=dato.lower() #Se transforma todo en minúsculas
  dato=dato.replace(" ", "") #Se quitan los espacios para que sea más sencillo

