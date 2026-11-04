# EcoTech-Evaluacion-MaximilianoCardozo

Utilicé la IA para generar datos de prueba dentro de la base de datos con el fin
de facilitar la prueba de la aplicación. La IA generó 5 departamentos y 20 empleados
con información ficticia, incluyendo nombres, correos electrónicos, direcciones y números de
teléfono.


## Levantar el proyecto en otro equipo

En el nuevo equipo necesitás tener instalados Git y Python 3. Luego, abrí
PowerShell y ejecutá:

```powershell
git clone https://github.com/maxicardozoparedes4431-cmyk/EcoTech-Evaluacion-MaximilianoCardozo.git
cd EcoTech-Evaluacion-MaximilianoCardozo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Si PowerShell no permite activar el entorno virtual, ejecutá:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Iniciar con SQLite

SQLite no requiere instalar ni ejecutar un servidor de base de datos. Editá el
archivo `.env` con esta configuración:

```env
DB_ENGINE=sqlite
DB_NAME=ecotech_local.db
```

Con el entorno virtual activado, iniciá el programa desde la raíz del proyecto:

```powershell
$env:PYTHONPATH="src"
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
DB_PASSWORD=tu_contraseña
```

Reemplazá `DB_USER` y `DB_PASSWORD` por las credenciales de tu instalación.
Con el entorno virtual activado, iniciá el programa:

```powershell
$env:PYTHONPATH="src"
python src\main.py
```

La aplicación crea las tablas y carga los datos de prueba al iniciar.
