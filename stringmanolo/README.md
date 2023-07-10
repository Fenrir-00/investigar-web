# CAMBIOS
- Añadir shebang  
Permite ejecutar el programa sin anteponer python3
- Añadir entorno virtual (venv)  
Permite aislar versiones de dependencias del programa de versiones de paquetes que tenga instalado el sistema
- Añade gestion real de dependencias con el requeriments.txt
- Remplaza llamados directas sin control al os por llamadas seguras para limpiar pantalla 
- Corrige la función ping  
Estaba creando ficheros temporales y leyéndolos usando llamadas inseguras en lugar de simplemente obtener el output del comando como retorno a una variable
- Corrige la función ip  
Mismo problema que ping
	
# TODO
- Autoinstalar el programa como comando
- Cambiar multiples llamadas consecutivas de printf for unica llamada
- Remplazar funciones que llaman a print por retorno de texto
- Lintea/identa/estila siguiendo convenciones 
- Muchas funciones dependen de variables globales en lugar de usar parámetros
