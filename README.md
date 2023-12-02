# Laboratorio 6 de Plataformas

## Esutiante:

- Luis Brenes Campos (C21324)

## Descripción del Proyecto

EL repositorio cuenta con tres archivos para ejecutar dos tareas diferentes:

- calc.py: Es una carculadora simple que realiza las operaciones básicas (multiplicar, sumar, divir y restar).

- eventmanager.py y datamanager.py: Actualiza datos en tiempo real de una función específica y se imprimen los datos cuando se da el cambio.

## Módulo 1: Calculadora ("calc.py")

### Descripción

El módulo `calc.py` proporciona una calculadora interactiva que permite al usuario realizar operaciones matemáticas básicas.

### Dependencias e Instalación

No posee dependencias. Aegurarse que posea python instalado

### Pasos para ejecución

1. Abre una terminal.
2. Navega al directorio que contiene `calc.py`.
3. Ejecuta el siguiente comando para "bash":
   - python calc.py
4. Utiliza CTRL + C para detener el programa.

### Resultados

El código logra con su cometido de realizar las opereaciones y se obtienen los datos necesarios dados por el usuario de manera correcta. Además, se tuvieron en cuenta otros errores posibles como dividir entre 0. Por otro lado, el menú tiene detalles que ayudan en el caso de que el usuario no pueda reconocer los carácteres. A su vez, pasamos de un solo print a varios para ejemplificar que, cuando se realizan divisiones y restas de manera invertida, dan otros resultados.

![Resultado 1](https://github.com/BraiderZ/Lab6/blob/feature/Readme/Resultado1_Calculadora.png?raw=true)
![Resultado 2](https://github.com/BraiderZ/Lab6/blob/feature/Readme/Resultado2_Calculadora.png?raw=true)

Si quisieramos mejorar el resultado, una posible mejor es dejar que el usuario elija la cantidad de números a usar y no solo 2.

## Módulo 2: Eventos en tiempo real ("eventmanager.py" y "datamanager.py")

### Descripción

El módulo tiene como objetivo actualizar los valores de une evento de manera real e imprimir dichas actualizaciones.

### Dependencias e Instalación

| Biblioteca   | Enlace                                              |
|--------------|-----------------------------------------------------|
| Threading    | [Threading](https://docs.python.org/3/library/threading.html) |
| Time         | [Time](https://docs.python.org/3/library/time.html) |
| Random       | [Random](https://docs.python.org/3/library/random.html) |

Para intalarlos en "bash":

- pip install threading
- pip install time
- pip install random

### Pasos para ejecución

1. Abre una terminal.
2. Navega al directorio que contiene `datamanager.py`.
3. Ejecuta el siguiente comando para "bash":
   - python datamanager.py
4. Utiliza CTRL + C para detener el programa.

### Resultados

El código logra con su cometido de actualizar en tiempo real los eventos. Entre los aspectos a destacar encontramos:

- El manejo de errores es efectivo. Todo lo que estuviera en el main se agregó dentro de "try" para evitar problemas.
- Se agregaron partes nuevas de script que se encargaran de detener el código de manera correcta ya que antes no funcionaba con solo un CRTL + C.
- Para lograr notificar de manera correcta los cambios, se colocó el método de "Notify" de "EventManager" después de realizar los cambios en la información.
- La función que es envidada como callback, cumple con su cometido al imprimir los cambios que son enviados a ella.

![Resultado](https://github.com/BraiderZ/Lab6/blob/feature/Readme/Resultado_DataManager.png?raw=true)

En caso de buscar una manera de mejorar el código, se puede profundizar en que el usuario pueda interactuar un poco más. Ejemplo de ello es darle opciones de diferentes eventos a elegir y recibir sus actualizaciones.




