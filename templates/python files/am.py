import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)#Definimos tiempos etre 0 y 1 con 1000 muestras

fc = 50 # Frecuency carry portadora
fm = 5 # Frecuency Moduladora
Ac = 1 # Amplitud de la Partadora
Am = 0.5 # Amplitud de las moduladora

#Señal portadora

carrier = Ac * np.cos(2 * np.pi * fc * t )

#Señal Moduladora

moduladora = Am *  np.cos(2 * np.pi * fm * t )

#Señal Modulada por amlitud (AM)

am_signal = (1 + moduladora) * carrier

#Graficar las señales

plt.subplot(3, 1, 2)
plt.plot(t, carrier, label="Portadora", color = 'r')
plt.title("Señal Portadora")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

#Grafica Moduladora
plt.subplot(3, 1, 1)
plt.plot(t, moduladora, label="Moduladora", color = 'b')
plt.title("Señal Moduladora")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

#Grafica para la señal Modulada en Amplitud
plt.subplot(3, 1, 3)
plt.plot(t, am_signal, label="Amplitud Modulada", color = 'g')
plt.title("Seña Modulada por Amplitud")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()