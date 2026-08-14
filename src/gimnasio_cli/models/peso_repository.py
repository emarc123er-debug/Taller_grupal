import json
from pathlib import Path

from gimnasio_cli.models.registro_peso import RegistroPeso

RUTA_POR_DEFECTO = Path(__file__).resolve().parents[3] / "data" / "peso.json"


class PesoRepository:
    """Persiste los registros de peso corporal en un archivo JSON local
    (aplicación de un único usuario). Guarda el historial completo internamente
    para permitir editar semanas pasadas, aunque la consulta solo expone la
    semana más reciente (regla de la especificación 002)."""

    def __init__(self, ruta_archivo: Path = RUTA_POR_DEFECTO) -> None:
        self._ruta_archivo = ruta_archivo

    def _cargar_todos(self) -> dict[str, RegistroPeso]:
        if not self._ruta_archivo.exists():
            return {}
        datos = json.loads(self._ruta_archivo.read_text(encoding="utf-8"))
        return {
            semana: RegistroPeso.desde_dict(semana, valores)
            for semana, valores in datos.items()
        }

    def _guardar_todos(self, registros: dict[str, RegistroPeso]) -> None:
        self._ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
        datos = {semana: registro.a_dict() for semana, registro in registros.items()}
        self._ruta_archivo.write_text(
            json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def guardar_registro(self, registro: RegistroPeso) -> None:
        registros = self._cargar_todos()
        registros[registro.semana] = registro
        self._guardar_todos(registros)

    def obtener_mas_reciente(self) -> RegistroPeso | None:
        registros = self._cargar_todos()
        if not registros:
            return None
        semana_mas_reciente = max(registros)
        return registros[semana_mas_reciente]
