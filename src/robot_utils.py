from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
from spike.operator import less_than_or_equal_to
from spike.operator import greater_than_or_equal_to

motion_sensor = MotionSensor()
motion_sensor.reset_yaw_angle()
timer = Timer()
motor_pair = MotorPair('A', 'E')  # replace with correct port for tank motors
distance_sensor = DistanceSensor('B') # replace with correct port for distance sensor


def right_turn(amount): # Makes a method to turn right. amount = angle
    motor_pair.start_tank(25, -25) # inplace right turn
    wait_until(motion_sensor.get_yaw_angle, greater_than_or_equal_to, amount) #Waits until the yaw angle is greater than or equal to angle
    motor_pair.stop() #Stops motor
    print(motion_sensor.get_yaw_angle()) #Prints yaw angle
    motion_sensor.reset_yaw_angle() #Resets yaw angle

def left_turn(amount): #Makes a method to turn left. amount = angle.
    motor_pair.start_tank(-25, 25) # inplace left turn
    wait_until(motion_sensor.get_yaw_angle, less_than_or_equal_to, amount) #Waits until the yaw angle is less than or equal to angle
    motor_pair.stop() #Stops motor
    print(motion_sensor.get_yaw_angle()) # prints yaw angle
    motion_sensor.reset_yaw_angle() # resets yaw angle

def move_distance_open_loop(distance, unit):
    motor_pair.set_motor_rotation(pi*3.5, 'in') # replace with diameter of robot wheel
    motor_pair.move(distance, unit)

def move_distance_closed_loop(target_distance):
    distance_inches = distance_sensor.get_distance_inches()
    print(distance_inches)
    moving_distance = distance_inches - target_distance
    print(moving_distance)
    motor_pair.start()
    distance_sensor.wait_for_distance_closer_than(moving_distance, 'in')
    motor_pair.stop()

def move_straight_closed_loop(time, speed):
    timer.reset()
    motion_sensor.reset_yaw_angle()
    while timer.now() < time:
        angle = motion_sensor.get_yaw_angle()
        motor_pair.start_tank(speed - angle, speed + angle)
    motor_pair.stop()
    print('current yaw angle ', angle, ' time elapsed ', timer.now())    

