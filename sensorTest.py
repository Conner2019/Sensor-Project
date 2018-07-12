import time
import RPi.GPIO as GPIO
from qhue import Bridge
from qhue import QhueException

try:
    GPIO.setmode(GPIO.BOARD) # use board pin numbers
    # define pin #7 as input pin
    pin = 7
    GPIO.setup(pin, GPIO.IN) 
    counter = 0
    sCount = 0
    temp = 0

    b = Bridge("192.168.1.167", '0lx0Wv2k0vj1rxyPlHjYQo23fo6ODunq6EEqn-Gk')
    groups = b.groups

    while 1:
        try:
          if GPIO.input(pin) == GPIO.LOW:
            sCount += 5
            temp = 0
            if sCount > 220:
              sCount = 220
            counter += 1
            print ("Sound Dectected", str(counter))
            b.groups[0].action(bri = sCount + 25, on = True, hue = 4000)
            time.sleep(.5)
          else:
            sCount = 0
            counter = 0
            temp += 1
            print ("It has been quiet for " + str(temp) + " second(s)")
            if temp > 4:
                b.groups[0].action(bri = sCount, on = False)
            time.sleep(1)
        except QhueException:
            pass
except KeyboardInterrupt:
    b.groups[0].action(on = False)
