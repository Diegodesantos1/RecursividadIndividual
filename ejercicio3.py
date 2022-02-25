bandera =["R","B","B","R","G","B","B","R","B","R","R","G","R","R","B","G","G"]
print(bandera)
rojo=[]
verde=[]
azul =[]
def ordenar_bandera(bandera):
  if len(bandera) > 0:
    color=bandera.pop(0)
    if color =="R":
      rojo.append(color)
      ordenar_bandera(bandera)
    elif color =="G":
      verde.append(color)
      ordenar_bandera(bandera)
    elif color =="B":
      azul.append(color)
      ordenar_bandera(bandera)
    else:
      bandera_ordenada=rojo+verde+azul
      print(f"La bandera ordenada es {bandera_ordenada}")
  else:
      bandera_ordenada=rojo+verde+azul
      print(f"La bandera ordenada es {bandera_ordenada}")
ordenar_bandera(bandera)
    
    