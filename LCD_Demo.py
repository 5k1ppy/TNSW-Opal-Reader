from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from lib_tft24T import TFT24T
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import spidev
from time import sleep

#For LCD SCREEN:
DC = 18
RST = 23

# Create TFT LCD/TOUCH object:
TFT = TFT24T(spidev.SpiDev(), GPIO, landscape=False)

# Initialize display.
TFT.initLCD(DC, RST)
# If rst is omitted then tie rst pin to +3.3V
# If led is omitted then tie led pin to +3.3V

# Get the PIL Draw object to start drawing on the display buffer.
draw = TFT.draw()

TFT.clear((255, 0, 0))
# Alternatively can clear to a black screen by simply calling:
TFT.clear()

while 1:
    print('Loading image...')
    # image = Image.open('opal.png')
    draw = TFT.draw()
    # Resize the image and rotate it so it's 240x320 pixels.
    # image = image.rotate(90,0,1).resize((240, 320))
    # Draw the image on the display hardware.
    print('Drawing image')
    # TFT.display(image)
    draw.rectangle((0, 0, 240, 320), outline=(0,143,0), fill=(0,143,0))
    draw.rectangle((0, 104, 240, 106), outline=(255,255,255), fill=(255,255,255))
    draw.bitmap((72, 6), Image.open('checkmark.png').rotate(90,0,1), fill="white")
    TFT.display()
    sleep(3)
    print('Loading image2...')
    image = Image.open('opal2.png')
    # Resize the image and rotate it so it's 240x320 pixels.
    image = image.rotate(90,0,1).resize((240, 320))
    # Draw the image on the display hardware.
    print('Drawing image')
    TFT.display(image)
