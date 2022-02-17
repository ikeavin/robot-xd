import pyvesc
import time
import serial

#Left side motors
#Move forward with negative current
leftPort = serial.Serial(port='/dev/ttyACM0', 
		     baudrate=11520, 
		     parity=serial.PARITY_NONE,
		     timeout = .1,
             bytesize=serial.EIGHTBITS)
    
#Right side motors
#Move forward with positive current
rightPort = serial.Serial(port='/dev/ttyACM1', 
		     baudrate=11520, 
		     parity=serial.PARITY_NONE,
		     timeout = .1,
             bytesize=serial.EIGHTBITS)

#Convert current into bytes that can be transmitted to the VESC             
def pack(value) -> bytes:
    message = pyvesc.SetCurrent(value)
    packet = pyvesc.encode(message)
    return packet

#Drive forward for specified amount of seconds
def driveForward(seconds):
    endTime = time.time()
    while time.time() < endTime + seconds:
        leftCurrent = -30000
        rightCurrent = -leftCurrent
        leftPacket = pack(leftCurrent)
        rightPacket = pack(rightCurrent)
        leftPort.write(leftPacket)
        rightPort.write(rightPacket)
        leftPort.flush()
        rightPort.flush()
            
driveForward(10)
