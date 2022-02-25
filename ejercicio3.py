bandera =["R","B","B","R","G","B","B","R","B","R","R","G","R","R","B","G","G"]
print(bandera)
def ordenar_bandera():
  rojo=[]
  verde=[]
  azul =[]
  if bandera.index("R"):
    color=bandera.pop(1)
    rojo.append(color)
    print(rojo)
    ordenar_bandera()
  elif bandera.index("G"):
    color=bandera.pop(1)
    verde.append(color)
    print(verde)
    ordenar_bandera()
  elif bandera.index("B"):
    color=bandera.pop(1)
    azul.append(color)
    print(azul)
    ordenar_bandera()
  else:
    bandera_ordenada=(rojo + verde + azul)
    print(bandera_ordenada)
ordenar_bandera()
    
    