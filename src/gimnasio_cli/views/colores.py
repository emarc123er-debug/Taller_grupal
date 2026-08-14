_AZUL = "\033[34m"
_RESET = "\033[0m"


def azul(texto: str) -> str:
    return f"{_AZUL}{texto}{_RESET}"
