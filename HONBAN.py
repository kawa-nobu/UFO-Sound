import RPi.GPIO as GPIO
from time import sleep
import pygame.mixer

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(26, GPIO.IN)

GPIO.setup(2, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(4, GPIO.IN)

#------------------------------------
pygame.mixer.init()
pygame.mixer.music.load("a.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
#------------------------------------
sound1 = pygame.mixer.Sound("3.wav") #BS1
sound2 = pygame.mixer.Sound("3.wav") #BS2
sound3 = pygame.mixer.Sound("3G.wav") #BS3
sound4 = pygame.mixer.Sound("1.wav") #MONEY(LS)
sound5 = pygame.mixer.Sound("3Y.wav") #UP
sound6 = pygame.mixer.Sound("3Y.wav") #RETURN1
sound7 = pygame.mixer.Sound("win.wav") #PRIZE_OUT
#------------------------------------
sw_on = 0
sw_on1 = 0
sw_on2 = 0
sw_on3 = 0
sw_on4 = 0
sw_on5 = 0
sw_on6 = 0
#------------------------------------
try:
    while True:
#--------------------------------BS1------------------------
        if GPIO.input(16) == GPIO.HIGH:
           if sw_on == 0:
               sw_on = 1
               print("GPIO_16_ON")
               sound1.play(-1)
               #sleep(10)
        else:
            sw_on = 0
            print("GPIO16_OFF")
#-----------------------------STOP-----------------------
        if sw_on == 0 and sw_on1 == 0 and sw_on2 == 0 and sw_on3 == 0 and sw_on4 == 0 and sw_on5 == 0 and sw_on6 == 0:
           sound1.stop()
           sound2.stop()
           sound3.stop()
           #sound4.stop()
           sound5.stop()
           sound6.stop()
           #sound7.stop()
#----------------------------BS2-------------------------
        if GPIO.input(20) == GPIO.HIGH:
           if sw_on1 == 0:
               sw_on1 = 1
               print("GPIO_20_ON")
               sound2.play(-1)
        else:
            sw_on1 = 0
            print("GPIO20_OFF")
#------------------------------BS3-----------------------
        if GPIO.input(21) == GPIO.HIGH:
           if sw_on2 == 0:
               sw_on2 = 1
               print("GPIO_20_ON")
               sound3.play(-1)
        else:
            sw_on2 = 0
            print("GPIO20_OFF")
#-------------------------MONEY----------------------------
        if GPIO.input(26) == GPIO.HIGH:
           if sw_on3 == 0:
               sw_on3 = 1
               print("GPIO_26_ON")
               sound4.play()
        else:
            sw_on3 = 0
            print("GPIO26_OFF")
#------------------------UP(TS)----------------------------
        if GPIO.input(2) == GPIO.HIGH:
           if sw_on4 == 0:
               sw_on4 = 1
               print("GPIO_2_ON")
               sound5.play(-1)
        else:
            sw_on4 = 0
            print("GPIO2_OFF")
#---------------------------RETURN---------------------------
        if GPIO.input(12) == GPIO.HIGH:
           if sw_on5 == 0:
               sw_on5 = 1
               print("GPIO_12_ON")
               sound6.play(-1)
        else:
            sw_on5 = 0
            print("GPIO12_OFF")
#-------------------------GET_PRIZE---------------------------
        if GPIO.input(4) == GPIO.HIGH:
           if sw_on6 == 0:
               sw_on6 = 1
               print("GPIO_4_ON")
               sound7.play()
        else:
            sw_on6 = 0
            print("GPIO4_OFF")
#--------------------------------------------------------
        sleep(0.1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()

