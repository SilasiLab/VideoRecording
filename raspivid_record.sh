#!/bin/bash

read -p "Enter video title: " vidTitle
read -p "Enter watermark text: " waterMarkText


raspivid --mode 4 -t 0 --preview '0,0,640,480' -a 12 -a $waterMarkText  --opacity 240 --framerate 30 --exposure fixedfps --shutter 1000 -o $vidTitle".h264" 
MP4Box -fps 30 -add $vidTitle".h264" $vidTitle".mp4"