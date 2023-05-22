# Proyecto-_Zoologico-_2
- Documentacion : https://docs.google.com/document/d/1EmKqiasSKhZLX2QTdeBXUAfIqm9hh3bBojo262MddHI/edit?usp=sharing
- Autoevaluacion 1: https://docs.google.com/document/d/1cYI9Cj0o8W3Fx_4WVC01van-i67PXUIB-LFnX2jsigo/edit?usp=sharing
- Autoevaluacion 2: https://docs.google.com/document/d/1vqaGZd0sRHJQYCQnG8GfJJVeUIFiXsdHNImOV-fGSIY/edit?usp=sharing
- UML : 

# Enunciado
En este proyecto, se espera que los estudiantes implementen un programa en Python que simule el funcionamiento
de un zoológico. <br> El programa debe hacer uso de los conceptos de programación orientada a objetos, incluyendo la
creación de clases, relaciones, herencia, sobrescritura, sobrecarga, modificadores de acceso e interfaces gráficas.
El zoológico se compone de diferentes hábitat, cada una de los cuales puede contener varios animales. Cada animal
tiene un nombre, una especie y un hábitat al que pertenece (entre otros).<br><br>
El programa debe permitir al usuario realizar las siguientes acciones:
Crear animales en el registro del zoológico.<br><br>
* Añadir un nuevo hábitat al zoológico. Se tiene una serie definida de tipos de hábitat que se pueden crear en el
zoológico: desértico, selvático, polar y acuático. <br><br>
* Cada hábitat debe permitir conocer el número de animales
asignados, temperatura, dieta y no permitir que un animal sea asignado si no cumple con las condiciones del
hábitat o si no hay disponibilidad de espacio. <br><br>
* Crear mínimo 2 atributos específicos para cada tipo de hábitat.
Añadir un nuevo animal a un hábitat existente, garantizando que el hábitat exista y que permita contener el tipo de
animal (cumpliendo con las condiciones del hábitat y disponibilidad).<br><br>

* Listar todos los hábitat del zoológico y sus respectivos animales.<br><br>
Permitiendo a los usuarios ver la información de
los animales, como su nombre, edad, tipo de alimentación, estado de salud y cualquier otro atributo que el
estudiante haya decidido agregar.<br><br>

# Realizar una acción en particular para un animal específico (dar órdenes al animal). 
Para esto debe tomar como parámetros el identificador del animal y el nombre de la acción a realizar. Las acciones disponibles para los
animales son:<br><br>

* * Comer, recibiendo el alimento y validando si este se encuentra en la lista aprobada para cada tipo de dieta.<br><br>
Dormir, recibiendo el número de horas que el animal debe dormir y validando si es suficiente tiempo de
acuerdo al valor definido para cada animal.<br><br> 
* * Llevar un acumulado de sueño del animal, ya que no debería
pasar el tiempo máximo de cada día.<br><br>
* * Jugar, permitiendo saber si el animal ya jugó en el día o no.<br><br>
* * Permitir a los usuarios agregar y editar diferentes tipos de alimentos para los animales en el zoológico. Los
animales deben tener diferentes tipos de alimentación según su dieta: carnívoros, herbívoros, omnívoros.<br><br>
* Realizar una consulta en línea mediante un API, para mostrar información relevante para el zoológico.<br><br>
* El programa debe ser capaz de manejar errores de entrada y salida de datos. Por ejemplo, si el usuario intenta
ingresar una edad no válida para un animal, el programa debería informar al usuario del error y solicitar que
ingrese una edad válida (informar al usuario mediante mensajes en la interfaz).<br><br>
* El programa debe estar desplegado en la nube, aprovechando las funcionalidades que Streamlit tiene para
facilitar este proceso.<br><br>
* Los estudiantes deben entregar un código Python completo que implemente todas las funcionalidades especificadas
anteriormente.<br><br> El proyecto se evaluará en función de la calidad del código, la implementación de los conceptos de
programación orientada a objetos, la funcionalidad del programa y la documentación.
