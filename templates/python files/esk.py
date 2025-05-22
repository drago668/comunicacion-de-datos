import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parámetros iniciales
bit_rate = 1
bitstream = [1, 0, 1, 1, 0]
fs = 1000
f_carrier = 10
T_bit = 1 / bit_rate
t_muestreo = np.linspace(0, T_bit * len(bitstream), len(bitstream) * fs)

# Señal digital expandida
digital_signal = np.repeat(bitstream, fs)

# Portadora base
carrier = np.sin(2 * np.pi * f_carrier * t_muestreo)

# Índice de modulación inicial
indice_modulacion_init = 0.5

# Función que construye la señal ASK según índice de modulación
def construir_signal_ask(m):
    # Si el bit es 1, se usa la portadora completa.
    # Si el bit es 0, se atenúa con (1 - m)
    mask_1 = (digital_signal == 1)
    mask_0 = (digital_signal == 0)
    return mask_1 * carrier + mask_0 * ((1 - m) * carrier)

# Señal ASK inicial
signal_ask = construir_signal_ask(indice_modulacion_init)

# Crear figura
fig, ax = plt.subplots(3, 1, figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

# Gráficas
line1, = ax[0].plot(t_muestreo, carrier, color="orange", label="Portadora")
ax[0].set_title("Señal Portadora")

line2, = ax[1].plot(t_muestreo, digital_signal, color="blue", label="Señal digital")
ax[1].set_title("Señal Digital")

line3, = ax[2].plot(t_muestreo, signal_ask, color="green", label="ASK Modulada")
ax[2].set_title("Señal ASK Modulada (solo modula en 0)")

for a in ax:
    a.set_xlabel("Tiempo")
    a.set_ylabel("Amplitud")
    a.grid()

# Slider para el índice de modulación
ax_slider = plt.axes([0.2, 0.05, 0.65, 0.03])
slider = Slider(ax_slider, 'Índice de Modulación', 0.0, 1.0, valinit=indice_modulacion_init, valstep=0.01)

# Actualización del slider
def update(val):
    m = slider.val
    nueva_signal_ask = construir_signal_ask(m)
    line3.set_ydata(nueva_signal_ask)
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.tight_layout()
plt.show()


