# Especificaciones

Esta carpeta contiene todas las especificaciones del proyecto, siguiendo la metodología
**Spec-Driven Development**: antes de programar una funcionalidad, se documenta qué debe
hacer, su alcance y sus reglas en un archivo de especificación.

## Convenciones

- Cada especificación es un archivo Markdown numerado secuencialmente:
  `NNN-nombre-corto.md` (ej. `001-gimnasio-rutinas-semanales.md`).
- Toda especificación nueva se agrega en esta carpeta, nunca fuera de ella.
- Usar `_plantilla.md` como punto de partida para especificaciones nuevas.
- Una especificación puede quedar como "En progreso" mientras se completa por partes
  (por ejemplo, cuando el contenido se define día a día o iteración a iteración).

## Arquitectura del proyecto

- **Patrón de código:** MVC (Modelo - Vista - Controlador).
- **Gestión de librerías/dependencias:** [uv](https://docs.astral.sh/uv/) (Python).

Ver `/CLAUDE.md` en la raíz del repositorio para el detalle de estas convenciones.

## Índice de especificaciones

| # | Especificación | Estado |
|---|---|---|
| 001 | [Gimnasio - Rutinas semanales](./001-gimnasio-rutinas-semanales.md) | Implementada |
