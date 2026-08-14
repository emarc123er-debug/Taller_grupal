from enum import Enum


class Dia(str, Enum):
    """Días válidos para una rutina (regla: solo lunes a viernes)."""

    LUNES = "lunes"
    MARTES = "martes"
    MIERCOLES = "miercoles"
    JUEVES = "jueves"
    VIERNES = "viernes"

    @classmethod
    def orden_semana(cls) -> list["Dia"]:
        return [cls.LUNES, cls.MARTES, cls.MIERCOLES, cls.JUEVES, cls.VIERNES]

    @classmethod
    def desde_texto(cls, texto: str) -> "Dia":
        normalizado = (
            texto.strip()
            .lower()
            .replace("é", "e")
            .replace("í", "i")
        )
        try:
            return cls(normalizado)
        except ValueError as error:
            dias_validos = ", ".join(dia.value for dia in cls.orden_semana())
            raise ValueError(
                f"'{texto}' no es un día válido. Días disponibles: {dias_validos}."
            ) from error
