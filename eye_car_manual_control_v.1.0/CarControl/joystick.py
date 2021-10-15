#https://pymotw.com/3/socket/tcp.html
# string example: 00/1500/90
import socket
import cv2 as cv

def send_cmd(cmd):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the CarControl is listening
    #server_address = ('localhost', 1081)
    server_address = ('localhost', 1090)
    sock.connect(server_address)
    try:
        # Send data
        message = cmd.encode()
        print(cmd)
        sock.sendall(message)
    finally:
        print('closing socket')
        sock.close()

speed=1500
angle=90
DEFAULT_CMD = '11/1500/90'
joystick = cv.imread("joystick.jpg")
cv.imshow("loystick",joystick)
while True:

    key = cv.waitKey(0)

    if key == ord('q'):
        send_cmd(DEFAULT_CMD)
        break
    if key == ord('s'):
        speed = speed - 20
        pass
    if key == ord('w'):
        speed = speed + 20
        pass
    if key == ord('a'):
        angle = angle + 5
        pass
    if key == ord('d'):
        angle = angle - 5
        pass
    if key == ord(' '):
        speed = 1500
        angle = 90
        pass
    if speed > 1700:
        speed = 1700
        pass
    if speed < 1500:
        speed = 1500
        pass
    if angle > 105:
        angle = 105
        pass
    if angle < 75:
        angle = 75
        pass
    send_cmd('00/'+str(speed)+'/'+str(angle))
