#!/bin/bash

read -p "Enter video title: " vidTitle

if [ -e /home/pi/sarahsVideos/$vidTitle".h264" ]
then
	echo "File already exists! Aborting!"
	exit	
fi


raspivid --mode 4 -t 0 --preview '0,0,640,480' --opacity 240 --framerate 30 --exposure fixedfps --shutter 1000 -o /home/pi/sarahsVideos/$vidTitle".h264"


