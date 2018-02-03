# WeChatJump
This is WeChat Jump assistant program

Running: demo.wmv

Android Mobile:
1.get root privileges
2.open Developer options(ex: MI Mobile, Setting->About phone->Kernel Version click repeatedly)
3.download Terminal Emulator
   (1)su
   (2)setprop service.adb.tcp.port 5555
   (3)stop adbd
   (4)start adbd
 
 Python:
 pip install Pillow,numpy,matplotlib
 project directory need copy adb
 
   
   
 Problem1: Device Unauthorized
 Solution: connect mobile by usb,delete C:\Users\username\.android addkey and addkey.pub(PC), Revoke USB debugging authorization and restart Developer Options(Mobile)
 
