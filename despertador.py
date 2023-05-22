import time
import simpleaudio as sa

# función para configurar el reloj despertador
def set_alarm():
    print("Ingrese la hora y el minuto a los que desea configurar el despertador: ")
    hour = int(input("Hora (en formato de 24 horas): "))
    minute = int(input("Minuto: "))
    print(f"Despertador configurado a las {hour:02d}:{minute:02d}")
    return hour, minute

# función para iniciar el despertador
def start_alarm(hour, minute):
    while True:
        current_time = time.localtime()
        if (current_time.tm_hour == hour) and (current_time.tm_min == minute):
            print("¡Despierta! ¡Es hora de levantarse!")
            wave_obj = sa.WaveObject.from_wave_file("Despertador/sonido/electric_guitar_melody_13.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()
            break
        time.sleep(60) # esperar 1 minuto antes de volver a comprobar la hora

# programa principal
print("Bienvenido al reloj despertador")

# configurar el reloj despertador
hour, minute = set_alarm()

# iniciar el reloj despertador
start_alarm(hour, minute)

print("Hasta luego")
