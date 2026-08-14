from gimnasio_cli.models.dia import Dia
from gimnasio_cli.models.rutina import Rutina


class CLIView:
    """Presenta las rutinas por consola."""

    def mostrar_semana(self, semana: dict[Dia, Rutina]) -> None:
        print("Rutinas de la semana (lunes a viernes):")
        for dia in Dia.orden_semana():
            rutina = semana[dia]
            estado = "definida" if rutina.definida else "pendiente"
            print(f"  {dia.value.capitalize():<10} {estado}")

    def mostrar_rutina(self, rutina: Rutina) -> None:
        print(f"Rutina del {rutina.dia.value}:")
        if not rutina.definida:
            print("  (sin ejercicios definidos todavía)")
            return
        for ejercicio in rutina.ejercicios:
            detalle = f"  - {ejercicio.nombre}: {ejercicio.series}x{ejercicio.repeticiones}"
            if ejercicio.descanso:
                detalle += f", descanso {ejercicio.descanso}"
            if ejercicio.peso:
                detalle += f", peso {ejercicio.peso}"
            if ejercicio.notas:
                detalle += f" ({ejercicio.notas})"
            print(detalle)

    def mostrar_error(self, mensaje: str) -> None:
        print(f"Error: {mensaje}")
