# destacame-back

## Sobre el modelamiento
En el siguiente enlace es posible encontrar una diagramación acorde a lo realizado:
https://dbdiagram.io/d/623dce07bed6183873fbe3ac
Todo confluye en los trips. Dentro del modelo también hay funciones para calcular el 
dígito verificador de los RUN y la hora de término de un viaje en base a la duración
del trayecto. De otra forma se podría viajar en el tiempo. 
Adicionalmente, al crear un viaje se crean automáticamente N asientos según la capacidad
del bus.  


## Instrucciones:
## Paso 1: Clonar Repositorio

```bash
$ git clone https://github.com/chilesun/destacame-back.git
$ cd destacame-back
```

## Paso 2: Instalar virtualenv (si ya lo tienes, puedes omitir este paso)

```bash
$ pip install virtualenv
```

## Paso 3: Crear entorno virtual

```bash
$ virtualenv .
$ source bin/activate
```

## Paso 4: Instalar requirements.txt

```bash
$ pip install -r requirements.txt
```

## Paso 5: Migrate e iniciar el servidor

```bash
$ python manage.py migrate
$ python manage.py runserver
```