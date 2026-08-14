import argparse
import sys

from gimnasio_cli.controllers.peso_controller import PesoController
from gimnasio_cli.controllers.rutina_controller import RutinaController
from gimnasio_cli.views.cli_view import CLIView


def _construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gimnasio-cli",
        description="Rutinas de gimnasio (lunes a viernes) y peso corporal semanal.",
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    subparsers.add_parser("semana", help="Muestra el estado de los 5 días.")

    parser_dia = subparsers.add_parser("dia", help="Muestra la rutina de un día.")
    parser_dia.add_argument("nombre", help="lunes, martes, miercoles, jueves o viernes")

    parser_peso = subparsers.add_parser("peso", help="Registra o consulta el peso corporal.")
    subparsers_peso = parser_peso.add_subparsers(dest="subcomando", required=True)

    parser_peso_registrar = subparsers_peso.add_parser(
        "registrar", help="Registra el peso de la semana actual (o de una semana pasada)."
    )
    parser_peso_registrar.add_argument("peso_kg", type=float, help="Peso en kilogramos")
    parser_peso_registrar.add_argument(
        "--semana",
        help="Semana a editar en formato AAAA-Www (ej. 2026-W32). Por defecto, la semana actual.",
    )

    subparsers_peso.add_parser("ver", help="Muestra el peso de la última semana registrada.")

    return parser


def main() -> None:
    parser = _construir_parser()
    args = parser.parse_args()

    view = CLIView()

    if args.comando == "semana":
        controller = RutinaController()
        view.mostrar_semana(controller.estado_semana())
        return

    if args.comando == "dia":
        controller = RutinaController()
        try:
            rutina = controller.rutina_del_dia(args.nombre)
        except ValueError as error:
            view.mostrar_error(str(error))
            sys.exit(1)
        view.mostrar_rutina(rutina)
        return

    if args.comando == "peso":
        controller = PesoController()

        if args.subcomando == "registrar":
            try:
                registro = controller.registrar_peso(args.peso_kg, args.semana)
            except ValueError as error:
                view.mostrar_error(str(error))
                sys.exit(1)
            view.mostrar_registro_peso(registro)
            return

        if args.subcomando == "ver":
            view.mostrar_peso_mas_reciente(controller.registro_mas_reciente())
            return
