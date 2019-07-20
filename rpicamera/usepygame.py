import pygame
import pygame.camera
#from pygame.locals import *

pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode((640, 480), 0)


def main():
    camlist = pygame.camera.list_cameras()
    if camlist:
        print('camera {} is detected'.format(camlist[0]))
        cam = pygame.camera.Camera(camlist[0], (640, 480))
        cam.start()
        image = cam.get_image()
        print(image)
        screen.blit(
            image,
            (0, 0),
        )
        pygame.display.update()
    else:
        raise ValueError('Sorry no cameras detected')
    print('end program')
if __name__ == '__main__':
    main()
