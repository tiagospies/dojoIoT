import network
import machine 
import socket 

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<center><h2>A simple webserver for turning HUZZAH Feather LED's on and off with Micropython</h2></center>
<center><h3>(for noobs to both the ESP8266 and Micropython)</h3></center>
<form>
LED0: 
<button name="LED" value="ON0" type="submit">LED ON</button>
<button name="LED" value="OFF0" type="submit">LED OFF</button><br><br>
LED2: 
<button name="LED" value="ON2" type="submit">LED ON</button>
<button name="LED" value="OFF2" type="submit">LED OFF</button>
</form>
</html>
"""

LED0 = machine.Pin(0, machine.Pin.OUT)
LED2 = machine.Pin(2, machine.Pin.OUT)

def handle(socket):
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDON0 = request.find('/?LED=ON0')
    LEDOFF0 = request.find('/?LED=OFF0')
    LEDON2 = request.find('/?LED=ON2')
    LEDOFF2 = request.find('/?LED=OFF2')
    #print("Data: " + str(LEDON0))
    #print("Data2: " + str(LEDOFF0))
    if LEDON0 == 6:
        print('TURN LED0 ON')
        LED0.low()
    if LEDOFF0 == 6:
        print('TURN LED0 OFF')
        LED0.high()
    if LEDON2 == 6:
        print('TURN LED2 ON')
        LED2.low()
    if LEDOFF2 == 6:
        print('TURN LED2 OFF')
        LED2.high()

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('cel tiago', 'tiagoecamila')

        #Setup Socket WebServer
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 80))
        s.listen(1)
        while not sta_if.isconnected():
            try:
                (conn, addr) = s.accept()
                handle(conn)
            except:
                socket.write("HTTP/1.1 500 Internal Server Error\r\n\r\n")
                socket.write("<h1>Internal Server Error</h1>")
            socket.close()
            machine.idle() 
    print('network config:', sta_if.ifconfig())

do_connect()

#sta_if.ifconfig()
