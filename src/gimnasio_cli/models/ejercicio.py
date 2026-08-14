from dataclasses import dataclass


@dataclass(frozen=True)
class Ejercicio:
    nombre: str
    series: int
    repeticiones: str
    peso: str | None = None
    descanso: str | None = None
    notas: str | None = None

    @classmethod
    def desde_dict(cls, datos: dict) -> "Ejercicio":
        return cls(
            nombre=datos["nombre"],
            series=datos["series"],
            repeticiones=datos["repeticiones"],
            peso=datos.get("peso"),
            descanso=datos.get("descanso"),
            notas=datos.get("notas"),
        )

    def a_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "series": self.series,
            "repeticiones": self.repeticiones,
            "peso": self.peso,
            "descanso": self.descanso,
            "notas": self.notas,
        }
