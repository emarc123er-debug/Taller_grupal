# Taller_grupal
Emma

## Gimnasio CLI

Aplicación de línea de comandos para consultar las rutinas de gimnasio de
lunes a viernes. Especificación: [`especificaciones/001-gimnasio-rutinas-semanales.md`](./especificaciones/001-gimnasio-rutinas-semanales.md).

También permite registrar el peso corporal semanal. Especificación:
[`especificaciones/002-peso-corporal-y-color-app.md`](./especificaciones/002-peso-corporal-y-color-app.md).

Arquitectura MVC (`src/gimnasio_cli/{models,views,controllers}`), dependencias
gestionadas con [uv](https://docs.astral.sh/uv/), datos persistidos en
`data/rutinas.json` y `data/peso.json`.

```bash
uv run gimnasio-cli semana        # estado de los 5 días
uv run gimnasio-cli dia lunes     # rutina de un día puntual

uv run gimnasio-cli peso registrar 78.5                    # peso de la semana actual
uv run gimnasio-cli peso registrar 80 --semana 2026-W30    # corrige una semana pasada
uv run gimnasio-cli peso ver                                # última semana registrada
```

## Interfaz web

También hay una interfaz web (convive con la CLI, misma lógica de negocio).
Especificación: [`especificaciones/003-interfaz-web.md`](./especificaciones/003-interfaz-web.md).

```bash
uv run gimnasio-web    # levanta el servidor en http://127.0.0.1:5000
```

- `/` — estado semanal de rutinas y último peso registrado
- `/dia/<nombre>` — detalle de la rutina de un día
- `/peso` — ver y registrar/editar el peso corporal
