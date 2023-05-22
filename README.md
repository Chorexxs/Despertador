# Despertador con Python

Este es un programa de reloj despertador simple escrito en Python. Se usa la biblioteca `time` para obtener la hora actual y la biblioteca `simpleaudio` para reproducir un sonido de guitarra eléctrica cuando el reloj despertador se activa. 

## Cómo usar

El programa le pedirá que ingrese la hora y el minuto en los que desea que el reloj despertador se active. Debe ingresar la hora en formato de 24 horas. Luego, el programa se ejecutará en segundo plano y se verificará la hora actual cada minuto hasta que la hora y el minuto configurados coincidan con la hora y el minuto actuales. En ese momento, se reproducirá un sonido de guitarra eléctrica y se detendrá el programa.

## Dependencias

Este programa depende de la biblioteca `simpleaudio`, que se puede instalar usando el siguiente comando:

"pip install simpleaudio"

## Archivos de sonido

El programa utiliza un archivo de sonido de guitarra eléctrica que debe estar ubicado en el directorio `Despertador/sonido/`. Si desea utilizar su propio archivo de sonido, asegúrese de cambiar la ruta en la línea 18 del archivo `despertador.py` para que coincida con la ubicación de su archivo de sonido. 
