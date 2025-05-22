potencai_del_transmisor=0#[dBm]
perdidas_en_el_cable=0#TX[dB]
Ganacia_de_antena=0#TX[dBi]
perdidas_en_trayectoria_espacio_libre=0 #[dB]
Ganacia_de_antena_rx=0 #RX[dBi]
perdidas_en_el_cable=0#Rx[dB]
Margen_sensibilidad_receptor=0#[dBm]

pct=0#perdidas cable transmisor
pcr=0 #perdidas cable receptor

margen= potencai_del_transmisor-pct+Ganacia_de_antena-perdidas_en_trayectoria_espacio_libre+Ganacia_de_antena_rx-pcr
resultado= margen-Margen_sensibilidad_receptor

#perdidas ene el espacio libre
frecuencia_senal=0
distancia=0
termino_constante=0
#fsl=20log(20.000)(frecuencia_senal)+20log(5*10^9)(distancia) +20 log ((4pi)/3*10^8)(termino_constante)
fsl=frecuencia_senal + distancia + termino_constante



#perdida recibida
#perdidas adicionales
fad=0
pr=potencai_del_transmisor+pct+Ganacia_de_antena-fsl+fad