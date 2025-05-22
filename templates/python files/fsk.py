import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parámetros básicos
bit_rate = 1         # bits por segundo
bitstream = [1, 0, 1, 1, 0]
fs = 1000            # frecuencia de muestreo
amplitud = 1         # amplitud de la señal
T_bit = 1 / bit_rate # duración de cada bit

f_carrier = 10       # frecuencia de la portadora

# Tiempo total de muestreo
t_muestreo = np.linspace(0, T_bit * len(bitstream), len(bitstream) * fs)

# Señal digital (para mostrar la secuencia)
digital_signal = np.repeat(bitstream, fs)

# Función para generar la señal FSK en función del índice de modulación h
def generate_fsk_signal(h):
    # Definir las frecuencias en función del índice de modulación
    f1 = f_carrier + h  # para bit "1"
    f2 = f_carrier - h  # para bit "0"
    
    signal_fsk = np.zeros_like(t_muestreo)
    
    for i, bit in enumerate(bitstream):
        t_segment = np.linspace(i * T_bit, (i + 1) * T_bit, fs)
        if bit == 1:
            signal_fsk[i * fs:(i + 1) * fs] = amplitud * np.sin(2 * np.pi * f1 * t_segment)
        else:
            signal_fsk[i * fs:(i + 1) * fs] = amplitud * np.sin(2 * np.pi * f2 * t_segment)
    return signal_fsk

# Valor inicial del índice de modulación
h_init = 2
signal_fsk = generate_fsk_signal(h_init)

# Crear figura y ejes
fig, ax = plt.subplots(3, 1, figsize=(10, 8))
plt.subplots_adjust(left=0.1, bottom=0.25)
t_ref = np.linspace(0, T_bit, fs)  # solo un bit de duración

onda_f1 = amplitud * np.sin(2 * np.pi * (f_carrier + h_init) * t_ref)
onda_f2 = amplitud * np.sin(2 * np.pi * (f_carrier - h_init) * t_ref)

# Gráfica de la señal FSK
line_fsk, = ax[1].plot(t_muestreo, signal_fsk, color="green", label="Señal FSK")
ax[1].set_title("Señal FSK modulada")
ax[1].set_xlabel("Tiempo (s)")
ax[1].set_ylabel("Amplitud")
ax[1].legend()

# Gráfica de la señal digital
line_digital, = ax[0].plot(t_muestreo, digital_signal, color="blue", label="Señal Digital")
ax[0].set_title("Señal Digital")
ax[0].set_xlabel("Tiempo (s)")
ax[0].set_ylabel("Amplitud")
ax[0].legend()



line_f1, = ax[2].plot(t_ref, onda_f1, color="red", linestyle='--', label="Onda f1")
ax[2].plot(t_ref, onda_f2, color="purple", linestyle='--', label="Onda f2")
ax[2].set_title("Señal FSK modulada")
ax[2].set_xlabel("Tiempo (s)")
ax[2].set_ylabel("Amplitud")
ax[2].legend()


# Crear un slider para el índice de modulación
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.05])
slider_mod = Slider(ax_slider, "Índice de modulación", 0.1, 5.0, valinit=h_init)

# Función de actualización al mover el slider
def update(val):
    new_h = slider_mod.val
    new_signal_fsk = generate_fsk_signal(new_h)
    line_fsk.set_ydata(new_signal_fsk)
    fig.canvas.draw_idle()

slider_mod.on_changed(update)
plt.show()
