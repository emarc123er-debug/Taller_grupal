from gimnasio_cli.models.dia import Dia
from gimnasio_cli.models.registro_peso import RegistroPeso
from gimnasio_cli.models.rutina import Rutina
from gimnasio_cli.views.colores import azul


class CLIView:
    """Presenta las rutinas y el peso corporal por consola. Los títulos de
    sección y los datos destacados se resaltan en azul (color de la app,
    especificación 002)."""

    def mostrar_semana(self, semana: dict[Dia, Rutina]) -> None:
        print(azul("Rutinas de la semana (lunes a viernes):"))
        for dia in Dia.orden_semana():
            rutina = semana[dia]
            estado = "definida" if rutina.definida else "pendiente"
            print(f"  {dia.value.capitalize():<10} {estado}")

    def mostrar_rutina(self, rutina: Rutina) -> None:
        print(azul(f"Rutina del {rutina.dia.value}:"))
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

    def mostrar_registro_peso(self, registro: RegistroPeso) -> None:
        print(azul("Peso corporal registrado:"))
        print(f"  Semana {registro.semana}: {azul(f'{registro.peso_kg} kg')} (cargado el {registro.fecha_registro})")

    def mostrar_peso_mas_reciente(self, registro: RegistroPeso | None) -> None:
        print(azul("Peso corporal (última semana registrada):"))
        if registro is None:
            print("  (sin registros todavía)")
            return
        print(f"  Semana {registro.semana}: {azul(f'{registro.peso_kg} kg')} (cargado el {registro.fecha_registro})")

    def mostrar_error(self, mensaje: str) -> None:
        print(f"Error: {mensaje}")
