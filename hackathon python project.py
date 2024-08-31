# main.py
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check for connected controllers
num_joysticks = pygame.joystick.get_count()
if num_joysticks < 2:
    print("Two controllers are required.")
    pygame.quit()
    exit()

# Initialize the joysticks
joystick1 = pygame.joystick.Joystick(0)
joystick2 = pygame.joystick.Joystick(1)
joystick1.init()
joystick2.init()

print("Controllers initialized:")
print(f"Controller 1: {joystick1.get_name()}")
print(f"Controller 2: {joystick2.get_name()}")

try:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Check controller inputs
            if event.type == JOYBUTTONDOWN:
                if event.joy == 0:
                    print(f"Controller 1 Button {event.button} pressed")
                elif event.joy == 1:
                    print(f"Controller 2 Button {event.button} pressed")

            if event.type == JOYAXISMOTION:
                if event.joy == 0:
                    print(f"Controller 1 Axis {event.axis} moved to {event.value}")
                elif event.joy == 1:
                    print(f"Controller 2 Axis {event.axis} moved to {event.value}")

finally:
    pygame.quit()
