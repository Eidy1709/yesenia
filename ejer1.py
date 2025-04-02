#crear lista para almacennar las ventas de la semana
ventas=[]

# usar un ciclo for para pedir las ventas de cada dia
for i in range(7):  # 7 dias de la semana
    # usar input para pedir la venta del dia
    venta_dia = float(input(f"Ingrese la venta del dia {i+1}:"))
    # agregar la venta a la lista de ventas
    ventas.append(venta_dia)

# procesar los datos
total_ventas = sum(ventas)
print(total_ventas)
promedio_ventas = total_ventas / len(ventas)

# condicion para verificar si se alcanzo la meta
meta = 5000

if total_ventas >= meta:
    mensaje = "Felicidades haz alcanzado la meta"
else:
    mensaje = "no se alcanzo la meta"

# imprimir el resultado


print(f"Total de ventas: ${total_ventas}")
print(f"Promedio $:{promedio_ventas}")
print(mensaje)