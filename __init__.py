from flask import Flask, render_template, redirect, url_for
import os

from . import plant_monitor as pm

def create_app():

    app = Flask(__name__)
    app.config['DATABASE'] = 'plant_waterer/plant_monitor.sqlite'

    from . import db
    db.init_app(app)

    monitor = pm.PlantMonitor()


    @app.route("/")
    def index():
        return render_template("main.html")

    @app.route("/monitor")
    def webpage_monitor():
        plant_information = monitor.get_status()
        return render_template("monitor.html", plant_info=plant_information)

    @app.route("/controller")
    def webpage_controller():
        plant_information = monitor.get_status()
        return render_template("controller.html", plant_info=plant_information)

    @app.route("/add_plant")
    def webpage_add_plant():
        return render_template("add_plant.html")

    @app.route("/api/<int:plant_no>/water", methods=['POST'])
    def api_water(plant_no):
        monitor.water(plant_no)
        info = monitor.get_status()
        return render_template("monitor.html", plant_info=info)

    @app.route("/api/add_plant/<int:plant_no>/<string:plant_name>")
    def api_add_plant(plant_no, plant_name):
        monitor.add_plant(plant_name, plant_no)
        info = monitor.get_status()
        return render_template("monitor.html", plant_info=info)

    @app.route("/api/start_pump")                                                                                                                                                            
    def api_start_pump():
        monitor.start_pump()
        return redirect(url_for("webpage_controller"), code=302)

    @app.route("/api/stop_pump")                                                                                                                                                            
    def api_stop_pump():
        monitor.stop_pump()
        return redirect(url_for("webpage_controller"), code=302)

    @app.route("/api/open_valve/<int:valve_no>")
    def api_open_valve(valve_no):
        monitor.open_valve(valve_no)
        return redirect(url_for("webpage_controller"), code=302)

    @app.route("/api/close_valve/<int:valve_no>")
    def api_close_valve(valve_no):
        monitor.close_valve(valve_no)
        return redirect(url_for("webpage_controller"), code=302)

    return app