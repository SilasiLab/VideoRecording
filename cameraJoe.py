from picamera import PiCamera
from time import sleep
import os

camera=PiCamera()

input("Press enter to start\n")
sentinel=0
while(sentinel==0):
    menu_choice=int(input("\nChoose one of the following options\n1-Preview "+
                      "\t2-Record\n"))
    if(menu_choice==1):
        camera.start_preview(fullscreen=False, window=(100,20,640,480))
        input("")
        camera.stop_preview()

    if(menu_choice==2):
        resolution_and_framerate=0
        while(resolution_and_framerate!=1 and resolution_and_framerate!=2 and resolution_and_framerate!=3):
            resolution_and_framerate=int(input("Choose one of the "+
                                               "following settings\n"+
                                               "1-1920x1080p 30fps\t"+
                                               "2-1280x720p 60fps\t"+
                                               "3-640x480p 90fps\n"))

            if(resolution_and_framerate==1):
                camera.resolution=(1920,1080)
                camera.framerate=30
                
            if(resolution_and_framerate==2):
                camera.resolution=(1280,720)
                camera.framerate=60

            if(resolution_and_framerate==3):
                camera.resolution=(640,480)
                camera.framerate=90

        shutter_speed=float(input("\nEnter a shutter speed in microseconds\n Note:\n1 second = 1000 milliseconds = 1000000 microseconds\n"))

        while((shutter_speed/1000000)>(1/float(camera.framerate))):
            print("Shutter speed is too large. Please enter a smaller one")
            shutter_speed=float(input("\nEnter a shutter speed\n"))
        camera.shutter_speed=int(shutter_speed)
        
        camera.start_preview(fullscreen=False, window=(0,0,640,480))
        input("\nPress enter to enter a file name and to start recording. To stop recording, press enter again. Pressing enter a third time will start a new recording\n")

        i=1
        while(i>0):
            filename=input('\nEnter a file name\n\n')
            #save_path='/media/pi/2CEF-0745'
            save_path='/media/pi/SILASI'
            completed_video=os.path.join(save_path, filename)
            camera.start_recording(completed_video+'.h264')
            print("Recording Video%d\n\n" %i)
            input("")
            camera.stop_recording()
            camera.stop_preview()
            input("")
            i=i+1
            camera.start_preview(fullscreen=False, window=(0,0,640,480))
            
                                
        
        


