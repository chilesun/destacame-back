# destacame-back

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