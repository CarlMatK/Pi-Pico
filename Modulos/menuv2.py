import time
import screen

menu_image = {
    "MENU1": "MENU1.bin",
    "MENU2": "MENU2.bin",
    "MENU3": "MENU3.bin",
    "MENU4": "MENU4.bin",
    "MENU5": "MENU5.bin",
    "MENU6": "MENU6.bin",
}

class MenuPrincipal:
    def __init__(self, tft):
        self.tft = tft
        self.opciones = list(menu_image.keys())
        self.seleccion_actual = 0

    def dibujar(self):
        # Dibuja la imagen del menú actual
        menu_key = self.opciones[self.seleccion_actual]
        archivo_bin = menu_image[menu_key]
        screen.image_draw_flash(self.tft, archivo_bin, x=0, y=0, width=240, height=240)

    def mover_arriba(self):
        if self.seleccion_actual > 0:
            self.seleccion_actual -= 1
            self.dibujar()

    def mover_abajo(self):
        if self.seleccion_actual < len(self.opciones) - 1:
            self.seleccion_actual += 1
            self.dibujar()