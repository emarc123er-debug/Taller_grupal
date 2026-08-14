import json
from pathlib import Path

from gimnasio_cli.models.dia import Dia
from gimnasio_cli.models.rutina import Rutina

RUTA_POR_DEFECTO = Path(__file__).resolve().parents[3] / "data" / "rutinas.json"


class RutinaRepository:
    """Persiste las rutinas en un archivo JSON local (aplicación de un único usuario)."""

    def __init__(self, ruta_archivo: Path = RUTA_POR_DEFECTO) -> None:
        self._ruta_archivo = ruta_archivo

    def cargar_semana(self) -> dict[Dia, Rutina]:
        if not self._ruta_archivo.exists():
            return {dia: Rutina(dia=dia) for dia in Dia.orden_semana()}

        datos = json.loads(self._ruta_archivo.read_text(encoding="utf-8"))
        semana: dict[Dia, Rutina] = {}
        for dia in Dia.orden_semana():
            datos_dia = datos.get(dia.value, {})
            semana[dia] = Rutina.desde_dict(dia, datos_dia)
        return semana

    def obtener_rutina(self, dia: Dia) -> Rutina:
        return self.cargar_semana()[dia]

    def guardar_semana(self, semana: dict[Dia, Rutina]) -> None:
        self._ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
        datos = {dia.value: rutina.a_dict() for dia, rutina in semana.items()}
        self._ruta_archivo.write_text(
            json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8"
        )
