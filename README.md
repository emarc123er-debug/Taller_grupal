# Taller_grupal
Emma

## Gimnasio CLI

Aplicación de línea de comandos para consultar las rutinas de gimnasio de
lunes a viernes. Especificación: [`especificaciones/001-gimnasio-rutinas-semanales.md`](./especificaciones/001-gimnasio-rutinas-semanales.md).

Arquitectura MVC (`src/gimnasio_cli/{models,views,controllers}`), dependencias
gestionadas con [uv](https://docs.astral.sh/uv/), datos persistidos en `data/rutinas.json`.

```bash
uv run gimnasio-cli semana        # estado de los 5 días
uv run gimnasio-cli dia lunes     # rutina de un día puntual
```
