#  Mastermind GA: Genetic Algorithm Solver #
---


##  Tabla de Contenidos ##
[Descripción General](https://github.com/B4TN4N0/Proyecto-Mastermind.git)

[Arquitectura del Sistema](https://github.com/B4TN4N0/Proyecto-Mastermind.git)

[Configuración del Experimento](https://github.com/B4TN4N0/Proyecto-Mastermind/blob/cbe21fc17277f657d6bf6c1810124639a88cc8d1/pyproject.toml)

[Lógica del Algoritmo Genético](https://github.com/B4TN4N0/Proyecto-Mastermind/tree/cbe21fc17277f657d6bf6c1810124639a88cc8d1/src)

[Interfaz de Usuario CLI](https://github.com/B4TN4N0/Proyecto-Mastermind/blob/cbe21fc17277f657d6bf6c1810124639a88cc8d1/main.py))

[Instalación y Uso](https://github.com/B4TN4N0/Proyecto-Mastermind.git)

[Análisis de Resultados](https://github.com/B4TN4N0/Proyecto-Mastermind.git)
---
##  Sobre el Juego ##
Mastermind es un juego de lógica donde un "Creador de Código" (el usuario) elige una combinación secreta, y un "Descifrador" (la IA) intenta adivinarla. En cada intento, el sistema proporciona pistas:

Puntos Negros: Colores correctos en la posición correcta.

Puntos Blancos: Colores correctos en la posición incorrecta.
--- 

##  Características Técnicas ##

El núcleo de este proyecto reside en su Algoritmo Genético, configurado con los siguientes parámetros técnicos:
| Parámetro | Valor | Descripción |
| :--- | :--- | :--- |
| **Población** | `100` | Individuos por generación. |
| **Genes de Color** | `8` | Red, Green, Blue, Purple, Yellow, White, Pink, Orange. |
| **Longitud del Código** | `4` | Tamaño de la combinación a adivinar. |
| **Mutación** | `0.05` | Probabilidad de alteración genética aleatoria. |
---

## Componentes Genéticos ##
[Selección](https://github.com/B4TN4N0/Proyecto-Mastermind/blob/cbe21fc17277f657d6bf6c1810124639a88cc8d1/src/Mesure_fitnes_for_individuals.py): Evaluación de la aptitud (fitness) basada en la proximidad al código secreto.

[Crossover](https://github.com/B4TN4N0/Proyecto-Mastermind/blob/cbe21fc17277f657d6bf6c1810124639a88cc8d1/src/Reproduce_offspring.py): Combinación de ADN de los mejores "padres" para generar descendencia.

[Mutación](https://github.com/B4TN4N0/Proyecto-Mastermind/blob/cbe21fc17277f657d6bf6c1810124639a88cc8d1/src/algorithm_parameters.py): Introducción de variabilidad para evitar máximos locales.
--- 

Interfaz Visual
Inspirado en las versiones clásicas de aplicaciones móviles, la interfaz de consola utiliza códigos para simular un tablero de madera real:

Esferas de color: Representadas por bloques sólidos de alta visibilidad.

Tablero: Diseño estructurado con marcos y numeración de intentos.
---

##  Estructura del Proyecto ##
![alt text](image.png)
---
## Instalación y Uso ##
Requisitos previos
Python 3.11 o superior.

Una terminal compatible con colores  (Terminal de Linux, PowerShell o CMD moderno en Win10/11).

Ejecución
Clona el repositorio:

Bash

git clone https://github.com/B4TN4N0/Proyecto-Mastermind.git
cd mastermind-ga
Ejecuta el juego:

Bash

python main.py
---
 Instrucciones de Juego
Al iniciar, verás el Menú de Colores disponibles (8 opciones).

El sistema te pedirá ingresar tu Código Secreto de 4 dígitos (ej: 1 2 5 8).

Una vez establecido, el Algoritmo Genético comenzará su proceso de evolución.

Observa cómo cada generación se acerca más a tu código hasta lograr el "Match" perfecto.
---
## 🛠️ Posibles Mejoras (Roadmap) ##
[ ] Implementar el algoritmo de Donald Knuth para comparar eficiencia contra el GA.

[ ] Exportación de estadísticas de convergencia a archivos .csv.

[ ] Interfaz gráfica de usuario (GUI) utilizando Tkinter o PyQt.

Desarrollado por: [Óscar Fernández Millan  y Joaquín Fernández García]