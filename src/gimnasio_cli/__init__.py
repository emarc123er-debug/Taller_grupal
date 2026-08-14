import argparse
import sys

from gimnasio_cli.controllers.rutina_controller import RutinaController
from gimnasio_cli.views.cli_view import CLIView


def _construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gimnasio-cli",
        description="Consulta las rutinas de gimnasio de lunes a viernes.",
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    subparsers.add_parser("semana", help="Muestra el estado de los 5 días.")

    parser_dia = subparsers.add_parser("dia", help="Muestra la rutina de un día.")
    parser_dia.add_argument("nombre", help="lunes, martes, miercoles, jueves o viernes")

    return parser


def main() -> None:
    parser = _construir_parser()
    args = parser.parse_args()

    controller = RutinaController()
    view = CLIView()

    if args.comando == "semana":
        view.mostrar_semana(controller.estado_semana())
        return

    if args.comando == "dia":
        try:
            rutina = controller.rutina_del_dia(args.nombre)
        except ValueError as error:
            view.mostrar_error(str(error))
            sys.exit(1)
        view.mostrar_rutina(rutina)
