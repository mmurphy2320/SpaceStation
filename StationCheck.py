import json
import urllib.request
from datetime import datetime
import turtle
import time

# TODO - Switch API call to requests library
# TODO - Modify string formatting to f'strings

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
people = result['people']
print('The number of people in space is {}.  Their names and craft are below:\n'.format(result['number']))
for X in people:
    print('Name: {} \nCraft: {}\n'.format(X['name'], X['craft']))

pos_url = 'http://api.open-notify.org/iss-now.json'
pos_response = urllib.request.urlopen(pos_url)
pos_result = json.loads(pos_response.read())
iss_location = pos_result['iss_position']
iss_lat = float(iss_location['latitude'])
iss_long = float(iss_location['longitude'])
time = pos_result['timestamp']
dt_obj = datetime.fromtimestamp(time)
dt_str = dt_obj.strftime('%m-%d-%Y %H:%M:%S')
print('At {} the ISS is located above:'.format(dt_str))
print('Latitude: {}\nLongitude: {}'.format(iss_lat, iss_long))

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
iss.goto(iss_long, iss_lat)
screen.exitonclick()
