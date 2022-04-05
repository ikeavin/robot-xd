from Motor import VESCMotors

motor = VESCMotors() 
motor.driveForward(10, 80000)
motor.zeroCurrentForSeconds(2)
motor.driveRight(10, 80000)
motor.zeroCurrentForSeconds(2)
motor.driveBackward(10, 80000)
motor.zeroCurrentForSeconds(2)
motor.driveLeft(10, 80000)
motor.zeroCurrentForSeconds(2)

