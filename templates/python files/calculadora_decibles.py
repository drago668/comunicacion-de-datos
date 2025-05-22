import math

def db_watts(num):
    return 10**(num/10)

def watts_db(num):
    return 10*math.log10(num) 


num=float(input("Ingresa la potencia de entrada: "))
num=watts_db(num)
num_ganancias=int(input("Ingresa la cantidad de ganacias o atenuaciones: "))

contador=num
for i in range(num_ganancias):
    contador+=float(input("Ingresa la atenuacion o ganancia "))
print(f"La potencia de salida es {contador} dB")
print(f"La potencia de salida es {db_watts(contador)} watts")