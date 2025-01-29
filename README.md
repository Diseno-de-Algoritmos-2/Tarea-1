# Tarea 1

Este repositorio contiene dos ejercicios de grafos (Punto 3 y Punto 5), los cuales se describen a continuación.

## Autores

- **Juan Camilo Sánchez** - [juancamilosanchez](

## Punto 3: Distribución de Amigos en Reuniones

### Descripción

Juan quiere invitar a sus amigos a su nuevo apartamento, pero algunas parejas de amigos han tenido conflictos. Por ello, necesita organizar dos reuniones de manera que no haya personas peleadas dentro de cada grupo. El ejercicio consiste en determinar si es posible distribuir a los amigos en dos reuniones, asegurando que no haya parejas conflictivas dentro de ellas.

### Estructura del Punto 3

El repositorio contiene los siguientes scripts para resolver el Punto 3:

1. **Algoritmo de Solución (Ubicado en /Punto-3)**:
   - `main.py`: Algoritmo que determina si es posible organizar las dos reuniones y genera los grupos de amigos. Se describe mejor la estrategia de solución en el archivo.
   - `input.txt`: Contiene los datos de los amigos y sus relaciones de amistad que son la entrada del algoritmo (Su estructura se detalla en el archivo main.py del punto 3).
   - `output.txt`: Guarda el resultado del programa, indicando si es posible organizar las reuniones y los grupos en los que se dividen los amigos (Si es posible) (Su estructura se detalla en el archivo main.py del punto 3).

2. **Generador de Grafos (Ubicado en /generador-grafos)**:
   - `grafo_punto-3.py`: Genera un grafo aleatorio de amistades y lo guarda en el archivo `input.txt` para ser usado por el algoritmo. Su uso es **opcional**, y su intencioń es facilitar la creación de casos de prueba, pero no es necesario para la ejecución del algoritmo.


Adicionalmente se incluye un caso de prueba en `input.txt` que puede ser utilizado para probar el algoritmo. Para el grafo de este caso de prueba, se incluye una imagen 'grafo.jpg' que muestra la estructura de las relaciones de amistad.

### Ejemplo (Punto 3)

**Entrada (`input.txt`)**:

Para cada línea del archivo de entrada, la primera palabra de cada linea representa un amigo, y la lista de amigos que le siguen (despues de un ':') son los amigos con quienes no está peleado/peleada, separados por comas. Por ejemplo, la siguiente entrada:

```
Juan: Pedro, Maria, Carlos
Carlos: Juan
Pedro: Juan, Maria
Maria: Juan, Pedro
```

**Salida (`output.txt`)**:

La salida cosiste en un archivo de texto llamado output.txt que contiene la información de las reuniones, junto con un mensaje que indica si es posible organizar las dos reuniones. Por ejemplo, la siguiente salida:

```
Es posible organizar las dos reuniones
Reunion 1: {'Pedro', 'Juan', 'Maria'}
Reunion 2: {'Carlos'}
```


## Punto 5: Optimización de Vías en una Ciudad

### Descripción

La ciudad fue diseñada originalmente con calles de una sola vía. A medida que la población creció, surgieron problemas de tráfico debido a desvíos innecesarios. El alcalde decidió ampliar algunas de las vías para que puedan ser de doble sentido. El objetivo es determinar qué vías deben convertirse en doble vía, de manera que se pueda transitar entre todos los puntos de la ciudad de forma eficiente, y con el mínimo costo de conversión.

### Estructura del Punto 5

El repositorio contiene los siguientes scripts para resolver el Punto 5:

1. **Algoritmo de Solución (Ubicado en /Punto-5)**:
   - `main.py`: Implementa el algoritmo que determina qué vías deben convertirse en doble vía para lograr la mínima conversión de costo, conectando toda la ciudad. Se describe mejor la estrategia de solución en el archivo.
   - `input.txt`: Contiene los datos de las vías de la ciudad, sus conexiones y los costos de conversión (Su estructura se detalla en el archivo main.py del punto 5).
   - `output.txt`: Guarda el resultado, indicando qué vías deben convertirse a doble vía y el costo asociado a la conversión (Su estructura se detalla en el archivo main.py del punto 5).

2. **Generador de Grafos (Ubicado en /generador-grafos)**:
   - `graph_generator.py`: Genera un grafo aleatorio que representa las vías de la ciudad, sus conexiones y los costos, y lo guarda en el archivo `input.txt`. Su uso es **opcional**, y su intención es facilitar la creación de casos de prueba, pero no es necesario para la ejecución del algoritmo.

### Ejemplo (Punto 5)

**Entrada (`input.txt`)**:

```
A: (B, 6), (D, 1), (E, 7)
B: (A, 6), (D, 4), (E, 3)
C: (E, 10)
D: (A, 1), (B, 4)
E: (A, 7), (B, 3), (C, 10)
```

En este ejemplo, cada línea representa una vía de la ciudad, donde la primera letra es el nombre de la vía, seguido de las conexiones con otras vías y los costos de conversión. Por ejemplo, la vía **A** está conectada con las vías **B**, **D**, y **E**, con costos de conversión de 6, 1, y 7 respectivamente.

**Salida (`output.txt`)**:

```
En este ejemplo, el algoritmo determina que las vías **A a D**, **B a E**, y **D a B** deben convertirse en doble vía para conectar toda la ciudad con el mínimo costo.
```


### Estrategia de Solución (Punto 5)

1. **Entrada**: El archivo `input.txt` contiene un grafo que describe las vías de la ciudad, donde cada línea representa una vía y las conexiones con otras vías junto con los costos de conversión.

2. **Algoritmo de Optimización**: El algoritmo utiliza **Prim's Algorithm** para encontrar el **Árbol de Expansión Mínima (MST)**. Esto nos permite determinar cuáles son las vías que deben convertirse en doble vía para conectar toda la ciudad al costo más bajo.

3. **Salida**: El archivo `output.txt` muestra las vías que deben convertirse a doble vía y el costo de cada conversión.


---


## Instalación/Configuración

### Requisitos

Este proyecto requiere Python 3 y las siguientes bibliotecas:

- **os**, **random**: Para manejar archivos y generar relaciones aleatorias. Estas bibliotecas vienen incluidas con Python 3.
- **networkx (Opcional)**: Para la creación y manipulación de grafos para datos de prueba. Su uso no es necesario para la ejecución del algoritmo, y unicamente facilita la creación de casos de prueba.
- **matplotlib (Opcional)**: Para la visualización de los grafos generados. Su uso no es necesario para la ejecución del algoritmo, y unicamente facilita la creación de casos de prueba.

### Instalación en Windows

1. **Instalar Python 3**:
   - Dirigase a la página oficial de Python [python.org](https://www.python.org/downloads/) y descargue la última versión de Python 3.
   - Durante la instalación, asegúrese de seleccionar la opción "Add Python to PATH".

2. **Instalar dependencias**:
   - Abra una terminal (símbolo del sistema o PowerShell) y navegue a la carpeta del proyecto.
   - Ejecute el siguiente comando para instalar las dependencias necesarias:
     ```bash
     pip install networkx matplotlib
     ```

### Instalación en Ubuntu

1. **Instalar Python 3**:
   - En la terminal, ejecute los siguientes comandos:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

2. **Instalar dependencias**:
   - Una vez instalado Python, instale las bibliotecas necesarias con:
     ```bash
     pip3 install networkx matplotlib
     ```

### Ejecución

1. Una vez que haya instalado las dependencias, podrá ejecutar el script principal. Para el **Punto 3** y el **Punto 5**, se ejecuta el archivo `3.py` y `5.py` respectivamente, ejemplo para el punto 3:

   Para el **Punto 3**:
   ```bash
   python 3.py


2. Si desea generar los grafos aleatorios, puede ejecutar los generadores correspondientes. Para el **Punto 3** y el **Punto 5**, puede ejecutar el archivo `grafo_punto-3.py` o `grafo_punto_5` respectivamente, ejemplo para el punto 3:

   Para el **Punto 3**:
   ```bash
   python grafo_punto-3.py
