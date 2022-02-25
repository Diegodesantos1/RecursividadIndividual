import sys

lista_palabra=["Alien","Eduardo","Cabeza","Rubén"]
print(lista_palabra)
intervalo_inf=0
intervalo_sup=len(lista_palabra)
numero_medio=(intervalo_sup+intervalo_inf)// 2
print("Qué palabra quieres buscar?")
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
    
    
    