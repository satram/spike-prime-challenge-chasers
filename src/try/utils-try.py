from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
motor_pair = MotorPair('C','D')
motorC = Motor('C')
motorD = Motor('D')
def left_or_right(angle):
    #Right turn
    #if yaw_angle=-89 motorC.move(18,'cm')
    #Left turn 
    #if yaw_angle=-88 motorD.move(-14, 'cm')
    while hub.motion_sensor.get_yaw_angle() < angle:
        motorC.start(-50)
    motorC.stop()

#motor_pair.move(13,'cm')
hub.motion_sensor.reset_yaw_angle()
left_or_right(45)
print(hub.motion_sensor.get_yaw_angle())


def move_straight_given_distance(distance, unit):   
    for count in range(0, 12)():
        hub.move(distance /12, 'in')