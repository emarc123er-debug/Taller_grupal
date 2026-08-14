import re
from datetime import date

_PATRON_SEMANA = re.compile(r"^\d{4}-W(0[1-9]|[1-4]\d|5[0-3])$")


def semana_actual() -> str:
    anio, semana, _ = date.today().isocalendar()
    return f"{anio}-W{semana:02d}"


def validar_semana(texto: str) -> str:
    texto = texto.strip()
    if not _PATRON_SEMANA.match(texto):
        raise ValueError(
            f"'{texto}' no es una semana válida. Formato esperado: AAAA-Www (ej. 2026-W33)."
        )
    return texto
