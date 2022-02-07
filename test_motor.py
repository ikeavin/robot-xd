import pyvesc
import time
import serial

def pack(value) -> bytes:
    message = pyvesc.SetCurrent(value)
    packet = pyvesc.encode(message)
    return packet


port = serial.Serial(port='/dev/ttyACM0', 
		     baudrate=11520, 
		     parity=serial.PARITY_NONE,
		     timeout = .1,
             bytesize=serial.EIGHTBITS)
             
while 1 == 1:
    current = 3000
    packet = pack(current)
    port.write(packet)
    port.flush()

