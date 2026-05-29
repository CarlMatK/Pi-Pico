import time
import gc
from machine import Pin, SPI, PWM
import gc9a01py as gc9a01


#---HARDWARE CONFIGURATION---#
#Define the pwm pin for the backlight
bl_pwm_pin = PWM(Pin(21))
bl_pwm_pin.freq(1000)  # Set frequency to 1 kHz
bl_pwm_pin.duty_u16(0)  # Set duty cycle to 0% (range is 0-65535)

#---DEFINE SPI AND TFT DISPLAY---#
spi = SPI(0, baudrate=60000000, sck=Pin(18), mosi=Pin(19))
tft = gc9a01.GC9A01(
    spi,
    cs=Pin(17, Pin.OUT),
    dc=Pin(16, Pin.OUT), 
    reset=Pin(20, Pin.OUT),
    backlight = None,
    rotation=0
    )

#---ANIMATION FUNTION PWM---#
def set_brightness(porcentage):
    duty = int(porcentage * 65535 / 100)  # Convert percentage to duty cycle
    bl_pwm_pin.duty_u16(duty)  # Set the duty cycle for the backlight

def fade_transition(tipo="in", duration=1000):
    steps = 20  # Number of steps in the fade transition
    delay = duration / steps  # Delay between each step
    if tipo == "in":
        for i in range(steps + 1):
            brightness = (i / steps) * 100  # Calculate brightness percentage
            set_brightness(brightness)  # Set the backlight brightness
            time.sleep_ms(int(delay))  # Wait for the specified delay
    elif tipo == "out":
        for i in range(steps + 1):
            brightness = ((steps - i) / steps) * 100  # Calculate brightness percentage
            set_brightness(brightness)  # Set the backlight brightness
            time.sleep_ms(int(delay))  # Wait for the specified delay

def image_draw_flash(tft, archivo_bin, x=0, y=0, width=240, height=240):
    #Carga optimizada con soporte para posicionamiento (X, Y).
    lineas_por_lectura = 10  # Número de líneas a leer por iteración
    bytes_por_linea = 2  # Cada píxel ocupa 2 bytes (RGB565)
    tamaño_buffer = lineas_por_lectura * width * bytes_por_linea
    buffer = bytearray(tamaño_buffer)
    try:
        with open(archivo_bin, "rb") as f:
            # Usamos 'offset_y' para recorrer las filas de la imagen
            for offset_y in range(0, height, lineas_por_lectura):
                f.readinto(buffer)
                
                # Sumamos 'x' e 'y' para posicionar el bloque en la pantalla
                tft.blit_buffer(buffer, x, y + offset_y, width, lineas_por_lectura)
                
                time.sleep_us(100) 
    except OSError:
        pass

