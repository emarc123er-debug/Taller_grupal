# 002 - Registro de peso corporal semanal y color de la aplicación

- **Estado:** Implementada (ver `README.md`)
- **Fecha:** 2026-08-14

## Objetivo

Ampliar la app de gimnasio para que el usuario pueda registrar su peso corporal una
vez por semana, y darle identidad visual a la CLI usando un color para resaltar la
salida en la terminal.

## Alcance

- Registro y consulta del peso corporal semanal (una aplicación de un único usuario,
  sin login — mismo criterio que la especificación [001](./001-gimnasio-rutinas-semanales.md)).
- Color de la aplicación: se usa para resaltar títulos y datos destacados en la
  salida de la CLI.
- **No incluye** en esta versión: gráficos de evolución, múltiples mediciones por
  semana, ni otras unidades corporales (grasa corporal, medidas, etc.).

## Reglas / comportamiento esperado

1. El peso corporal se registra **una vez por semana**, en **kilogramos (kg)**.
2. Cada registro de peso queda asociado a la semana en la que se cargó (no a un día
   puntual como las rutinas).
3. Debe ser posible registrar el peso de la semana actual.
4. Debe ser posible consultar el registro de peso corporal más reciente (última
   semana registrada), no un historial completo.
5. Si ya existe un registro para la semana en curso, un nuevo registro lo reemplaza
   (no se permite más de un valor por semana).
6. Debe ser posible editar/corregir el registro de una semana pasada (no solo el de
   la semana actual).
7. La salida de la CLI usa **color azul** para resaltar: títulos de sección, el
   peso registrado y encabezados de tablas/listas.

## Modelo de datos (propuesto)

- **RegistroPeso**
  - `semana`: identificador de semana (ej. año + número de semana ISO)
  - `peso_kg`: número (kilogramos)
  - `fecha_registro`: fecha en que se cargó el dato

## Decisiones

- **Unidad:** kilogramos (kg).
- **Frecuencia:** un único valor de peso por semana.
- **Color de la aplicación:** azul.
- **Edición:** se puede editar/corregir un registro de una semana pasada (no solo el
  de la semana actual).
- **Historial:** se muestra limitado a la última semana registrada (no el historial
  completo).
