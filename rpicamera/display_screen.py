"""
Capture frame from Official RaspberryPi camera, 
and convert them numpy array of RGB form and then
display it using pygame

sudo apt update
sudo apt install python3-picamera
sudo apt install python3-pil
python3 get_npdata_from_picamera.py
"""

import os
import time

import numpy as np
import pygame
import picamera
from picamera.array import PiRGBArray
from PIL import Image

"""
When we use this script on your Raspbian lite,
we need to set.
"""
os.environ['SDL_VIDEODRIVER'] = 'fbcon'


def main():
    print('init pygame')
    pygame.init()
    screen_size = (
        pygame.display.Info().current_w,
        pygame.display.Info().current_h
    )
    screen = pygame.display.set_mode(screen_size)
    screen.fill((128, 128, 128))
    print('update')
    pygame.display.update()
    print('updated')
    newsize = (min(screen_size), min(screen_size))
    dest = (
        (screen_size[0] - newsize[0]) // 2,
        (screen_size[1] - newsize[1]) // 2
    )
    with picamera.PiCamera() as camera:
        with PiRGBArray(camera) as stream:
            camera.resolution = (640, 480)
            start = time.time()
            print('start')
            while time.time() - start < 3:
                camera.capture(stream, 'rgb', use_video_port=True)
                pilImg = Image.fromarray(stream.array)
                stream.truncate(0)
                pilImg = pilImg.resize(newsize)
                np_img = np.asarray(pilImg).astype(np.uint8)
                img = pygame.surfarray.make_surface(np_img)
                screen.blit(img, dest)
                pygame.display.update()

if __name__ == '__main__':
    main()
