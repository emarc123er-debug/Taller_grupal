from datetime import date

from gimnasio_cli.models.peso_repository import PesoRepository
from gimnasio_cli.models.registro_peso import RegistroPeso
from gimnasio_cli.models.semana import semana_actual, validar_semana


class PesoController:
    """Orquesta el registro y la consulta de peso corporal semanal."""

    def __init__(self, repositorio: PesoRepository | None = None) -> None:
        self._repositorio = repositorio or PesoRepository()

    def registrar_peso(self, peso_kg: float, semana: str | None = None) -> RegistroPeso:
        if peso_kg <= 0:
            raise ValueError("El peso debe ser un número mayor a 0 kg.")

        semana_valida = validar_semana(semana) if semana else semana_actual()
        registro = RegistroPeso(
            semana=semana_valida,
            peso_kg=peso_kg,
            fecha_registro=date.today().isoformat(),
        )
        self._repositorio.guardar_registro(registro)
        return registro

    def registro_mas_reciente(self) -> RegistroPeso | None:
        return self._repositorio.obtener_mas_reciente()
