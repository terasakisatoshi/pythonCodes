"""
Capture frame from Official Raspberry Pi camera for 5 seconds
You can use it even RaspberryPi lite
usage:

sudo apt update
sudo apt install python3-picamera
python3 capture5sec.py
"""
import time

import picamera


def main():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        time.sleep(5)
        camera.stop_preview()

if __name__ == '__main__':
    main()
