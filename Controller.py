import keyboard
from Motor import VESCMotors

motor = VESCMotors()
power = 60000

while True:
    if keyboard.is_pressed("w"):
        print("You pressed w")
        motor.packetForward(power)
    elif keyboard.is_pressed("a"):
        print("You pressed a")
        motor.packetLeft(power)
    elif keyboard.is_pressed("s"):
        print("You pressed s")
        motor.packetBackward(power)
    elif keyboard.is_pressed("d"):
        print("You pressed d")
        motor.packetRight(power)
    elif keyboard.is_pressed("q"):
        motor.zeroCurrent()
        break
    else:
        motor.zeroCurrent()