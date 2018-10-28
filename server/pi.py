'''
@author: Bader Zaidan 
'''

try:
    import RPi.GPIO as gpio
    on_pi = True
except RuntimeError:
    on_pi = False

import time
import logging

# BCM 23, line 16
# BCM 24, line 18
server = "covfefemat"
version = 0.01
host = 'localhost'
port = 80
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
logging.info("Initialising: %s/%d %s:%d", server, version, host, port)
#gpio_port = 10
class Pi(object):
    switch = None

    def __init__(self,name, gpio_port):
        self.name = name
        if on_pi:
            gpio.setmode(gpio.BOARD)
            gpio.setup(gpio_port, gpio.OUT)

    def start_brew(self):
        logging.info("Brew start, timer trigger")
        gpio.output(gpio_port, gpio.HIGH) ## or gpio.LOW for off
	time.sleep(30*60)  ## sleep 30m for brewing+heating of baseplate
        self.stop_brew()
        
    def stop_brew(self):
        logging.info("Brew Stop, timer trigger")
        gpio.output(gpio_port, gpio.LOW) ## or gpio.LOW for off
        
    def brew_status(self):
        logging.info("Brew Status")
        
