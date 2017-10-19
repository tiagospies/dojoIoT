import network
import machine 
import time 
from machine import Pin
from machine import ADC
import urequests
import ujson

#GPIO of red-switch
doorSensor = Pin(0, Pin.IN)

IFTTT_SERVER = "http://maker.ifttt.com/trigger/opendoor/with/key/"
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

def send_status_open():
    payload = "{\n\t\"value1\":\"Aberta\"\n}"
    headers1 = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }
    response = urequests.post(IFTTT_URL_CALL, headers = headers1, data=payload)

def send_status_close():
    payload = "{\n\t\"value1\":\"Fechada\"\n}"
    headers1 = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }
    response = urequests.post(IFTTT_URL_CALL, headers = headers1, data=payload)

send_status_open()
send_status_close()

#doorSensor.irq(trigger=Pin.IRQ_FALLING, handler=send_status_close)
#doorSensor.irq(trigger=Pin.IRQ_RISING, handler=send_status_open)



