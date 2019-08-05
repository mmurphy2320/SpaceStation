import requests
from datetime import datetime
import numpy
import pandas
from pandas import DataFrame

class ISS:

    def __init__(self):
        self.astro_url = 'http://api.open-notify.org/astros.json'
        self.loc_url = 'http://api.open-notify.org/iss-now.json'
        self.astros = self.get_astros()
        self.loc_json = self.get_loc_json()
        self.lat = self.get_lat()
        self.long = self.get_long()
        self.time = self.get_time()

    def get_astros(self):
        astros = []
        astros_df = requests.get(self.astro_url)
        astros_json = astros_df.json()
        for x in astros_json['people']:
            astros.append(x['name'])
        return astros

    def get_loc_json(self):
        loc_df = requests.get(self.loc_url)
        return loc_df.json()

    def get_lat(self):
        return self.loc_json['iss_position']['latitude']

    def get_long(self):
        return self.loc_json['iss_position']['longitude']

    def get_time(self):
        dt_obj = datetime.fromtimestamp(self.loc_json['timestamp'])
        dt_str = dt_obj.strftime('%m-%d-%Y %H:%M:%S')
        return dt_str


    def write_data(self):
        data = {'Time': self.time, 'Astronauts': self.astros, 'Latitude':
         self.lat, 'Longitude': self.long}
        df = DataFrame(data=data)
        try:
            with open('iss_data.csv', 'w') as file:
                df.tocsv(file)
        except:
            print('WTF IS WRONG!!')

    # TODO - Build data writing functions to CSV and troubleshoot pandas
    # Check current directory for csv named iss_data.csv
    # if exists, continue and append data to it.  It not, create and append data to it



myData = ISS()
print(myData.astros)
print(myData.lat)
print(myData.long)
print(myData.time)
