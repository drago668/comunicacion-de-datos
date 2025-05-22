import numpy as np
import matplotlib.pyplot as plt
# Desarrollado por Daniel Esteban Rivera Gomez

# Parámetros básicos
fs = 10000  
t = np.linspace(0, 1, fs)  
f_message = 5  
f_carrier = 50  

# Señal de mensaje
message_signal = np.sin(2 * np.pi * f_message * t)

# Modulación AM
am_signal = (1 + message_signal) * np.cos(2 * np.pi * f_carrier * t)

# Modulación FM
kf = 75  
fm_signal = np.cos(2 * np.pi * f_carrier * t + kf * np.cumsum(message_signal) / fs)

# Modulación FSK
f1 = 30  #
f0 = 20  
binary_sequence = np.tile([1, 0], len(t) // 2)  # Secuencia binaria 101010...
fsk_signal = np.cos(2 * np.pi * (f1 * binary_sequence + f0 * (1 - binary_sequence)) * t)

# Gráficos
plt.figure(figsize=(12, 10))

# Señal de mensaje
plt.subplot(4, 1, 1)
plt.plot(t, message_signal, label="Señal de Mensaje")
plt.title("Señal de Mensaje")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()

# Señal AM
plt.subplot(4, 1, 2)
plt.plot(t, am_signal, label="Señal AM", color="orange")
plt.title("Modulación en Amplitud (AM)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()

# Señal FM
plt.subplot(4, 1, 3)
plt.plot(t, fm_signal, label="Señal FM", color="green")
plt.title("Modulación en Frecuencia (FM)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()

# Señal FSK
plt.subplot(4, 1, 4)
plt.plot(t, fsk_signal, label="Señal FSK", color="purple")
plt.title("Modulación FSK (Frequency Shift Keying)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
