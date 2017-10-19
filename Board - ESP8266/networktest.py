import network
import machine 
import socket 

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('SSID', 'PW')
        while not sta_if.isconnected():
            machine.idle() 
    print('network config:', sta_if.ifconfig())

do_connect()