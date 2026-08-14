# Convenciones del proyecto

## Metodología: Spec-Driven Development

- Toda especificación nueva se crea dentro de la carpeta [`especificaciones/`](./especificaciones/README.md),
  numerada secuencialmente (`NNN-nombre-corto.md`).
- No se implementa una funcionalidad sin que exista primero (o en paralelo) su
  especificación correspondiente en esa carpeta.
- Cada especificación nueva o con cambios de alcance importantes se desarrolla en su
  propia rama creada a partir de `main`.

## Arquitectura de código: MVC

El código de la aplicación se organiza siguiendo el patrón **Modelo - Vista - Controlador**:

- **Modelo:** entidades y lógica de datos/negocio.
- **Vista:** presentación/salida hacia el usuario.
- **Controlador:** orquesta la interacción entre modelo y vista.

## Gestión de dependencias: uv

Las librerías del proyecto (Python) se gestionan con [`uv`](https://docs.astral.sh/uv/)
(`uv add`, `uv sync`, `uv run`, etc.) en lugar de `pip`/`venv` manual.
