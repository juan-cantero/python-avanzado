# Entornos virtuales

Un entorno virtual en Python es una herramienta 
que te permite crear un espacio aislado donde puedes instalar 
y manejar las dependencias (bibliotecas y versiones de Python) 
específicas para un proyecto en particular, sin afectar al sistema global

- `pip list`: Muestra las bibliotecas instaladas en el entorno virtual o global

¿Cómo crear un entorno virtual? (entorno aislado del global)

- `python -m venv .venv` (Windows)
- `python3 -m venv .venv` (Linux o Mac)

¿Cómo activar el entorno virtual?


Si usas Windows, por única vez debes dar permisos a Windows para luego activar el entorno virtual. Abrir `Microsoft PowerShell` en modo administrador, y ejecutar el comando:

`Set-ExecutionPolicy Unrestricted`

Luego cerrar todas las terminales abiertas para que los cambios tengan efecto.


- `.\.venv\Scripts\activate`  (Windows Powershell)
- `source .venv/bin/activate` (Linux o Mac)

¿Cómo crear requirements.txt?
- `pip freeze >> requirements.txt`

¿Cómo instalar paquetes desde requirements.txt?
- `pip install -r requirements.txt`
