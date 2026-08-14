import os

from flask import Flask, flash, redirect, render_template, request, url_for

from gimnasio_cli.controllers.peso_controller import PesoController
from gimnasio_cli.controllers.rutina_controller import RutinaController
from gimnasio_cli.models.dia import Dia


def crear_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.environ.get("GIMNASIO_SECRET_KEY", os.urandom(24))

    rutina_controller = RutinaController()
    peso_controller = PesoController()

    @app.get("/")
    def inicio():
        return render_template(
            "index.html",
            semana=rutina_controller.estado_semana(),
            dias=Dia.orden_semana(),
            peso=peso_controller.registro_mas_reciente(),
        )

    @app.get("/dia/<nombre>")
    def ver_dia(nombre: str):
        try:
            rutina = rutina_controller.rutina_del_dia(nombre)
        except ValueError as error:
            flash(str(error))
            return redirect(url_for("inicio"))
        return render_template("dia.html", rutina=rutina)

    @app.get("/peso")
    def ver_peso():
        return render_template("peso.html", peso=peso_controller.registro_mas_reciente())

    @app.post("/peso")
    def registrar_peso():
        peso_kg_texto = request.form.get("peso_kg", "")
        semana = request.form.get("semana") or None
        try:
            peso_kg = float(peso_kg_texto)
            peso_controller.registrar_peso(peso_kg, semana)
        except ValueError as error:
            flash(str(error))
        return redirect(url_for("ver_peso"))

    return app


def main() -> None:
    crear_app().run(debug=True)
