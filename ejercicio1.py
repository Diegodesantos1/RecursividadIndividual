import sys
def tabla():
  lista_palabra=["Alien","Eduardo","Cabeza", 5,"Rusia","Avión", 3,"Mascarilla","Algoritmo","Logaritmo", 12,"Integral","Naranja","Martín","Juan","Leonardo","Javier","Estados Unidos"]
  print(lista_palabra)
tabla()

print("Establece el intervalo inferior de búsqueda")
intervalo_inf=int(input())
print("Establece el intervalo superior de búsqueda")
intervalo_sup=int(input())
if intervalo_inf >= intervalo_sup:
  print("No se puede realizar la búsqueda")
  sys.exit
else:
  print("Qué palabra quieres buscar?")
  palabra_buscar=str(input())
  numero_medio= intervalo_sup//intervalo_inf
def dicotomia():
  numero_medio =-1
  if lista_palabras[numero_medio] == palabra:
    print(f"La palabra es {palabra_buscar}")
  else:
    dicotomia()
    
dicotomia()
    
    
    