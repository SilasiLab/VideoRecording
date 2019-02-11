#!/bin/bash

read -p "Enter video title: " vidTitle

raspivid --mode 4 -t 0 --preview '0,0,640,480' --opacity 240 --framerate 30 --exposure fixedfps --shutter 1000 -o /home/pi/sarahsVideos/$vidTitle".h264"


