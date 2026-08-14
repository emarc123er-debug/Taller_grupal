# 003 - Interfaz web

- **Estado:** Implementada (ver `README.md`)
- **Fecha:** 2026-08-14

## Objetivo

Agregar una interfaz web a la aplicación de gimnasio, para poder consultar las
rutinas y el peso corporal, y registrar/editar el peso, desde el navegador.

## Alcance

- La interfaz web **convive** con la CLI existente ([001](./001-gimnasio-rutinas-semanales.md),
  [002](./002-peso-corporal-y-color-app.md)): ambas usan la misma lógica de negocio
  (modelos y controladores), solo cambia la vista.
- La web permite **consultar y editar**: ver el estado semanal de rutinas, el
  detalle de cada día, ver el último peso registrado, y registrar/editar el peso
  semanal (igual que ya permite la CLI).
- Sigue siendo una aplicación de **un único usuario, sin login**.
- **No incluye** en esta versión: crear/editar rutinas desde la web (las rutinas se
  siguen definiendo por especificación, como hasta ahora), ni despliegue en un
  servidor público (uso local).

## Reglas / comportamiento esperado

1. Reutiliza los modelos y controladores existentes (`RutinaController`,
   `PesoController`); la Vista Web es una capa nueva, no una reimplementación de
   la lógica.
2. Página principal: muestra el estado de los 5 días (definida/pendiente) y el
   último peso registrado.
3. Página de detalle de un día: muestra los ejercicios de esa rutina (mismas
   reglas que la CLI, incluyendo el rechazo de sábado/domingo).
4. Página/formulario de peso: permite registrar el peso de la semana actual y,
   opcionalmente, editar el de una semana pasada (mismo criterio que la CLI:
   upsert por semana, sin historial completo visible).
5. La interfaz web usa el mismo **color azul** de la aplicación (spec 002) como
   color principal de la UI.
6. Corre en un servidor local (no requiere autenticación ni HTTPS para esta
   versión).

## Arquitectura

- Se mantiene el patrón **MVC**: los modelos y controladores de `src/gimnasio_cli/`
  se reutilizan tal cual; se agrega una nueva Vista Web (plantillas HTML) que
  consume los mismos controladores que hoy usa la `CLIView`.
- **Framework web:** [Flask](https://flask.palletsprojects.com/) — liviano, encaja
  naturalmente con MVC y se gestiona como dependencia con `uv` (`uv add flask`).
- La persistencia no cambia: sigue en `data/rutinas.json` y `data/peso.json`.

## Rutas propuestas

| Ruta | Método | Descripción |
|---|---|---|
| `/` | GET | Estado semanal de rutinas + último peso registrado |
| `/dia/<nombre>` | GET | Detalle de la rutina de un día |
| `/peso` | GET | Formulario y último peso registrado |
| `/peso` | POST | Registra/edita el peso (campo semana opcional) |

## Decisiones

- Framework: Flask.
- Convive con la CLI (no la reemplaza).
- Permite consulta y edición de peso desde la web.
- Servidor local, sin autenticación, sin despliegue público en esta versión.
- Color principal de la UI: azul (mismo criterio que la spec 002).
