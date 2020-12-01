import uos
import time
import camera

from machine import SDCard
uos.mount(SDCard(),'/sd')
uos.chdir('sd')
camera.init(0,format=camera.JPEG)

i=0
while i<10000:
    buf=camera.capture()
    imgname=str(i)+".jpg"
    img=open(imgname,'w')
    img.write(buf)
    img.close()
    time.sleep(1)
    i+=1
