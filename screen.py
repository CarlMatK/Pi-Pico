import time
import gc9a01py as gc9a01
from machine import Pin, SPI, PWM

def init_values():
    # Inicia totalmente apagado (oscuridad)
    # Configuracion de Hardware (Pantalla)
    bl_pwm = PWM(Pin(21))
    bl_pwm.freq(1000)
    bl_pwm.duty_u16(0)
    
    spi = SPI(0, baudrate=60000000, sck=Pin(18), mosi=Pin(19))
    
    tft = gc9a01.GC9A01(
    spi, 
    dc=Pin(16, Pin.OUT), 
    cs=Pin(17, Pin.OUT), 
    reset=Pin(20, Pin.OUT), 
    backlight=None,  
    rotation=0)
    
    return (tft,bl_pwm)
    
# --- FUNCIONES DE CONTROL DE ANIMACIÓN (PWM) ---

def set_brightness(bl_pwm,porcentaje):
    duty = int((porcentaje / 100) * 65535)
    bl_pwm.duty_u16(duty)
    
def fade_transition(bl_pwm,tipo="in", duracion_ms=600):
    pasos = 20
    tiempo_paso = duracion_ms // pasos
    
    if tipo == "in":
        for i in range(0, 101, 5):
            set_brightness(bl_pwm,i)
            time.sleep_ms(tiempo_paso)
    elif tipo == "out":
        for i in range(100, -1, -5):
            set_brightness(bl_pwm,i)
            time.sleep_ms(tiempo_paso)
            
def dibujar_imagen_flash(tft, archivo_bin, ancho=240, alto=240):
    """
    Carga optimizada para ejecución autónoma (main.py).
    Se reduce a 15 líneas para evitar bloqueos del bus de la Flash.
    """
    lineas_por_bloque = 10 # <--- CORRECCIÓN DE MEMORIA CRÍTICA
    bytes_por_pixel = 2
    tamano_buffer = ancho * lineas_por_bloque * bytes_por_pixel
    buffer = bytearray(tamano_buffer)
    
    try:
        with open(archivo_bin, "rb") as f:
            for y in range(0, alto, lineas_por_bloque):
                f.readinto(buffer)
                tft.blit_buffer(buffer, 0, y, ancho, lineas_por_bloque)
                # Pequeña pausa de 500 microsegundos para dejar respirar al bus de la Flash
                time.sleep_us(100) 
    except OSError:
        pass

