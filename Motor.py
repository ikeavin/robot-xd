import pyvesc
import time
import serial

class VESCMotors:
    def __init__(self) -> None:
        #Left side motors
        #Move forward with negative current
        self.leftPort = serial.Serial(port='/dev/ttyACM0', 
                baudrate=11520, 
                parity=serial.PARITY_NONE,
                timeout = .1,
                bytesize=serial.EIGHTBITS)

        #Right side motors
        #Move forward with positive current
        self.rightPort = serial.Serial(port='/dev/ttyACM1', 
                baudrate=11520, 
                parity=serial.PARITY_NONE,
                timeout = .1,
                bytesize=serial.EIGHTBITS)

    #Convert current into bytes that can be transmitted to the VESC             
    def pack(self, value) -> bytes:
        message = pyvesc.SetCurrent(value)
        packet = pyvesc.encode(message)
        return packet

    #Sends a current of zero to both motors, effectively stopping
    #the robot
    def zeroCurrent(self):
        leftPacket = self.pack(0)
        rightPacket = self.pack(0)
        self.leftPort.write(leftPacket)
        self.rightPort.write(rightPacket)
        self.leftPort.flush()
        self.rightPort.flush()

    def zeroCurrentForSeconds(self, seconds):     
        endTime = time.time()
        while time.time() < endTime + seconds:
            leftPacket = self.pack(0)
            rightPacket = self.pack(0)
            self.leftPort.write(leftPacket)
            self.rightPort.write(rightPacket)
            self.leftPort.flush()
            self.rightPort.flush()
        self.zeroCurrent()
        
    #Drive forward for specified amount of seconds
    def driveForward(self, seconds, power):
        endTime = time.time()
        while time.time() < endTime + seconds:
            leftCurrent = -int(power)
            rightCurrent = -1 * leftCurrent
            leftPacket = self.pack(leftCurrent)
            rightPacket = self.pack(rightCurrent)
            self.leftPort.write(leftPacket)
            self.rightPort.write(rightPacket)
            self.leftPort.flush()
            self.rightPort.flush()
        self.zeroCurrent()

    #Drive backward for specified amount of seconds
    def driveBackward(self, seconds, power):
        endTime = time.time()
        while time.time() < endTime + seconds:
            leftCurrent = int(power)
            rightCurrent = -1 * leftCurrent
            leftPacket = self.pack(leftCurrent)
            rightPacket = self.pack(rightCurrent)
            self.leftPort.write(leftPacket)
            self.rightPort.write(rightPacket)
            self.leftPort.flush()
            self.rightPort.flush()
        self.zeroCurrent()

    #Drive right for specified amount of seconds
    def driveRight(self, seconds, power):
        endTime = time.time()
        while time.time() < endTime + seconds:
            leftCurrent = int(power * .75)
            rightCurrent = int(power)
            leftPacket = self.pack(leftCurrent)
            rightPacket = self.pack(rightCurrent)
            self.leftPort.write(leftPacket)
            self.rightPort.write(rightPacket)
            self.leftPort.flush()
            self.rightPort.flush()
        self.zeroCurrent()

    #Drive left for specified amount of seconds
    def driveLeft(self, seconds, power):
        endTime = time.time()
        while time.time() < endTime + seconds:
            leftCurrent = int(-(power * .75))
            rightCurrent = int(-power)
            leftPacket = self.pack(leftCurrent)
            rightPacket = self.pack(rightCurrent)
            self.leftPort.write(leftPacket)
            self.rightPort.write(rightPacket)
            self.leftPort.flush()
            self.rightPort.flush()
        self.zeroCurrent()
