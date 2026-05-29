
import gc
import machine
import time
import screen
from machine import Pin
from menuv2 import MenuPrincipal as menu



#---MAIN LOOP---#
def main():
    gc.collect()  # Limpia la memoria antes de iniciar
    screen.set_brightness(0)
    #---CARGA IMAGEN Y ANIMACIÓN DE ENTRADA---#
    screen.image_draw_flash(screen.tft, "INICIO.bin", x=0, y=0, width=240, height=240)
    time.sleep_ms(100)  
    screen.fade_transition("in", duration=800)  
    time.sleep(2.5)  
    screen.fade_transition("out", duration=500)  
    time.sleep_ms(100)  
    screen.tft.fill(0)  # Limpiamos a oscuras

    #---¡CORRECCIÓN CRÍTICA!: VOLVER A ENCENDER LA PANTALLA---#
    # Asegúrate de que en tu 'screen.py' exportes la función de brillo o el objeto PWM
    if hasattr(screen, "set_brightness"):
        screen.set_brightness(100)
    elif hasattr(screen, "bl_pwm"):
        screen.bl_pwm_pin.duty_u16(65535) # Encendido total directo al PWM

    #---MENÚ PRINCIPAL---#

    btn_arriba = machine.Pin(13, Pin.IN, Pin.PULL_UP)
    btn_abajo = machine.Pin(12, Pin.IN, Pin.PULL_UP)

    menuv2 = menu(screen.tft) 
    menuv2.dibujar()
    screen.image_draw_flash(screen.tft, "MENU1.bin", x=0, y=0, width=240, height=240)
    while True :
        # Si se presiona el botón de abajo (lectura en bajo / 
        if btn_abajo.value() == 0:
            menuv2.mover_abajo()
            time.sleep_ms(250)  # Antirrebote (Debounce) para evitar saltos dobles
        
        # Si se presiona el botón de arriba
        if btn_arriba.value() == 0:
            menuv2.mover_arriba()
            time.sleep_ms(250)  # Antirrebote
    
        time.sleep_ms(10)  # Pequeño respiro para el procesador 
        

# Corrección de sintaxis para el punto de entrada de MicroPython
if __name__ == "__main__":
    main()