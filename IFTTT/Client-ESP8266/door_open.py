import network
import machine 
import time 
from machine import Pin
from machine import ADC
import urequests
import ujson

#GPIO of red-switch
doorSensor = Pin(0, Pin.IN, machine.Pin.PULL_UP)

IFTTT_SERVER = "http://maker.ifttt.com/trigger/opendoor/with/key/"
IFTTT_KEY = "cAa_G_-pTA-FDANT-d6QF2"
IFTTT_URL_CALL = IFTTT_SERVER + IFTTT_KEY
HEADER_REQUEST = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }

def disable_irq():
        doorSensor.irq(handler=None)

def enable_irq():
    doorSensor.irq(trigger=Pin.IRQ_FALLING, handler=send_status_open)

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('tiago', 'tiagoecamila')
        while not sta_if.isconnected():
            machine.idle() 
    print('network config:', sta_if.ifconfig())

def send_status_open(p):
    disable_irq()
    if(p.value() == 0):
        payload = "{\n\t\"value1\":\"Aberta\"\n}"
        response = urequests.post(IFTTT_URL_CALL, headers = HEADER_REQUEST, data = payload)
        response.close()
    enable_irq()
    print('Interrupção acionada.');

def main():
    do_connect()
    doorSensor.irq(trigger=Pin.IRQ_FALLING, handler=send_status_open)

main()