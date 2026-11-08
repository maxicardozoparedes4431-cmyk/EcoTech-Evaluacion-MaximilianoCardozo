# EcoTech-Evaluacion-MaximilianoCardozo

# Documentación de uso de la IA

Utilicé la IA para generar datos de prueba dentro de la base de datos con el fin
de facilitar la prueba de la aplicación. La IA generó 5 departamentos y 20 empleados
con información ficticia, incluyendo nombres, correos electrónicos, direcciones y números de
teléfono.

Mi razonamiento para este uso de la IA es para de forma eficiente, porder cargar datos que tengan sentido
sin tener que estar registrando empleados/adminstradores constantemente

También use la IA como apoyo para la consulta de la API, específicamente en la sección de rescatar el último dato disponible de la base de datos y guardarla como historial.

Decidí mantener los cambios realizados ya que funcionan de manera correcta
en caso de alguna falla con la API


## Levantar el proyecto en otro equipo

En el nuevo equipo necesitás tener instalados Git y Python 3. Luego, abre
PowerShell y ejecutá:

```git bash
git clone https://github.com/maxicardozoparedes4431-cmyk/EcoTech-Evaluacion-MaximilianoCardozo.git
cd EcoTech-Evaluacion-MaximilianoCardozo
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
cp .env.example .env
```


## Iniciar con SQLite

SQLite no requiere instalar ni ejecutar un servidor de base de datos. Editá el
archivo `.env` con esta configuración:

```env
DB_ENGINE=sqlite
DB_NAME=ecotech_local.db
```

Con el entorno virtual activado, iniciá el programa desde la raíz del proyecto:

```git bash
python src\main.py
```

Las tablas y los datos de prueba se generan automáticamente en el archivo
indicado por `DB_NAME`.

## Iniciar con MySQL

Para usar MySQL, asegurate de tener instalado el servidor MySQL y de que esté
iniciado. Creá la base de datos antes de ejecutar la aplicación:

```sql
CREATE DATABASE ecotech_local CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Luego, configurá `.env` con los datos de conexión:

```env
DB_ENGINE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ecotech_local
DB_USER=root
DB_PASSWORD=
```

```
IMPORTANTE CAMBIAR EL PUERTO A 3308
```

Reemplazá `DB_USER` y `DB_PASSWORD` por las credenciales de tu instalación.
Con el entorno virtual activado, iniciá el programa:

```powershell
$env:PYTHONPATH="src"
python src\main.py
```

La aplicación crea las tablas y carga los datos de prueba al iniciar.

Si quiere utilizar el menú de admin, Ingrese con el usuario "admin_sys" con "admin123" de contraseña

En cabmio si quiere utilizar el menú de empleado, Ingrese con el usuario "empleado_1" con "empleado123" de contraseña
