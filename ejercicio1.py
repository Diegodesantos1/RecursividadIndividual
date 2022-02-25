import sys

lista_palabra=["Alien","Eduardo","Cabeza","Rubén"]
print(lista_palabra)
intervalo_inf=0
intervalo_sup=len(lista_palabra)
numero_medio=(intervalo_sup+intervalo_inf)// 2
print(numero_medio)
print("Qué palabra quieres buscar?")
palabra_buscar=str(input())
def dicotomia():
  numero_tabla =lista_palabra.index(palabra_buscar)
  if numero_tabla == numero_medio:
    print(f"La palabra es {palabra_buscar}")


dicotomia()
    
    
    