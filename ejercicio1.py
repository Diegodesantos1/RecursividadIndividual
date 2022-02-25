import sys

lista_palabra=["Alien","Eduardo","Cabeza"]
print(lista_palabra)
print("Establece el intervalo inferior de búsqueda")
intervalo_inf=int(input())
print("Establece el intervalo superior de búsqueda")
intervalo_sup=int(input())
if intervalo_inf > intervalo_sup or intervalo_inf == 0:
  print("No se puede realizar la búsqueda")
  sys.exit
else:
  print("Qué palabra quieres buscar?")
  palabra_buscar=str(input())
  numero_medio= intervalo_sup//intervalo_inf
  def dicotomia():
    numero_medio =-1
    palabra_tabla =lista_palabra.index("palabra_buscar")
    if palabra_tabla == palabra_buscar:
      print(f"La palabra es {palabra_buscar}")
    else:
      dicotomia()

dicotomia()
    
    
    