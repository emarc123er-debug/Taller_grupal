from gimnasio_cli.models.dia import Dia
from gimnasio_cli.models.rutina import Rutina
from gimnasio_cli.models.rutina_repository import RutinaRepository


class RutinaController:
    """Orquesta el acceso a las rutinas entre el modelo y la vista."""

    def __init__(self, repositorio: RutinaRepository | None = None) -> None:
        self._repositorio = repositorio or RutinaRepository()

    def estado_semana(self) -> dict[Dia, Rutina]:
        return self._repositorio.cargar_semana()

    def rutina_del_dia(self, texto_dia: str) -> Rutina:
        dia = Dia.desde_texto(texto_dia)
        return self._repositorio.obtener_rutina(dia)
