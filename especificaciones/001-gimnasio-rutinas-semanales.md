# 001 - Gimnasio: Rutinas semanales (lunes a viernes)

- **Estado:** En progreso (el contenido de las rutinas se irá completando día a día)
- **Fecha:** 2026-08-14

## Objetivo

Aplicación de gimnasio que permite registrar y consultar la rutina de ejercicios
correspondiente a cada día de la semana laboral, para que el usuario sepa qué
entrenamiento le toca cada día.

## Alcance

- Incluye rutinas únicamente para los días **lunes, martes, miércoles, jueves y viernes**.
- **No incluye** sábado ni domingo (fuera de alcance de esta especificación).
- Las rutinas de cada día serán proporcionadas por el usuario de forma incremental,
  una especificación/actualización por día. Hasta que un día no tenga rutina
  definida, se considera "pendiente".

## Reglas / comportamiento esperado

1. Existen exactamente 5 días válidos: Lunes, Martes, Miércoles, Jueves, Viernes.
2. Cada día tiene asociada una única rutina (conjunto de ejercicios).
3. Cada rutina está compuesta por uno o más ejercicios, con al menos: nombre del
   ejercicio, series y repeticiones (peso/descanso/notas son opcionales).
4. Debe ser posible consultar la rutina de un día específico.
5. Debe ser posible ver el estado de todos los días de la semana (con rutina definida
   o pendiente).
6. No se debe permitir crear ni consultar rutinas para sábado o domingo.

## Modelo de datos (propuesto)

- **Dia**: enum { lunes, martes, miercoles, jueves, viernes }
- **Rutina**
  - `dia`: Dia (único por rutina)
  - `ejercicios`: lista de Ejercicio
- **Ejercicio**
  - `nombre`: texto
  - `series`: número
  - `repeticiones`: número
  - `peso`: número (opcional)
  - `descanso`: texto/número (opcional)
  - `notas`: texto (opcional)

## Preguntas abiertas

- ¿La aplicación es para un solo usuario o debe soportar múltiples usuarios/login?
- ¿Interfaz de uso: web, CLI, escritorio o API?
- ¿Se requiere persistencia en base de datos, o alcanza con almacenamiento en archivo
  local para esta primera versión?

## Rutinas por día

| Día | Estado | Detalle |
|---|---|---|
| Lunes | Definida | Sentadillas, press banca, remo con barra |
| Martes | Definida | Press militar, dominadas, curl de bíceps |
| Miércoles | Pendiente | — |
| Jueves | Pendiente | — |
| Viernes | Pendiente | — |

> Esta tabla se irá completando a medida que el usuario indique la rutina de cada día.

### Lunes

| Ejercicio | Series | Repeticiones | Peso | Descanso | Notas |
|---|---|---|---|---|---|
| Sentadillas | Por definir | Por definir | — | — | — |
| Press banca | Por definir | Por definir | — | — | — |
| Remo con barra | Por definir | Por definir | — | — | — |

### Martes

| Ejercicio | Series | Repeticiones | Peso | Descanso | Notas |
|---|---|---|---|---|---|
| Press militar | Por definir | Por definir | — | — | — |
| Dominadas | Por definir | Por definir | — | — | — |
| Curl de bíceps | Por definir | Por definir | — | — | — |
