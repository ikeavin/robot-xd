from Motor import VESCMotors

motor = VESCMotors() 
for x in range (1, 20):
    print(str(x) + "0k")
    motor.driveForward(2, 10000 * x)

motor.zeroCurrentForSeconds(2)
motor.driveRight(5, 80000)
motor.zeroCurrentForSeconds(2)
motor.driveBackward(5, 80000)
motor.zeroCurrentForSeconds(2)
motor.driveLeft(5, 80000)
motor.zeroCurrentForSeconds(2)

