'''
Aplicacion con el objetivo de evitar que el ordenador se bloquee, para ello cada
30 segundos clica en el raton en la esquina superior izquierda de la pantalla.
'''

import ctypes
import time

def left_click(x, y, clicks=1):
    SetCursorPos(x, y)
    for i in range(clicks):
        mouse_event(2, 0, 0, 0, 0)
        mouse_event(4, 0, 0, 0, 0)

def main(sec=30):
    while True:
        left_click(0, 0)
        time.sleep(sec)

if __name__ == "__main__":
    SetCursorPos = ctypes.windll.user32.SetCursorPos
    mouse_event = ctypes.windll.user32.mouse_event
    main()
