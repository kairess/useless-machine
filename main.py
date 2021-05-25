from dynamikontrol import Module
import time

module = Module()

module.motor.angle(60)

def on():
    time.sleep(0.5)
    module.motor.angle(-23)
    time.sleep(0.7)
    module.motor.angle(60)

module.switch.on(on)

while True:
    time.sleep(0.5)

module.disconnect()
