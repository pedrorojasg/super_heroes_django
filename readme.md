# Super Heroes Project (With Django)

Consigna: Crear una web que muestre datos de tus superhéroes favoritos, guardados en un BD.

+ Deberá tener un template, una vista y dos modelos (SuperHeroe y Poder)
+ La clase SuperHeroe, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas)
+ Se deberán crear como mínimo 3 superhéroes, cada uno con dos poderes
+ Los superheróes se deben ver desde la web.

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona el proyecto
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para cargar super heroes iniciales

```
from heroes.models import *
from datetime import date

spiderman = SuperHeroe.objects.create(nombre='Spiderman', peso_kg=70, fecha_nacimiento=date(2000,3,4))
hulk = SuperHeroe.objects.create(nombre='Hulk', peso_kg=400, fecha_nacimiento=date(1970,10,6))

# Creando un poder sin superheroe asignado
telarana = Poder.objects.create(nombre='Telaraña')

# Creando un poder con superheroe asignado
patada = Poder.objects.create(nombre='Patada', super_heroe=spiderman)

# ¿Como asignar un super poder sin super heroe a alguien?
telarana.super_heroe = spiderman
telarana.save()
```
