"""
This module lets you practice the use of robot sensors.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Ben Hawkins.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time
import math

# -----------------------------------------------------------------------------
# Done 2:  With your instructor, do quiz questions 1 through 5.
#          After you understand the answers to those questions,
#          mark this _TODO_ as DONE.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Done 3:  With your instructor, do quiz questions 6 through XXX.
#          After you understand the answers to those questions,
#          mark this _TODO_ as DONE.
# -----------------------------------------------------------------------------

def main():
    """ Calls the testing functions. """
    # Un-comment out these tests as you implement the methods they test.
    #run_test_beep_and_tone()
    #run_test_go_straight_for_seconds()
    # run_test_go_straight_for_inches_using_time()
    #run_test_go_straight_for_inches_using_sensor()
    run_test_raise_arm()
    # run_test_lower_arm()
    # run_test_go_straight_until_black()
    # run_test_go_forward_until_distance_is_less_than()
    # run_test_tones_until_touch_sensor_is_pressed()


def run_test_beep_and_tone():
    """
    Tests the:
       -- beep method of the Beeper    class
       -- tone method of the ToneMaker class
    """
    # -------------------------------------------------------------------------
    # Done: 4.  Implement and test this method.
    # -------------------------------------------------------------------------
    # IMPORTANT:
    #   For testing the   beep   method,
    #   make the robot beep 10 times (use a loop!)
    #   with a short pause after each
    #     (Note:  time.sleep(X)    causes a program to pause for X seconds.)
    #   Do not forget to apply the   wait   method to beep, as usual.
    #
    #   For testing the   tone   method,
    #   make the robot make tones ranging from about 100 to about 200,
    #   in increments of 10, with 50 millisecond durations.
    #   Do not forget to apply the   wait   method to tone, as usual.
    # -------------------------------------------------------------------------

    #b = Beeper()
    #for k in range(10):
    #   b.beep().wait()

    t = ToneMaker()
    for k in range(30):
        t.tone(50+k*30,10).wait()


# -----------------------------------------------------------------------------
# done 5:  With your instructor, do quiz questions XXX through XXX.
#          After you understand the answers to those questions,
#          mark this _TODO_ as DONE.
# -----------------------------------------------------------------------------


def run_test_go_straight_for_seconds():
    """
    Tests the   go, stop, and go_straight_for_seconds   methods of DriveSystem.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the following   DriveSystem   methods:')
    print('  go   stop   go_straight_for_seconds')
    print('--------------------------------------------------')

    # Need these for all the tests:
    drive_system = DriveSystem()
    beeper = Beeper()

    # Test 1: Go forward for 5 seconds at full speed.
    print()
    print('Test 1:')
    print('After the beep, I will go forward for 5 seconds at full speed.')
    input('Press the ENTER key to continue.')
    beeper.beep()
    drive_system.go_straight_for_seconds(5, 100)

    # Test 2: Go backward for 2.5 seconds at half speed.
    print()
    print('Test 2:')
    print('After the beep, I will go backward for 2.5 seconds at half speed.')
    input('Press the ENTER key to continue.')
    beeper.beep()
    drive_system.go_straight_for_seconds(2.5, -50)
    # -------------------------------------------------------------------------
    # TODO: 6.  Run the above tests.  Be sure to understand the
    #              go_straight_for_seconds   method of   DriveSystem.
    # -------------------------------------------------------------------------


def run_test_go_straight_for_inches_using_time():
    """
    Tests the   go_straight_for_inches_using_time   method of DriveSystem.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the following   DriveSystem   methods:')
    print('  go_straight_for_inches_using_time')
    print('--------------------------------------------------')

    # Need these for all the tests:
    drive_system = DriveSystem()
    beeper = Beeper()

    # Test 1: Go forward for 24 inches at full speed.
    print()
    print('Test 1:')
    print('After the beep, I will go forward for 24 inches at full speed.')
    input('Press the ENTER key to continue.')
    beeper.beep()
    drive_system.go_straight_for_inches_using_time(24, 100)

    # Test 2: Go backward 12 inches at half speed.
    print()
    print('Test 2:')
    print('After the beep, I will go backward for 12 inches at half speed.')
    input('Press the ENTER key to continue.')
    beeper.beep()
    drive_system.go_straight_for_inches_using_time(12, -50)
    # -------------------------------------------------------------------------
    # TODO: 7.  Run the above tests.  Be sure to understand the
    #              go_straight_for_inches_using_time   method of   DriveSystem.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# TODO 8:  With your instructor, do quiz questions XXX through XXX.
#          After you understand the answers to those questions,
#          mark this _TODO_ as DONE.
# -----------------------------------------------------------------------------

def run_test_go_straight_for_inches_using_sensor():
    """
    Tests the   go_straight_for_inches_using_sensor   method of DriveSystem.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the following   DriveSystem   methods:')
    print('  go_straight_for_inches_using_sensor')
    print('--------------------------------------------------')

    # Need these for all the tests:
    drive_system = DriveSystem()
    beeper = Beeper()

    # Test 1: Go forward for 24 inches at full speed.
    print()
    print('Test 1:')
    print('After the beep, I will go forward for 24 inches at full speed.')
    input('Press the ENTER key to continue.')
    beeper.beep()
    drive_system.go_straight_for_inches_using_sensor(24, 100)

    # Test 2: Go backward for 12 inches at half speed.
    print()
    print('Test 2:')
    print('After the beep, I will go backward for 12 inches at half speed.')
    input('Press the ENTER key to continue.')
    beeper.beep()
    drive_system.go_straight_for_inches_using_sensor(12, -50)

    # -------------------------------------------------------------------------
    # Done: 9.  With your instructor, implement the
    #      go_straight_for_inches_using_sensor    method of   DriveSystem.
    #      The tests are already written for you -- READ THEM (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Done 10:  With your instructor, do quiz questions XXX through XXX.
#          After you understand the answers to those questions,
#          mark this _TODO_ as DONE.
# -----------------------------------------------------------------------------


def run_test_raise_arm():
    """ Tests the   raise_arm   method of ArmAndClaw. """
    print()
    print('--------------------------------------------------')
    print('Testing the   raise_arm   method of ArmAndClaw.')
    print('--------------------------------------------------')

    # Need these for all the tests:
    arm_and_claw = ArmAndClaw()
    beeper = Beeper()

    # Test 1: Raise arm.  Nothing will happen if it is already raised.
    print()
    print('Test 1:')
    print('After the beep, I will raise the arm.')
    input('Press the ENTER key to continue.')
    beeper.beep()
    arm_and_claw.raise_arm()

    # Test 2: Lower the arm a bit and then raise arm.
    print()
    print('Test 2:')
    print('After the beep, I will lower the arm a bit and then raise the arm.')
    input('Press the ENTER key to continue.')
    beeper.beep()

    arm_and_claw.motor.turn_on(-100)
    time.sleep(2)
    arm_and_claw.motor.turn_off()

    time.sleep(2)
    arm_and_claw.raise_arm()

    # -------------------------------------------------------------------------
    # TODO: 11.  With your instructor, implement the
    #      raise_arm    method of   DriveSystem.
    #      The tests are already written for you -- READ THEM (above).
    # -------------------------------------------------------------------------


def run_test_lower_arm():
    """ Tests the   lower_arm   method of ArmAndClaw. """
    print()
    print('--------------------------------------------------')
    print('Testing the   lower_arm   method of ArmAndClaw.')
    print('--------------------------------------------------')

    # Need these for all the tests:
    arm_and_claw = ArmAndClaw()
    beeper = Beeper()

    # Test 1: Raise arm.  Nothing will happen if it is already raised.
    #         Then lower the arm.
    print()
    print('Test 1:')
    print('After the beep, I will raise, then lower, the arm.')
    input('Press the ENTER key to continue.')
    beeper.beep()

    arm_and_claw.raise_arm()
    time.sleep(1)
    arm_and_claw.lower_arm()

    # Test 2: Raise the arm a bit and then lower arm.
    print()
    print('Test 2:')
    print('After the beep, I will raise the arm a bit and then lower the arm.')
    input('Press the ENTER key to continue.')
    beeper.beep()

    arm_and_claw.motor.turn_on(100)
    time.sleep(4)
    arm_and_claw.motor.turn_off()

    time.sleep(2)
    arm_and_claw.lower_arm()

    # -------------------------------------------------------------------------
    # TODO: 12.  With your instructor, implement the
    #      lower_arm    method of   DriveSystem.
    #      The tests are already written for you -- READ THEM (above).
    # -------------------------------------------------------------------------


def run_test_go_straight_until_black():
    """ Tests the   go_straight_until_black   method of DriveSystem. """
    print()
    print('--------------------------------------------------')
    print('Testing the   go_straight_until_black   method of DriveSystem:')
    print('--------------------------------------------------')
    # -------------------------------------------------------------------------
    # TODO: 13. Implement this test method, then implement the method it tests.
    # -------------------------------------------------------------------------


def run_test_go_forward_until_distance_is_less_than():
    """ Tests the   go_forward_until_distance_is_less_than   method of DriveSystem. """
    print()
    print('--------------------------------------------------')
    print('Testing the   go_forward_until_distance_is_less_than   method of DriveSystem:')
    print('--------------------------------------------------')
    # -------------------------------------------------------------------------
    # TODO: 14. Implement this test method, then implement the method it tests.
    # -------------------------------------------------------------------------


def run_test_tones_until_touch_sensor_is_pressed():
    """ Tests the   tones_until_touch_sensor_is_pressed   method of DriveSystem. """
    print()
    print('--------------------------------------------------')
    print('Testing the   go_straight_until_light_intensity_is_within   method of DriveSystem:')
    print('--------------------------------------------------')
    # -------------------------------------------------------------------------
    # TODO: 15. Implement this test method, then implement the method it tests.
    # -------------------------------------------------------------------------


###############################################################################
#    DriveSystem    and    ArmAndClaw    classes.
# Students: You will implement some of the former and all of the latter.
###############################################################################

class DriveSystem(object):
    """
    Controls the robot's motion via GO and STOP methods,
        along with various methods that GO/STOP under control of a sensor.
    """

    def __init__(self):
        """
        What comes in:  Two (optional) sensors.
        What goes out:  Nothing, i.e., None.
        Side effects:
          -- Stores the (optional) sensors.
          -- Constructs two Motors (for the left and right wheels).
        Type hints:
          :type color_sensor:              ColorSensor
          :type infrared_proximity_sensor: InfraredProximitySensor
        """
        self.left_motor = Motor('B')
        self.right_motor = Motor('C')

    def go(self, left_wheel_speed, right_wheel_speed):
        self.left_motor.turn_on(left_wheel_speed)
        self.right_motor.turn_on(right_wheel_speed)

    def stop(self):
        self.left_motor.turn_off()
        self.right_motor.turn_off()

    def go_straight_for_seconds(self, seconds, speed):
        start = time.time()
        self.go(speed, speed)
        # Note: using   time.sleep   to control the time to run is better.
        # We do it with a WHILE loop here for pedagogical reasons.
        while True:
            if time.time() - start >= seconds:
                self.stop()
                break

    def go_straight_for_inches_using_time(self, inches, speed):
        # NOTE to students:  The constant and formula below are not accurate
        seconds_per_inch_at_100 = 10.0  # 1 sec = 10 inches at 100 speed
        seconds = abs(inches * seconds_per_inch_at_100 / speed)

        self.go_straight_for_seconds(seconds, speed)

    def go_straight_for_inches_using_sensor(self, inches, speed):
        inches_per_degree = self.left_motor.WheelCircumference / 360
        desired_degrees = inches / inches_per_degree
        self.left_motor.reset_position()
        self.left_motor.turn_on(speed)
        self.right_motor.turn_on(speed)
        while True:
            if desired_degrees <= abs(self.left_motor.get_position()):
                break
        self.left_motor.turn_off()
        self.right_motor.turn_off()

    def go_straight_until_black(self, speed):
        """
        Goes straight at the given speed until the robot is over
        a black surface, as measured by the color sensor.
        """
        pass

    def go_forward_until_distance_is_less_than(self, inches, speed):
        """
        Goes forward at the given speed until the distance
        to the nearest object, per the infrared proximity sensor,
        is less than the given number of inches.
        """
        pass

    def tones_until_touch_sensor_is_pressed(self):
        """
        Plays an increasing sequence of short tones,
        stopping when the touch sensor is pressed.
        """
        pass


###############################################################################
# Classes built directly upon the underlying EV3 robot modules:
#   -- Motor
#   -- TouchSensor
#   -- ColorSensor
#   -- IR_DistanceSensor
#   --
# USE them, but do NOT modify them.
###############################################################################
class Motor(object):
    WheelCircumference = 1.3 * math.pi

    def __init__(self, port, motor_type='wheel'):
        # port must be 'A', 'B', 'C', or 'D'.  Use 'arm' as motor_type for Arm.
        if motor_type == 'wheel':
            self._motor = ev3.LargeMotor('out' + port)
        else:
            self._motor = ev3.MediumMotor('out' + port)

    def turn_on(self, speed):  # speed must be -100 to 100
        self._motor.run_direct(duty_cycle_sp=speed)

    def turn_off(self):
        self._motor.stop(stop_action="brake")

    def get_position(self):  # Units are degrees (that the motor has rotated).
        return self._motor.position

    def reset_position(self):
        self._motor.position = 0


class TouchSensor(object):
    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._touch_sensor = ev3.TouchSensor('in' + str(port))

    def is_pressed(self):
        """ Returns True if this TouchSensor is pressed, else returns False """
        return self._touch_sensor.is_pressed


class ColorSensor(object):
    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._color_sensor = ev3.ColorSensor('in' + str(port))

    def get_reflected_light_intensity(self):
        """
        Shines red light and returns the intensity of the reflected light.
        The returned value is from 0 to 100,
        but in practice more like 3 to 90+ in our classroom lighting
        with our downward-facing XXX-inches-from-the-ground sensor placement.
        """
        return self._color_sensor.reflected_light_intensity


class InfraredProximitySensor(object):
    def __init__(self, port):
        self._ir_sensor = ev3.InfraredSensor('in' + str(port))

    def get_distance(self):  # port must be 1, 2, 3 or 4
        """
        Returns the distance to the nearest object sensed by this IR sensor.
        Units are: XXX.
        """
        # DCM: Fix above units XXX and add info re width of range.
        return self._ir_sensor.proximity


class Beeper(object):
    def __init__(self):
        self._beeper = ev3.Sound

    def beep(self):
        # DCM: Indicate that this is NON-blocking.
        # DCM: Indicate that returns a subprocess.Popen, which has a WAIT method
        return self._beeper.beep()


class ToneMaker(object):
    def __init__(self):
        self._tone_maker = ev3.Sound

    def tone(self, frequency, duration):
        # DCM: Indicate that this is NON-blocking.
        # DCM: Indicate that returns a subprocess.Popen, which has a WAIT method
        return self._tone_maker.tone(frequency, duration)  # MHz, msec  DCM XXX CTO


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
