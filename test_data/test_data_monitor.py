import numpy as np
import time
import json
import sqlite3

class test_data_monitor:

    def __init__(self, db_path):
        self.data_path = "./"
        self.db_path = db_path

    def start_pump(self):
        print("Starting pump")
        return True

    def stop_pump(self):
        print("Stopping pump")
        return True

    def read_sensor(self, sensor_no):
        # this will need to be made a bit cleverer to convert whatever our voltage is into a meaningful moisture valve
        # perhaps the datasheet will help
        return 3.3 * np.random.rand(1)

    def close_all_valves(self):
        print("Closing all valves")
        return True

    def open_valve(self, valve_no):
        print(f"opening valve {valve_no}")
        return True

    def close_valve(self, valve_no):
        print(f"closing valve {valve_no}")
        return True

    def add_plant(self, name, sensor_no, moisture_threshold):
        print(f"Adding plant: {name} to sensor: {sensor_no}")
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        cursor.execute(f"UPDATE plants SET plant_name=?, moisture_threshold=? WHERE sensor_no=?;", (name, moisture_threshold, sensor_no))
        db.commit()
        db.close()
        return True

    def remove_plant(self, sensor_no):
        print(f"Removing plant from sensor: {sensor_no}")
        # do sql shit
        return True    

    
    def get_status(self):
        print("getting current monitor status...")
        # get plant names and information from the database
        
        plant_info = []
        valves = {}
        pump = {}

        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()
            for sensor_no in range(1,4):
                current_moisture = np.round(self.read_sensor(sensor_no), 2) # get the sensor information from the sensor and push to db
                cursor.execute("UPDATE plants SET moisture=? WHERE sensor_no=?", (float(current_moisture), sensor_no))
                db.commit()
                cursor.execute("SELECT * FROM plants WHERE sensor_no=?", (sensor_no,))
                plant_row_information = cursor.fetchone()
                plant_info.append(plant_row_information)
                print(plant_row_information)
        return plant_info, valves, pump
            
    
    def water(self, plant_no):
        self.close_all_valves()
        self.open_valve(plant_no)
        self.start_pump()
        time.sleep(5)
        self.stop_pump()
        self.close_valve(plant_no)
        return True
    