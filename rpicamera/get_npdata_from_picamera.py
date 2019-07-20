"""
Capture frame from Official RaspberryPi camera, and convert them numpy array of RGB form

sudo apt update
sudo apt install python3-picamera
sudo apt install python3-pil
python3 get_npdata_from_picamera.py
"""

import time

import numpy as np
import picamera
from picamera.array import PiRGBArray
from PIL import Image


def main():
    with picamera.PiCamera() as camera:
        with PiRGBArray(camera) as stream:
            camera.resolution = (640, 480)
            camera.start_preview()
            start = time.time()
            while time.time() - start < 5:
                camera.capture(stream, 'rgb', use_video_port=True)
                pilImg = Image.fromarray(stream.array)
                pilImg.resize((10, 8))
                np_img = np.asarray(pilImg)
                print(np_img)
                stream.truncate(0)
            camera.stop_preview()


if __name__ == '__main__':
    main()
