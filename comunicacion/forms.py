from django import forms

class RadioEnlaceForm(forms.Form):
    potencia_tx = forms.FloatField(label="Potencia del transmisor (dBm)")
    perdidas_cable_tx = forms.FloatField(label="Pérdidas en cable TX (dB)")
    ganancia_ant_tx = forms.FloatField(label="Ganancia de antena TX (dBi)")
    frecuencia = forms.FloatField(label="Frecuencia (Hz)")
    distancia = forms.FloatField(label="Distancia (m)")
    ganancia_ant_rx = forms.FloatField(label="Ganancia de antena RX (dBi)")
    perdidas_cable_rx = forms.FloatField(label="Pérdidas en cable RX (dB)")
    margen_sens_rx = forms.FloatField(label="Margen de sensibilidad RX (dBm)")
    perdidas_adicionales = forms.FloatField(label="Pérdidas adicionales (dB)", required=False, initial=0)