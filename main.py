import gc
import time
from ulora import LoRa, ModemConfig, SPIConfig
import requests
import screen
#import lora_handler

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
    screnn.dibujar_imagen_flash(tft, "WINDSPEED.bin")
    time.sleep_ms(100)
    
    # [FASE pornhub]: Encendido del fondo definitivo
    screen.set_brightness(bl_pwm,100)
    
    # [OTROSEscaneo de redes disponibles]
    requests.Telemetry()
    
    # [FASE XVideos]: Bucle de retenc Q Q Qión pasivo para main.py autónomo
    while True:
        time.sleep(1)
        gc.collect() # Mantenemos la memoria limpia constantemente

if __name__ == "__main__":
    main()