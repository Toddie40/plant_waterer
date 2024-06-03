import numpy as np
import time
import json

class test_data_monitor:

    def __init__(self):
        self.data_path = "./"

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

    def add_plant(self, name, sensor_no):
        print(f"Adding plant: {name} to sensor: {sensor_no}")
        return True

    def remove_plant(self, sensor_no):
        print(f"Removing plant from sensor: {sensor_no}")
        return True    

    
    def get_status(self):
        print("getting current monitor status...")
        with open("test_data/monitor_status_test.json", "r") as data_file:
            
            py_object = json.loads(data_file.read())
            sensors = py_object['sensors']
            valves = py_object['valves']
            pump = py_object['pump'] 
            return sensors, valves, pump
            
    
    def water(self, plant_no):
        self.close_all_valves()
        self.open_valve(plant_no)
        self.start_pump()
        time.sleep(5)
        self.stop_pump()
        self.close_valve(plant_no)
        return True
    