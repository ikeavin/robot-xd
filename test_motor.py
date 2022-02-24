from Motor import VESCMotors

motor = VESCMotors() 
motor.driveForward(10)
motor.zeroCurrentForSeconds(5)
motor.driveRight(10)
motor.zeroCurrentForSeconds(5)
motor.driveBackward(10)
motor.zeroCurrentForSeconds(5)
motor.driveLeft(10)
motor.zeroCurrentForSeconds(5)

