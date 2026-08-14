from dataclasses import dataclass


@dataclass(frozen=True)
class RegistroPeso:
    semana: str
    peso_kg: float
    fecha_registro: str

    @classmethod
    def desde_dict(cls, semana: str, datos: dict) -> "RegistroPeso":
        return cls(
            semana=semana,
            peso_kg=datos["peso_kg"],
            fecha_registro=datos["fecha_registro"],
        )

    def a_dict(self) -> dict:
        return {"peso_kg": self.peso_kg, "fecha_registro": self.fecha_registro}
