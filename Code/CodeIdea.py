# Modified version of code.py from https://developer.sony.com/develop/spresense/docs/circuitpython_tutorials_en.html#_sample_code_3
# Show principle of focusstacking focusrail

import board
import sdioio
import storage
import camera

# Initialize SD card storage
sd = sdioio.SDCard(
    clock=board.SDIO_CLOCK,
    command=board.SDIO_COMMAND,
    data=board.SDIO_DATA,
    frequency=25000000)
vfs = storage.VfsFat(sd)
storage.mount(vfs, '/sd')

# Set up camera, assign picture attributes, and take picture
# Write picture data to file `buffer`.
# The following code takes one foto and writes it to the SDCard

cam = camera.Camera()

# Repeat in a loop and increase number of file /sd/image<No>.JPG

loopcounter = 0
howmanyfotos = 10
thefoto = 0
buffer = bytearray(512 * 1024)

while thefoto < howmanyfotos:
    filename = "/sd/image" + thefoto + ".jpg"
    file = open(filename,"wb")
    size = cam.take_picture(buffer, width=1920, height=1080, format=camera.ImageFormat.JPG)
    file.write(buffer, size)
  
# after one photo is taken, move camera for one step

# <commands to access motor>

    thefoto = thefoto + 1


file.close()

# After photos are taken, loop over photos and create stack
# This is a version  that uses open CV to stack fotos - code can be reused here
# https://github.com/produkt-manager/focusstacking/blob/main/Focusstacking_KV260_V1_0.ipynb


# Build and install the final code as described here 
# https://developer.sony.com/develop/spresense/docs/circuitpython_tutorials_en.html#_build_and_deploy_circuitpython_on_spresense_from_sources