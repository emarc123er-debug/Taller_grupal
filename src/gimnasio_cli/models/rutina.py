from dataclasses import dataclass, field

from gimnasio_cli.models.dia import Dia
from gimnasio_cli.models.ejercicio import Ejercicio


@dataclass
class Rutina:
    dia: Dia
    ejercicios: list[Ejercicio] = field(default_factory=list)

    @property
    def definida(self) -> bool:
        return len(self.ejercicios) > 0

    @classmethod
    def desde_dict(cls, dia: Dia, datos: dict) -> "Rutina":
        ejercicios = [Ejercicio.desde_dict(e) for e in datos.get("ejercicios", [])]
        return cls(dia=dia, ejercicios=ejercicios)

    def a_dict(self) -> dict:
        return {"ejercicios": [e.a_dict() for e in self.ejercicios]}
