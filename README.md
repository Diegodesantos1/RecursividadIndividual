<h1 align="center">Ejercicios de Recursividad Individual</h1>

*He usado la herramienta de Replit para poder programar online y así resolver los ejercicios propuestos aplicando el contenido de esta lección, que es la* **Recursividad**.

***

<h2>Repositorio</h2>

Este es el link del [Repositorio](https://github.com/Diegodesantos1/RecursividadIndividual)

***

## Ejercicio 1: Búsqueda por dicotomía en una tabla ordenada

Aquí su [Milestone](https://github.com/Diegodesantos1/RecursividadIndividual/milestone/1?closed=1)

El código empleado para resolverlo es el siguiente:

```python
lista_palabra=["Alien","Eduardo","Cabeza","Rubén","Javier","Atlas","Río", "Servir", 
"Abrir","Camión", "Ordenador", "Mandaloriano", "Conflicto", "Móvil", "Estambul","Wifi", 
"Nft", "Real Madrid","Dicotomía","Gafas", "Pesado", "Bicicleta","Reloj", "Abrigo",
"Criptoestafa", "Emblemático","Inanición","Comunicación","Ifema","Spa","Auditorio",
"Campo", "Bernabéu", "Iluminati", "Copiar", "Libre", "Como", "El", "Mar"]
print(lista_palabra)
cota_sup=len(lista_palabra)
numero_medio=(cota_sup)// 2
print("¿Qué palabra quieres buscar?")
palabra_buscar=str(input())
def dicotomia(numero_medio):
  numero_tabla =lista_palabra.index(palabra_buscar)
  if numero_tabla == numero_medio:
    print(f"La palabra {palabra_buscar} se encuentra en el índice {numero_tabla}")
  elif numero_tabla < numero_medio:
    dicotomia(numero_medio-1)
  elif numero_tabla > numero_medio:
    dicotomia(numero_medio+1)
dicotomia(numero_medio)
```

## Ejercicio 2: Análisis de una cadena de caracteres

Aquí su [Milestone](https://github.com/Diegodesantos1/RecursividadIndividual/milestone/3?closed=1)

El código empleado para resolverlo es el siguiente:
```python
print("¿Que palabra, frase o número quieres comprobar para ver si es un palíndromo?")
dato=input()

i,j = "áéíóúñÁÉÍÓÚÑ" , "aeiounAEIOUN"
acento=str.maketrans(i,j)
dato=dato.translate(acento)
dato=dato.lower() #Se transforma todo en minúsculas
dato=dato.replace(" ", "") #Se quitan los espacios para que sea más sencillo
lista = list(dato)
listafinal= list(reversed(dato))
def comprobar_palindromo(dato):
  if len(dato) < 1:
    print(f"La palabra o número {dato} es un palíndromo") #Caso para una sola letra o número
  else:
    if dato[0] == dato [-1]:
      comprobar_palindromo(dato[1:-1])
    else:
      print(f"La palabra o número {dato} no es un palíndromo")
comprobar_palindromo(dato)
```
