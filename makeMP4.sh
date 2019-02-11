#!/bin/bash

for video in /home/pi/sarahsVideos/*.h264; do

	MP4Box -fps 30 -add $video ${video::-4}"mp4"
done
