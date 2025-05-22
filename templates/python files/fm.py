import numpy as np
import matplotlib.pyplot as plt

def modulacion_fm(fc,fm,beta,duracion,fs):
    t=np.linspace(0,duracion,int(fs*duracion)) 
    mensaje=np.sin(2*np.pi* fm*t) #Señal moduladora
    portadora=np.cos(2*np.pi* fc*t+beta*np.sin(2*np.pi*fm*t))
    moduladora=np.cos(2*np.pi* fc*t)
    fm_senal=1+(mensaje)*portadora
    return t, mensaje,portadora,moduladora,fm_senal

    


fc=1000  #fercuencia de la señal portadora
fm=100  #frecuencia de la señal portadora
beta=5  #indice de modulacion
duracion=0.02
fs= 100000    #frecuencia de muestreo en HZ

#vamos a generar la señal portadora
t, mensaje, portadora,moduladora,fm_senal= modulacion_fm(fc,fm,beta,duracion,fs)

# Vamos a graficar las señales
plt.figure(figsize=(10,6))
plt.subplot(4,1,1)
plt.plot(t, mensaje, label="Señal moduladora (Message) ", color="red")
plt.title("Señal mensaje")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")

plt.subplot(4,1,2)
plt.plot(t, portadora, label="Señal FM")
plt.title("Señal portadora")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")


plt.subplot(4,1,3)
plt.plot(t, fm_senal, label="Señal FM",color="c")
plt.title("Señal modulada en fm")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")

plt.subplot(4,1,4)
plt.plot(t, portadora, label="Señal FM",linestyle="dashdot")
plt.title("Señal portadora")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")

plt.subplot(4,1,4)
plt.plot(t, mensaje, label="Señal FM",linestyle="--")
plt.title("Señal moduladora y mensaje")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()