bandera =["R","B","B","R","G","B","B","R","B","R","R","G","R","R","B","G","G"]
print(bandera)
def ordenar_bandera():
  rojo=[]
  verde=[]
  azul =[]
  color=bandera.pop(0)
  if color =="R":
    rojo.append(color)
  elif color =="G":
    verde.append(color)
  elif color =="B":
    azul.append(color)
  else:
    print(bandera_ordenada)
ordenar_bandera()
    
    