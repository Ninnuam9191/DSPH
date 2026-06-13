# Desarrollo de Software para Hardware (DCSH01)
## Evaluación Sumativa 4.2: Visualización Personalizada de Datos XY

Este repositorio contiene una versión modificada y optimizada del proyecto base para la adquisición y visualización de datos de telemetría provenientes de un sensor móvil (acelerómetro). La interfaz ha sido rediseñada completamente desde cero utilizando un enfoque creativo de radar interactivo en un entorno web dinámico.

---

## Características Incorporadas

* **Tema Oscuro Moderno:** Diseño con paleta de colores oscuros profundos y acentos en azul neón vibrante.
* **Visualización Creativa en Tiempo Real:** En lugar de una cuadrícula estática rígida, se implementó un Visor de Radar de Tipo Mira, el cual traduce de forma fluida y continua las coordenadas analógicas de los ejes X e Y en la pantalla mediante un indicador luminoso móvil.
* **Comportamiento de Palanca de Mando (Yoke):** El sistema mapea de manera interactiva la inclinación física del dispositivo móvil, simulando la interfaz de control de una aeronave.

---

## Restricciones Obligatorias Cumplidas

De acuerdo con los requerimientos de la evaluación, la interfaz cumple estrictamente con las siguientes reglas de diseño:
1. Sin JavaScript: Todo el dinamismo de la interfaz y el posicionamiento en tiempo real se resuelven exclusivamente mediante lógica de servidor y condicionales inline.
2. Uso Exclusivo de Flask, HTML, CSS y Jinja: Las posiciones relativas se calculan dinámicamente en el backend y se renderizan usando el motor de plantillas Jinja.
3. CSS en el <head>: Todo el código de diseño de la interfaz se encuentra incorporado internamente dentro de las etiquetas <style> del bloque <head>.
4. Uso Exclusivo de Selectores por ID: No se empleó ninguna clase CSS (.class); todos los elementos y estilos apuntan estrictamente a selectores únicos por identificador (#id).

---

## Estructura del Proyecto

```bash
.
├── app.py               # Servidor Flask que recibe la telemetría TCP del sensor (Ejes Y, X)
├── README.md            # Documentación del proyecto modificado
└── templates
    └── index.html       # Plantilla HTML con estilos por ID y lógica de posicionamiento Jinja
