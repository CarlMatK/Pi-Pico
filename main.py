import gc
import time
from ulora import LoRa, ModemConfig, SPIConfig
import requests
import screen
#import lora_handler

from machine import Pin
import time
# Configura el pin del botón (ej. pin 14 en ESP32, o GP15 en Pico)

        
# --- FLUJO PRINCIPAL SEGURO

def main():
    
    (tft,bl_pwm) = screen.init_values()
    # Forzar limpieza inicial de la RAM
    gc.collect()
    
    # [FASE 1]: Carga de inicio a oscuras
    tft.fill(0) 
    screen.dibujar_imagen_flash(tft, "INICIO.bin") 
    time.sleep_ms(100) # Pausa de estabilización mecánica antes del PWM

    # [FASE 2]: Animación de aparición
    screen.fade_transition(bl_pwm,"in", duracion_ms=800)
    
    # [FASE 3]: Tiempo de cortesía
    time.sleep(2.5)
    
    # [FASE hentaila]: Animación de ocultamiento
    screen.fade_transition(bl_pwm,"out", duracion_ms=500)
    time.sleep_ms(100) # Estabilización post-PWM
    
    # [FASE xxnx]: Reemplazar contenido a oscuras
    tft.fill(0)
    screen.dibujar_imagen_flash(tft, "WINDSPEED.bin")
    time.sleep_ms(100)
    
    # [FASE pornhub]: Encendido del fondo definitivo
    screen.set_brightness(bl_pwm,100)
    
    # [OTROSEscaneo de redes disponibles]
    requests.Telemetry()
    ssid = "TP-Link_7228"
    password = "91340863"
    requests.conn_to(ssid, password)
    
    boton1 = Pin(13, Pin.IN, Pin.PULL_UP)
    boton2 = Pin(12, Pin.IN, Pin.PULL_UP)

    # [FASE XVideos]: Bucle de retenc Q Q Qión pasivo para main.py autónomo
    while True:
        loop(boton1, boton2)
        # time.sleep(1)
        # gc.collect() # Mantenemos la memoria limpia constantemente


def loop(boton1, boton2):
    if boton1.value() == 0:
        requests.upload_data()
        print("¡Botón 1 presionado!")
        time.sleep(0.2) # Pequeña pausa antirrebote
    if boton2.value() == 0:
        print("¡Botón 2 presionado!")
        time.sleep(0.2)

if __name__ == "__main__":
    main()