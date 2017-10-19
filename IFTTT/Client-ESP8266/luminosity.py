import network
import machine 
import time 
from machine import Pin
from machine import ADC
import urequests

#GPIO of red-switch
button = Pin(0, Pin.IN)

IFTTT_SERVER = "http://maker.ifttt.com/trigger/Luminosity/with/key/"
IFTTT_KEY = "cAa_G_-pTA-FDANT-d6QF2"
IFTTT_URL_CALL = IFTTT_SERVER + IFTTT_KEY

def sub_cb(topic, msg):
    print((topic, msg))

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('tiago', 'tiagoecamila')
        while not sta_if.isconnected():
            machine.idle() 
    print('network config:', sta_if.ifconfig())


do_connect()

def send_ADC_value(value):
    if(value > 100)
        response = urequests.post(IFTTT_URL_CALL, data = { "value1": str(value), value2: "Dia" })

    if(value < 30)
        response = urequests.post(IFTTT_URL_CALL, data = { "value1": str(value), value2: "Noite" })

def main():
    adc = ADC(0)
    while True:
        adcValue = adc.read()
        #send_ADC_value(int(adcValue))
        time.sleep(2)

main()



