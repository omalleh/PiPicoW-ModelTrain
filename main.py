import machine
import socket
import network
import time
from machine import Pin
from machine import Pin, PWM
import webpage

# WIFI Configuration
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("PickleOffice","Ninjarabbitpants!01")
 
# Setup Outputs
fwdLed = Pin(2, Pin.OUT)
revLed = Pin(3, Pin.OUT)
day = Pin(4, Pin.OUT)   
night = Pin(5, Pin.OUT) 
coach = Pin(6, Pin.OUT)
onBoard = Pin("LED", Pin.OUT)

fwdPin = 20 
revPin = 21 
pwmPin = 17 


def motorMove(speed,direction,speedGP,cwGP,acwGP):
    print(speed,direction,speedGP,cwGP,acwGP)
    if speed > 100: speed=100
    if speed < 0: speed=0
    Speed = PWM(Pin(speedGP))
    Speed.freq(20000)
    cw = Pin(cwGP, Pin.OUT)
    acw = Pin(acwGP, Pin.OUT)
    Speed.duty_u16(int(speed/100*65536))
    print(int(speed/100*65536))
    if direction < 0:
      cw.value(0)
      acw.value(1) 
    if direction == 0:
      cw.value(0)
      acw.value(0)
    if direction > 0:
      cw.value(1)
      acw.value(0)
     
# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)
    onBoard.on()
    


# Do the things
def serve(connection):
    speed = 0
    direction = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        print(request)

        # Boolean Contols         
        if request == '/off?':
            direction = 0
            day.low()
            night.low()
            coach.low()
            fwdLed.low()
            revLed.low()
            motorMove(0,direction,pwmPin,fwdPin,revPin)
            
        elif request == '/day?':
            day.high()
            night.low()
            coach.low()
        elif request == '/night?':
            day.low()
            night.high()
        elif request == '/coach?':
            coach.high()
            
        # FORWARD CONTROL     
        elif '/forward?' in request:
            direction = 1
            fwdLed.high()
            revLed.low()
            
            try:
                index = request.find('motor') + len('motor=')
                speed = int(float(request[index]))
                print(speed)
            except (ValueError, IndexError) as error:
                print(error)
                pass
            
            motorMove(speed*10,direction,pwmPin,fwdPin,revPin)
            

        # REVERSE CONTROL        
        elif '/reverse?' in request:
            direction = -1
            fwdLed.low()
            revLed.high()
            
            try:
                index = request.find('motor') + len('motor=')
                speed = int(float(request[index]))
                print(speed)
            except (ValueError, IndexError) as error:
                print(error)
                pass
            
            motorMove(speed*10,direction,pwmPin,fwdPin,revPin)
            
        # Values for graphic 
        showSpeed = '%.2f'%speed
        
        if direction == 1:
            showDirection = 'Forward'
        elif direction == 0:
            showDirection = 'Stopped'
        elif direction == -1:
            showDirection = 'Reverse'
            
        tacho = speed * 13.8
        
        html = webpage.webpage(showDirection,showSpeed,tacho)
        client.send(html)
        client.close()
 
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return(connection)
 
 
try:
    if ip is not None:
        connection=open_socket(ip)
        serve(connection)
except KeyboardInterrupt:
    machine.reset()